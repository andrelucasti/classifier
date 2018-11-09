import pandas as pd
from elasticsearch import Elasticsearch
from collections import namedtuple
import json

es = Elasticsearch("localhost")

def connect():
    if es.ping():
        print("connected!")
    else:
        print("ohhh shit! what's happening?!")

def getAllValues():

    hints = es.search("", "")

    obj = json.dumps(json2obj(hints))

    print(obj)


def json2obj(hints):
    data = []
    for hit in hints['hits']['hits']:
        v = hit["_source"]
        data.append({'id': v['id'],'name': v['name']})

    result = {"data": data}

    return result



if __name__ == '__main__':
    print("begin...")
    connect()
    getAllValues()