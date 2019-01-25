import numpy as np
import Levenshtein as ls

# classe pour calculer les distances
class AlgoDis:

    def deleteNull(self, data1, data2):
        data1_no_null = []
        data2_no_null = []
        for d1, d2 in data1, data2:
            if d1 != None and d2 != None:
                data1_no_null.append(d1)
                data2_no_null.append(d2)

        return data1_no_null, data2_no_null

    def selectNumeric(self, data):
        data_num = []
        for d in data:
            if isinstance(d, int):
                data_num.append(d)
        data_num = np.array(data_num)
        return data_num

    def selectStr(self, data):
        data_str = []
        for d in data:
            if isinstance(d, str):
                data_str.append(d)
        data_str = np.array(data_str)
        return data_str

    def euclideanDistance(self, data1, data2):

        data1, data2 = self.deleteNull(data1,data2)
        data1 = self.selectNumeric(data1)
        data2 = self.selectNumeric(data2)

        dis = np.linalg.norm(data1 - data2)
        return dis

    def levenshteinDistance(self, data1, data2):

        data1, data2 = self.deleteNull(data1, data2)
        data2 = self.selectStr(data2)
        data1 = self.selectStr(data1)

        lsdistances = 0
        for i in range(len(data1)):
            lsdistances = ls.distance(data1[i], data2[i]) + lsdistances
        return lsdistances

    def calculateDis(self, data1, data2):
        dis = self.euclideanDistance(data1, data2) + self.levenshteinDistance(data1, data2)
        return dis
