import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Levenshtein as ls

file = 'en.openfoodfacts.org.products.csv'
df = pd.DataFrame()
with open(file)as f:
    chunk_iter = pd.read_csv(file, sep='\t', iterator=True, chunksize=100000)
    for chunk in chunk_iter:
        df = pd.concat([df, chunk])

cols = df.columns.values.tolist()

print(cols)


def separateData(dataset):
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
