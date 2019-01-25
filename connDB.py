from pymongo import MongoClient
import pandas as pd

class ConnDB:

    def connect_mongo(host, port, username, password, db):
        """ A util for making a connection to mongo """
        if username and password:
            mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
            conn = MongoClient(mongo_uri)
        else:
            conn = MongoClient(host, port)

        return conn[db]

    def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
        """ Read from Mongo and Store into DataFrame """

        # Connect to MongoDB
        db = db.connect_mongo(host=host, port=port, username=username, password=password, db=db)

        # Make a query to the specific DB and Collection
        cursor = db[collection].find(query)

        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(cursor))

        return df