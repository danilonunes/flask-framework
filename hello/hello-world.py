from flask import Flask #importando do pacote flask a classe Flask

app = Flask(__name__)

@app.route('/')
def ola():
    return "<h1>Olá Mundo!</h1>"

@app.route('/en')
def hello():
    return "<h1>Hello world!</h1>"

if __name__ == '__main__':
    app.run()
