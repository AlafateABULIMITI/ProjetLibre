import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Levenshtein as ls
import connDB


def separateData(data):
    pass


def euclideanDistance(data1, data2):
    dis = np.linalg.norm(data1 - data2)
    return dis


def levenshteinDistance(data1, data2):
    lsdistances = 0
    for i in range(len(data1)):
        lsdistances = ls.distance(data1[i], data2[i]) + lsdistances
    return lsdistances


def calculateDis(data1, data2):
    dis = euclideanDistance(data1, data2) + levenshteinDistance(data1, data2)
    return dis


def cleanData(df):
    # 1.quantitiy
    df.rename(columns={'quantity': 'quantity(g)'}, inplace=True)
    df['quantity(g)'].fillna('0', inplace=True)
    df['quantity(g)'] = df['quantity(g)'].replace('grammes', '', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('kg', '000', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('g', '', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace(' ', '', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('Vrac', '0', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('ml', '', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('capsules', '', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('l', '000', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace(
        '1.008000/12pain', '0', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('c000e', '000', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace(',', '.', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('4x5c000', '0', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('1bun', '0', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('e', '', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('r', '', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('c000', '000', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('(nto)', '', regex=True)
    df['quantity(g)'] = df['quantity(g)'].replace('()', '', regex=True)
    df['quantity(g)'] = df['quantity(g)'].astype(float)



if __name__ == "__main__":
    # file = 'en.openfoodfacts.org.products.csv'
    # df = pd.DataFrame()
    # with open(file)as f:
    #     chunk_iter = pd.read_csv(file, sep='\t', iterator=True, chunksize=100000)
    #     for chunk in chunk_iter:
    #         df = pd.concat([df, chunk])
    #
    # cols = df.columns.values.tolist()
    # df.info()
    # print(cols)
    # openFoodCollection=connDB.connecDB()
    # lines=openFoodCollection.find().count()
    # print(str(lines)+" lines in the collection.")
    #
    # testObjects=openFoodCollection.find().limit(2)
    # for object in testObjects:
    #     print(object)

    connDB = connDB.ConnDB()
    connDB.connect_mongo(port=27017,username="",password="",db="openFood",host="localhost")

    myquery = {"_id": "20172022"}
    testData=connDB.read_mongo(db="openFood",collection="openFood", query=myquery)
    print("nombre est: "+ str(len(testData)))

