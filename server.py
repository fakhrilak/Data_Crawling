from flask import  Flask,request, Response, jsonify
from controllers.entities import entities
from controllers.crawling import crawling
from controllers.get_data_entities import get_data_entities
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

route = "/api/crawling/v1/"


@app.route(route + "entities",methods=['GET', 'POST'])
def entities_routes():
    try:
        if request.method == 'POST':
            data = json.loads(request.data)
            print(request.data)
            ##return coba(data)
    except Exception as e:
        raise

@app.route(route + "crawling",methods=['GET', 'POST'])
def crawling_routes():
        data = json.loads(request.data)
        return crawling(data["body"])

@app.route(route + "getcrawling",methods=['GET', 'POST'])
def get_crawling():
    try:
        if request.method == 'POST':
            data = json.loads(request.data)
            return get_data_entities(data["body"])
    except Exception as e:
        raise

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='6000',debug=True)
