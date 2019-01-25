from pymongo import MongoClient
import pandas as pd

# classe pour connecter avec BD
class ConnDB:

    def connect_mongo(self, host, port, username, password, db):
        """ A util for making a connection to mongo """
        if username and password:
            mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
            conn = MongoClient(mongo_uri)
        else:
            conn = MongoClient(host, port)

        return conn[db]

    def read_mongo(self, db, collection, query={}, host='localhost', port=27017, username=None, password=None,nbLimit=1):
        """ Read from Mongo and Store into DataFrame """

        # Connect to MongoDB
        db = self.connect_mongo(host=host, port=port, username=username, password=password, db=db)

        # Make a query to the specific DB and Collection
        dataSet = db[collection].find(query).limit(nbLimit)

        # Expand the cursor and construct the DataFrame
        df = pd.DataFrame(list(dataSet))

        return df
