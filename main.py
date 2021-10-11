from flask import Flask
import requests


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/<string:n>')
def test(n):
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    querystring = {"q": n}
    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "1a53d552damshed4fa66dee8f368p1c1ab7jsn609e3ef84a7c"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    temp = response.json()
    ##print(temp['d'])
    if 'd' in temp:
        return temp
    else :
        return "Movie Not Found"

if __name__ == "__main__":
    app.run(debug=True)    