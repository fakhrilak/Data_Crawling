import bs4 as bs
import urllib.request
import re
import json
import pymongo

def crawling(data):
    newdata = json.loads(data)
    mongo = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = mongo["datacrawling"]
    collection = mydb["crawling"]
    query = {"url":newdata["url"]}
    D = []
    for x in collection.find({},query):
        D = x
    print("test",D["url"])
    if newdata["url"] == D["url"]:
        return "Data Crawling Yang Anda Cari Sudah Ada"
    elif newdata["url"] != D["url"]:
        scraped_data = urllib.request.urlopen(newdata['url'])
        article = scraped_data.read()
        parsed_article = bs.BeautifulSoup(article,'lxml')
        paragraphs = parsed_article.find_all(newdata['type'])
        article_text = ""
        for p in paragraphs:
            article_text += p.text
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["datacrawling"]
        mycol = mydb["crawling"]
        mydict = { "url": str(newdata["url"]),"data":formatted_article_text}
        x = mycol.insert_one(mydict)
        return(formatted_article_text)
