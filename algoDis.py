import numpy as np
import Levenshtein as ls


class AlgoDis:

    def deleteNull(self, data1, data2):
        data1_no_null = []
        data2_no_null = []
        for i in range(len(data1)):
            if (data1[i] != np.nan and data2[i] != np.nan) or ((
                                                                       (type(data1[i]) == np.str and type(
                                                                           data2[i]) == np.str) or (
                                                                               type(data1[i]) == 'list' and type(
                                                                           data2[i]) == 'list')) and (
                                                                       len(data1[i]) != 0 and len(data2[i]) != 0)):
                data1_no_null.append(data1[i])
                data2_no_null.append(data2[i])

            # if (type(data1[i]) == np.str and type(data2[i]) == np.str) or (type(data1[i]) == 'list' and type(
            #         data2[i]) == 'list'):
            #     if len(data1[i]) != 0 and len(data2[i]) != 0:
            #         data1 = np.delete(data1, i)
            #         data2 = np.delete(data2, i)

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

        data1, data2 = self.deleteNull(data1, data2)
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
