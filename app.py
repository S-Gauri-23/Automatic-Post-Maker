from flask import Flask,url_for,render_template,request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    finalNews=""
    for data in soup.find_all("div",class_="Section_widget_listing__Bf6q8",limit=6):
        news=data.div.div.a["title"]
        finalNews += '\u2022 '+news+'\n'
    #print(finalNews)
    return render_template("index.html",News=finalNews)