import googlemaps
import pandas as pd
import json
from folium.plugins import FeatureGroupSubGroup
import requests
import folium
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



class GoogleMaps:
    def __init__(self):
         self.gmaps = googlemaps.Client(key='INSIRA SUA CHAVE API') #OBS COLOQUE SUA PRÓPRIA CHAVE API AQUI
            # Passando a chave de acesso à api da google
            
    def geocoder_location(self, location):
        geocode_result = self.gmaps.geocode(location)
        if geocode_result:
            latitude = geocode_result[0]['geometry']['location']['lat']
            longitude = geocode_result[0]['geometry']['location']['lng']
            return latitude, longitude
        else:
            return None, None
        
 # A classe GoogleMaps acima, tem a função de transformar o endereço do crime em pontos de latitude e longitude,
 # esses que serão utilizados na classe FMap para criação dos marcadores de crimes

    

class FMap:
    
    def __init__(self):
        
        self.map = folium.Map(
            location=[-8.065569, -34.916540], 
            zoom_start=12, 
            tiles='CartoDB Dark Matter',
            attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.',
            control_scale=False
        )
        # Aqui eu seto a localização inicial do mapa no centro de recife e escolho o tipo do mapa em 'tiles'
        
        self.feature_groups = {
            'Assedio': folium.FeatureGroup(name='Assédio'),
            'Estupro': folium.FeatureGroup(name='Estupro'),
            'Assalto': folium.FeatureGroup(name='Assalto'),
            'Arrastao': folium.FeatureGroup(name='Arrastão'),
            'Arrombamento': folium.FeatureGroup(name='Arrombamento'),
            'Homicidio': folium.FeatureGroup(name='Homicídio'),
            'Crime de trânsito': folium.FeatureGroup(name='Crime de trânsito')
        }
        # Nesse trecho eu adiciono features para que seja possível filtrar os crimes que aparecerão no mapa
        
        for fg in self.feature_groups.values():
            self.map.add_child(fg)
        
        self.layer_control_added = False  # Flag para verificar se o controle de camadas foi adicionado
        
    def add_marker(self, latitude, longitude, crime_type, street, area, period):
        icon = folium.Icon(color='gray')
        
        # Definindo o ícone (cor + fig) com base no tipo de crime 
        if crime_type == 'Assedio':
            icon = folium.Icon(color='darkpurple')
        elif crime_type == 'Estupro':
            icon = folium.Icon(color='darkred')
        elif crime_type == 'Assalto':
            icon = folium.Icon(color='gray')
        elif crime_type == 'Arrastao':
            icon = folium.Icon(color='darkblue')
        elif crime_type == 'Arrombamento':
            icon = folium.Icon(color='orange')
        elif crime_type == 'Homicidio':
            icon = folium.Icon(color='black')
        elif crime_type == 'Crime de trânsito':
            icon = folium.Icon(color='green')
        
        popup_content = f"""
        <h3>{crime_type}</h3>
        <p>Localidade: {street}</p>
        <p>Bairro: {area}</p>
        <p>Período: {period}</p>
        """
        
        marker = folium.Marker(
            location=[latitude, longitude],
            popup=popup_content,
            icon=icon
        )
        
        # Adicionando o marcador ao FeatureGroup correspondente
        if crime_type in self.feature_groups:
            marker.add_to(self.feature_groups[crime_type])
        else:
            marker.add_to(self.map)

    def plot_map(self):
        if not self.layer_control_added:  # Verifica se o controle de camadas já foi adicionado
            folium.LayerControl().add_to(self.map)
            self.layer_control_added = True
        return self.map

    # Basicamente a classe FMap acima é uma classe focada na inicialização do mapa,
    # na adição dos marcadores de crimes e na adição do filtro
    