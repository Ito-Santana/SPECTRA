# SPECTRA
## Sistema de Previsão e Controle Tático de Riscos e Alertas

![Logo do Projeto](https://github.com/Ito-Santana/SPECTRA/blob/main/Recursos/Logo/LOGO%20VERTICAL.png)

<p align="center">
  <a href="https://youtu.be/fYQhm1CPDAw">
    <img src="https://img.youtube.com/vi/fYQhm1CPDAw/maxresdefault.jpg" alt="Vídeo de Demonstração">
  </a>
</p>
<p align="center">Clique na imagem para assistir</p>


## Descrição
O **SPECTRA** é um sistema  desenvolvido como parte do currículo da disciplina de Projetos, oferecida no curso de Gestão de Tecnologia da Informação pela Cesar School. Seu principal propósito é mapear e analisar em tempo real os índices de criminalidade em ambientes urbanos, utilizando tecnologias avançadas de geolocalização e análise de dados.

O diferencial do SPECTRA está em sua capacidade de plotar pins no mapa, fornecendo uma representação visual imediata dos locais onde ocorreram crimes. Essa funcionalidade permite uma compreensão mais rápida e intuitiva da distribuição geográfica dos eventos criminais, facilitando a identificação de padrões, áreas de risco e necessidades específicas de intervenção.

Com uma interface intuitiva e poderosas ferramentas de visualização de dados, o SPECTRA capacita não apenas os gestores de segurança pública e planejadores urbanos, mas também a população em geral, a tomar decisões informadas e estratégicas para aprimorar a segurança e a qualidade de vida nas cidades. Além disso, sua capacidade de análise em tempo real possibilita uma resposta ágil a eventos emergentes, contribuindo para uma abordagem proativa na prevenção e combate à criminalidade.

O SPECTRA representa um avanço significativo na gestão da segurança urbana, integrando tecnologia, dados e conhecimento para enfrentar os desafios complexos do cenário urbano contemporâneo.


## Fluxograma e Pins

|  Fluxograma                                    | Descrição                                                                                       |
|------------------------------------------------|-------------------------------------------------------------------------------------------------|
| ![Fluxograma do Projeto](https://github.com/Ito-Santana/SPECTRA/blob/main/Recursos/Fluxograma.png) | Inicialmente, o usuário estará na página do mapa, onde poderá filtrar os crimes exibidos ou informar um novo crime.<br><br>Ao inserir um novo crime, o usuário fornecerá a localização, o período e o tipo de crime. Esses dados serão salvos previamente no banco de dados. Simultaneamente, a localização será pesquisada na API do Google para obter as coordenadas de latitude e longitude, que também serão armazenadas no banco de dados.<br><br>Com todas as informações reunidas, um novo marcador (pin) será adicionado à tela inicial. 🌟 |

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| Pins                               | Relação de Cores                                                                               |
|------------------------------------|------------------------------------------------------------------------------------------------|
| ![Fluxograma do Projeto](https://github.com/Ito-Santana/SPECTRA/blob/main/Recursos/pins.png) | Roxo : Assédio<br><br>Vermelho: Estupro<br><br>Cinza: Assalto<br><br>Verde: Crime de Trânsito<br><br>Azul: Arrastão<br><br>Laranja: Arrombamento<br><br>Preto: Homícidio


# Equipe
1. Italo Santana - jiss@cesar.school
2. Guilherme Borges - gbvc@cesar.school
3. Davi Paiva - dpcs@cesar.school
4. Henrique Pimentel - hdgp@cesar.school 
5. Alexandre Sergio - asaaj@cesar.school

# Como Executar

Este é um guia para executar o projeto SPECTRA.

## Pré-requisitos

Antes de começar, verifique se você possui os seguintes requisitos instalados:

- Python 3.x
- Todas as bibliotecas listadas no arquivo `requirements.txt`
- Uma chave API válida do Google Maps. Se você não tiver uma, consulte a documentação oficial [aqui](https://developers.google.com/maps/documentation/geocoding/overview?hl=pt-br).

## Passos para Execução

1. Faça o download do projeto para o seu computador.

2. Instale as bibliotecas necessárias executando o seguinte comando no terminal:


3. No arquivo `Functions/BuildMap.py`, na classe `GoogleMaps`, localize a linha onde está escrito `key=INSIRA SUA CHAVE API` e substitua `INSIRA SUA CHAVE API` pela sua chave API do Google Maps.

4. Execute o código `SPECTRA.py` no terminal:



