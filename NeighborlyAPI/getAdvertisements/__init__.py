# Requires pip install requests && pip freeze > requirements.txt
import requests
import os
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        payload = {
            "email": "ekojojoshua@hotmail.com",
            "due": "28/4/2021",
            "task": "My new task!"
        }
        response = requests.post(
            os.environ['LOGIC_APP_URL'], data = payload)
        print(f"Success: {response.status_code}")
    except Exception as e:
        print(f"Mail was not sent! {e}")


    try:
        url = "mongodb://myneighborlycosmoacc:FfPutq1TardvkmWnodcUSCYvRssgDiZuToNjR4YX4fUI4H2TZ1vWFFpadEy3Q1wi7Hc5jL8U6B7yIivQsLRpAw==@myneighborlycosmoacc.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@myneighborlycosmoacc@"
        client = pymongo.MongoClient(url)
        database = client['azure']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

