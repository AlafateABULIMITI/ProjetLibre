import numpy as np
import Levenshtein as ls
import operator
import math


class AlgoDis:

    def deleteNull(self, data1, data2):
        data1_no_null = []
        data2_no_null = []
        for i in range(len(data1)):
            if isinstance(data1[i], str) and isinstance(data2[i], str):
                if (len(data1[i]) != 0 and len(data2[i]) != 0):
                    if (operator.eq(str.lower(data1[i]), 'unknown') or operator.eq(str.lower(data2[i]), 'unknown')):
                        continue
                    else:
                        data1_no_null.append(data1[i])
                        data2_no_null.append(data2[i])
                else:
                    continue
            else:
                if (isinstance(data1[i], list) and isinstance(data2[i], list)) or (
                        isinstance(data1[i], dict) and isinstance(data2[i], dict)):
                    if len(data1[i]) != 0 and len(data2[i]) != 0:
                        if isinstance(data1[i], list) and isinstance(data2[i], list) and operator.eq(
                                str.lower(data1[i][0]), 'unknown') == False and operator.eq(str.lower(data2[i][0]),
                                                                                            'unknown') == False:
                            data1_no_null.append(data1[i])
                            data2_no_null.append(data2[i])
                        else:
                            continue
                    else:
                        continue
                else:
                    if (isinstance(data1[i], list) == False and isinstance(data2[i], list) == False and
                            isinstance(data1[i], dict) == False and isinstance(data2[i], dict) == False and
                            isinstance(data1[i], str) == False and isinstance(data2[i], str) == False and
                            math.isnan(data1[i]) == False and math.isnan(data2[i]) == False):
                        data1_no_null.append(data1[i])
                        data2_no_null.append(data2[i])
                    else:
                        continue
        return data1_no_null, data2_no_null

    def selectNumeric(self, data):
        data_num = []
        for d in data:
            if isinstance(d, int) or isinstance(d, np.float64):
                data_num.append(d)
        data_num = np.array(data_num)
        return data_num

    def selectStr(self, data):
        data_str = []
        for d in data:
            if isinstance(d, str) or isinstance(d, list) or isinstance(d, dict):
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
