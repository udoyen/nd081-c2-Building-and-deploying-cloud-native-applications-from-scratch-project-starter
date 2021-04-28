import azure.functions as func
import pymongo
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = "mongodb://myneighborlycosmoacc:FfPutq1TardvkmWnodcUSCYvRssgDiZuToNjR4YX4fUI4H2TZ1vWFFpadEy3Q1wi7Hc5jL8U6B7yIivQsLRpAw==@myneighborlycosmoacc.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@myneighborlycosmoacc@"
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)} #INFO: Had to remove the bson.ObjectId use to get it to work
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

