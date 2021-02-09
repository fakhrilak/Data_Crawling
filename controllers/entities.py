import json
from kbbi import KBBI
import nltk
from flask import jsonify

def entities(data):
    response = {}
    text_array = data
    title = text_array.title()
    output = nltk.word_tokenize(title)
    for a in output:
        text = KBBI(a)
        # try:
        #     text = KBBI(a)
        # except Exception as e:
        #     return e
        text_dumps = json.dumps(text.serialisasi(),indent=2)
        text_loads = json.loads(text_dumps)
        A = json.dumps(text_loads["entri"],indent = 2)
        B = json.loads(A)
        C = ''
        data = []
        for i in B:
            C = json.dumps(i["makna"])
            D = json.loads(C)
            print(i)
            for c in D:
                data.append({"arti" : c["submakna"]})
                #print(json.dumps(i["submakna"]))
                response.update({a: data})
    return jsonify(response)
