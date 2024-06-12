from jinja2 import Template



  
class MapStyle:
    def map_template(self):
        self.template = Template("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SPECTRA</title>
    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            padding: 0;
            height: 100vh;
            overflow: hidden;
            background-color: #16171d;
        }

        h1 {
            text-align: center;
            margin-top: 20px;
            color: white;
        }
        .yellow {
            color: #ffcc00; /* Amarelo */
        }

        .white {
            color: white;
        }
        .sonar{
            color: #ffcc00;
            position: relative;
            display: inline-block;
        }
        
        .sonar::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background-color: white;
            opacity: 0.7;
            animation: sonar 3s ease-out infinite;
        }
        
        @keyframes sonar {
            0% {
                transform: translate(-50%, -50%) scale(0);
                opacity: 0.7;
            }
            100% {
                transform: translate(-50%, -50%) scale(8);
                opacity: 0;
            }
        }

        /* Estilos para o botão */
        .crime-button {
            position: absolute;
            top: 10px;
            right: 20px;
            background-color: #ffcc00;
            color: #16171d;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }

        /* Estilos para o botão quando passa o mouse por cima */
        .crime-button:hover {
            background-color: #ffe066;
        }
    </style>
</head>
<body style="background-color: #16171d;">
     <h1>
        <a href="/map" style="text-decoration: none; color: white;">
            <span class="white">SPE<span class="sonar">C</span>TRA</span>
        </a>
    </h1>
    <button class="crime-button" onclick="window.location.href = '/crime_form';">Informar crime</button>
    <!-- Substitua 'pagina_de_informacao_do_crime.html' pelo URL da página que deseja redirecionar -->
    {{ folium_map_html | safe }}
</body>
</html>

    """)
        return self.template


