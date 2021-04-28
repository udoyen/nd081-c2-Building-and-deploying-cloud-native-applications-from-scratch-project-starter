import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://myneighborlycosmoacc:FfPutq1TardvkmWnodcUSCYvRssgDiZuToNjR4YX4fUI4H2TZ1vWFFpadEy3Q1wi7Hc5jL8U6B7yIivQsLRpAw==@myneighborlycosmoacc.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@myneighborlycosmoacc@"
        client = pymongo.MongoClient(url)
        database = client['azure']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)