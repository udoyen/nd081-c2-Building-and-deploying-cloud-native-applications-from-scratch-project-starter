import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://myneighborlycosmoacc:FfPutq1TardvkmWnodcUSCYvRssgDiZuToNjR4YX4fUI4H2TZ1vWFFpadEy3Q1wi7Hc5jL8U6B7yIivQsLRpAw==@myneighborlycosmoacc.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@myneighborlycosmoacc@"
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)} #INFO: Had to remove the bson.ObjectId use to get it to work
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
