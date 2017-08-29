#coding: utf-8

from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", curso="Flask", instrutor="Bruno Mendes")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

@app.route('/usuario/<string:usuario>')
def usuario(usuario):
    return "Usuário %s" % usuario

if __name__ == '__main__':
    app.run(debug=True)
