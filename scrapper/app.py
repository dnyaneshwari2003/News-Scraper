from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_headlines():
    url = 'http://yahoo.com'
    req_data = requests.get(url)
    content = req_data.text
    soup = BeautifulSoup(content, "html.parser")

    headlines = []
    for headline in soup.find_all("h3"):
        raw_headline = headline.get_text()
        headline = raw_headline.strip()
        if len(headline) < 10:
            continue
        headlines.append(headline)

    return headlines

@app.route('/')
def home():
    headlines = get_headlines()
    return render_template("index.html", headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)
