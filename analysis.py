import connDB
import algoDis
import pandas as pd

# def separateData(data):
#     pass


# def cleanData(df):
#     # 1.quantitiy
#     df.rename(columns={'quantity': 'quantity(g)'}, inplace=True)
#     df['quantity(g)'].fillna('0', inplace=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('grammes', '', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('kg', '000', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('g', '', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace(' ', '', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('Vrac', '0', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('ml', '', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('capsules', '', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('l', '000', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace(
#         '1.008000/12pain', '0', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('c000e', '000', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace(',', '.', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('4x5c000', '0', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('1bun', '0', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('e', '', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('r', '', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('c000', '000', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('(nto)', '', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].replace('()', '', regex=True)
#     df['quantity(g)'] = df['quantity(g)'].astype(float)


# Main execution
if __name__ == "__main__":
    file = 'en.openfoodfacts.org.products.csv'
    df = pd.DataFrame()
    with open(file)as f:
        chunk_iter = pd.read_csv(file, sep='\t', iterator=True, chunksize=100000)
        for chunk in chunk_iter:
            df = pd.concat([df, chunk])

    cols = df.columns.values.tolist()
    df.info()
    print(cols)

    # openFoodCollection=connDB.connecDB()
    # lines=openFoodCollection.find().count()
    # print(str(lines)+" lines in the collection.")
    #
    # testObjects=openFoodCollection.find().limit(2)
    # for object in testObjects:
    #     print(object)

    # connDB = connDB.ConnDB()
    # myquery = {"countries": 'France'}
    # testData = connDB.read_mongo(db="openFood", collection="openFood", query=myquery, nbLimit=5)
    # dataItem1 = testData.iloc[0].values
    # dataItem2 = testData.iloc[1].values

    # print(testData.iloc[0])

    # algoDistance = algoDis.AlgoDis()
    # list1, list2 = algoDistance.deleteNull(dataItem1, dataItem2)
    # print(len(list1))
    # selectNumeric=algoDistance.selectNumeric(list1)
    # selectStr=algoDistance.selectStr(list1)
    # print(len(selectNumeric))
    # print(len(selectStr))
    # print(len(selectStr))
    # for i in list1:
    #     print(i)
    # distance=algoDistance.calculateDis(data1=dataItem1,data2=dataItem2)
    # print("la distance est: "+distance)
