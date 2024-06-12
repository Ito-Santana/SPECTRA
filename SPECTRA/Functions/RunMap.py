import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template
from Functions.BuildMap import GoogleMaps, FMap
from Styles.Map_Page import MapStyle

class Run:
    def __init__(self):
        self.gmaps = GoogleMaps()
        self.mapa = FMap()
        # Aqui eu faço as instâncias das classes que são reponsáveis pela inicialização do mapa 
        # e  pela conversão da localização para latitude e longitude
        
        
    def load_data(self):
        self.data = pd.read_csv(r'C:\Users\josei\OneDrive\Área de Trabalho\SPECTRA\Database\Crime_data.csv')
      
    def update_search_column(self):
        self.data['Search'] = self.data.apply(
            lambda row: row['Street'] + ' ' + row['Area'] + ' ' + row['City'] if pd.isna(row['Search']) or row['Search'] == "" else row['Search'], 
            axis=1
        )
        # Transformo as colunas recebidas do formularios em uma string única que será justamente a string 
        # pesquisada na api google
            
    def fetch_coordinates(self):
        if self.data['Latitude'].isnull().any():
            for index, row in self.data.iterrows():
                if pd.isna(row['Latitude']) or pd.isna(row['Longitude']):
                    search = row['Search']
                    latitude, longitude = self.gmaps.geocoder_location(search)
                    self.data.at[index, 'Latitude'] = latitude
                    self.data.at[index, 'Longitude'] = longitude

            self.data.to_csv(r'C:\Users\josei\OneDrive\Área de Trabalho\SPECTRA\Database\Crime_data.csv', index=False)
            self.data.to_csv(r'C:\Users\josei\OneDrive\Área de Trabalho\SPECTRA\Database\New_data.csv', index=False)

        # Acima utilizei o if para apenas utilizar o geocoder (api google) nas colunas que a latitude está vazia.
        # Dessa forma eu garanto que ele não sobrecarregará o sistema de pesquisa, refazendo pesquisas 
        # já feitas e deixando lento a visualização do mapa atualizado

    def add_markers_to_map(self):
        for index, row in self.data.iterrows():
            latitude = row['Latitude']
            longitude = row['Longitude']
            crime_type = row['Crime type']
            street = row['Street']
            area = row['Area']
            period = row['Period']
            self.mapa.add_marker(latitude, longitude, crime_type, street, area, period)

        # Para cada linha da base de crimes eu passo os conteudos da célula para a função que adiciona os marcadores,
        # dessa formar os marcadores terão os dados certos.
        
        
    def run(self):
        self.load_data()
        self.update_search_column()
        self.fetch_coordinates()
        self.add_markers_to_map()
        return self.mapa.plot_map().get_root().render()
        
        # A função run, acima, basicamente executa todo o processo de rodar o mapa na ordem certa.
        # As funções '.get_root().render()' são para poder lidar com a representação HTML final do mapa
        # que será integrada a uma aplicação FastAPI.
        
class AddNewCrime:       
    def add_to_csv(self, street, area, city, crime_type, period): 
        file_path = r'C:\Users\josei\OneDrive\Área de Trabalho\SPECTRA\Database\Crime_data.csv'
        
        self.data = pd.read_csv(file_path) 
   
        new_row = pd.DataFrame({'Street': [street], 'Area': [area], 'City': [city], 'Crime type': [crime_type], 'Period': [period]})
   
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        
        self.data.to_csv(file_path, index=False)
 
        # Essa função vai ser chamada para adicionar os crimes informados pelos usuários.
