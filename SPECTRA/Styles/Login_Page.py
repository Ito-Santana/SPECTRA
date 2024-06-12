from jinja2 import Template



class LoginStyle:
    def login_template(self):
        self.template_login = Template("""
    <!DOCTYPE html>
<html>
<head>
    <title>SPECTRA</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap" rel="stylesheet">
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

        .background {
            width: 430px;
            height: 520px;
            position: absolute;
            transform: translate(-50%,-50%);
            left: 50%;
            top: 50%;
        }


        .login-container {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            height: calc(100vh - 100px); /* Adjust height to account for margin-top of h1 */
            padding-top: 50px; /* Adjust padding to move form down */
        }

        .login-form {
            height: 450px;
            width: 400px;
            background-color: rgba(255,255,255,0.13);
            position: relative;
            border-radius: 10px;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.1);
            box-shadow: 0 0 40px rgba(8,7,16,0.6);
            padding: 0px 35px;
        }

        .login-form * {
            font-family: 'Poppins',sans-serif;
            color: #ffffff;
            letter-spacing: 0.5px;
            outline: none;
            border: none;
        }

        .login-form h3 {
            font-size: 32px;
            font-weight: 500;
            line-height: 42px;
            text-align: center;
        }

        .login-form label {
            display: block;
            margin-top: 30px;
            font-size: 16px;
            font-weight: 500;
        }

        .login-form input {
            display: block;
            height: 50px;
            width: calc(100% - 20px);
            background-color: rgba(255,255,255,0.07);
            border-radius: 3px;
            padding: 0 10px;
            margin-top: 8px;
            font-size: 14px;
            font-weight: 300;
        }

        .login-form ::placeholder {
            color: #e5e5e5;
        }

        .login-form button {
            margin-top: 50px;
            width: 100%;
            background-color: #ffffff;
            color: #080710;
            padding: 15px 0;
            font-size: 18px;
            font-weight: 600;
            border-radius: 5px;
            cursor: pointer;
        }

        .login-form button:hover {
            background-color: rgba(255,255,255,0.47);
        }

    </style>
</head>
<body>
    <h1>
        <span class="white">SPE<span class="sonar">C</span>TRA</span>
    </h1>
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>
    <div class="login-container">
    <form class="login-form" onsubmit="window.location.href = '/map'; return false;">
        <h3>Login Here</h3>

        <label for="username">Username</label>
        <input type="text" placeholder="Username..." required title="Please fill out this field">

        <label for="password">Password</label>
        <input type="password" placeholder="Password" id="password" required title="Please fill out this field">

        <button type="submit">Log In</button>
    </form>
    </div>
</body>
</html>

        """)
        return self.template_login
    
   