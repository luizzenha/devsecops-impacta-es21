from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)  

@app.route("/")
def pagina_inicial():
    return "Processo CI com Travis e Deploy no Heroku"

if __name__ == '__main__':
    app.run(debug=True)
