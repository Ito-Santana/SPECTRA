from jinja2 import Template




class CrimeForm:
    def crime_form_template(self):
        form_template = Template("""
<!DOCTYPE html>
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
            color: #f2622; 
        }

        .white {
            color: white;
        }

        .sonar {
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

        .form-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin-top: -50px; /* Ajuste este valor conforme necessário */
        }

        .form {
            background-color: rgba(255, 255, 255, 0.13);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
            width: 300px;
            color: white;
        }

        .form label {
            display: block;
            margin-top: 15px;
            font-size: 16px;
            font-weight: 500;
        }

        .form input,
        .form select {
            display: block;
            width: 100%;
            padding: 10px;
            margin-top: 8px;
            background-color: rgba(255, 255, 255, 0.07);
            border: none;
            border-radius: 3px;
            font-size: 14px;
            font-weight: 300;
            color: white;
            appearance: none;
            -webkit-appearance: none;
            -moz-appearance: none;
        }

        .form select {
            background-color: rgba(255, 255, 255, 0.07);
            color: white;
        }

        .form select option {
            background-color: rgba(22, 23, 29, 1);
            color: white;
        }

        .form button {
            margin-top: 20px;
            width: 100%;
            padding: 10px;
            background-color: #ffcc00;
            color: #16171d;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }

        .form button:hover {
            background-color: rgba(255, 204, 0, 0.8);
        }

    </style>
</head>
<body>
    <h1>
        <a href="/map" style="text-decoration: none; color: white;">
            <span class="white">SPE<span class="sonar">C</span>TRA</span>
        </a>
    </h1>
    <div class="form-container">
        <form class="form" method="post" action="/">
            <label for="city">Cidade</label>
            <input type="text" id="city" name="city" placeholder="Cidade..." required>

            <label for="neighborhood">Bairro</label>
            <input type="text" id="neighborhood" name="neighborhood" placeholder="Bairro..." required>

            <label for="street">Rua</label>
            <input type="text" id="street" name="street" placeholder="Rua..." required>

            <label for="period">Período</label>
            <select id="period" name="period" required>
                <option value="">Selecione o período</option>
                <option value="manhã">Manhã</option>
                <option value="tarde">Tarde</option>
                <option value="noite">Noite</option>
            </select>

            <label for="crime_type">Tipo de Crime</label>
            <select id="crime_type" name="crime_type" required>
                <option value="">Selecione o tipo de crime</option>
                <option value="Roubo">Roubo</option>
                <option value="Assalto">Assalto</option>
                <option value="Homicidio">Homicídio</option>
                <option value="Estupro">Estupro</option>
                <option value="Crime de trânsito">Crime de trânsito</option>
                <option value="Assedio">Assédio</option>
                <option value="Arrombamento">Arrombamento</option>
            </select>

            <button type="submit">Informar Crime</button>
        </form>
    </div>
</body>
</html>
""")
        return form_template
