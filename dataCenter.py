import algoDis
from twoGrams import sorVec
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


# classe pour integrer
class DataCenter:
    algoDis = algoDis.AlgoDis()

    def cleanData(self, dataFrame, cols):
        df = dataFrame[ cols ]
        return df

    def selectData(self, dataFrame):
        pass

    def seletPOIs(self, dataFrame):
        data = self.convertDataSet(dataFrame)
        estimator = KMeans(n_clusters=3)
        estimator.fit(data)  # 聚类
        label_pred = estimator.labels_  # 获取聚类标签
        centroids = estimator.cluster_centers_  # 获取聚类中心
        inertia = estimator.inertia_  # 获取聚类准则的总和
        print('inertia')
        print(inertia)
        print('centroids')
        print(centroids)
        print('label_pred')
        print(label_pred)

    def convertDataSet(self, df):
        num_df = pd.DataFrame()
        for index, row in df.iterrows():
            data_num = self.algoDis.selectNumeric(row.values)
            two_gram = self.algoDis.selectStr(row)
            data = np.append(data_num, two_gram)
            data = np.nan_to_num(data)
            df_temp = pd.DataFrame([ data ])
            num_df = pd.concat([ num_df, df_temp ], axis=0)
        return num_df

