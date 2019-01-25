from pymongo import MongoClient

def connecDB():
    conn = MongoClient('mongodb://localhost:27017/')
    dblist =conn.list_database_names()
    if 'openFood'in dblist:
        myDB=conn["openFood"]
        collist =myDB .list_collection_names()
        if 'openFood' in collist:
            print("Collection openFood exists")
            return myDB["openFood"]
        else:
            print(' Collection openFood no exists')
    else:
        print(' DB openFood no exists')