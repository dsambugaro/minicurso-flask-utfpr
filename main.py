#coding: utf-8


from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/perfil/<string:username>')
def perfil(username):
    token = "?access_token=23649e966d75f235c03e317aff87785295075e60"
    url = "https://api.github.com/users/" + username + token
    r = requests.get(url)
    if r.status_code == 200:
        url_repos = r.json()['repos_url'] + token
        repos = requests.get(url_repos).json()
        return render_template("perfil.html", user = r.json(), repos = repos)
    else:
        return abort(404)sdfsf

if __name__ == '__main__':
    app.run(debug=True)
