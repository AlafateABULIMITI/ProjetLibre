import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Levenshtein as ls
import connDB
import algoDis
import dataCenter

# def separateDa
# ta(data):
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

    # connDB = connDB.ConnDB()
    # myquery = {"countries": 'France'}
    # testData = connDB.read_mongo(db="openFood", collection="products", query=myquery, nbLimit=5)
    # dataItem1 = testData.iloc[0].values
    # dataItem2 = testData.iloc[1].values
    #
    # # print(testData.iloc[0])
    #
    # algoDistance = algoDis.AlgoDis()
    # list1, list2 = algoDistance.deleteNull(dataItem1, dataItem2)
    # print(type(list1[0]))
    # print(list1)
    # selectNumeric=algoDistance.selectNumeric(list1)
    # print(selectNumeric)
    # for i in list1:
    #     print(i)
    # distance=algoDistance.calculateDis(data1=dataItem1,data2=dataItem2)
    # print("la distance est: "+distance)
    file = 'fr.openfoodfacts.org.products.csv'
    df = pd.DataFrame()
    with open(file)as f:
        chunk_iter = pd.read_csv(file, sep='\t', iterator=True, chunksize=100000)
        for chunk in chunk_iter:
            df = pd.concat([ df, chunk ])

    dataCenter = dataCenter.DataCenter()
    colslist = [ 'url', 'product_name', 'brands', 'categories', 'labels', 'allergens_fr', 'traces_fr', 'additives_n',
                 'additives_fr', 'main_category_fr', 'image_small_url', 'energy_100g', 'energy-from-fat_100g',
                 'fat_100g', 'saturated-fat_100g', 'butyric-acid_100g', 'caproic-acid_100g', 'caprylic-acid_100g',
                 'capric-acid_100g', 'lauric-acid_100g', 'myristic-acid_100g', 'palmitic-acid_100g',
                 'stearic-acid_100g', 'arachidic-acid_100g', 'behenic-acid_100g', 'lignoceric-acid_100g',
                 'cerotic-acid_100g', 'montanic-acid_100g', 'melissic-acid_100g', 'monounsaturated-fat_100g',
                 'polyunsaturated-fat_100g', 'omega-3-fat_100g', 'alpha-linolenic-acid_100g',
                 'eicosapentaenoic-acid_100g', 'docosahexaenoic-acid_100g', 'omega-6-fat_100g', 'linoleic-acid_100g',
                 'arachidonic-acid_100g', 'gamma-linolenic-acid_100g', 'dihomo-gamma-linolenic-acid_100g',
                 'omega-9-fat_100g', 'oleic-acid_100g', 'elaidic-acid_100g', 'gondoic-acid_100g', 'mead-acid_100g',
                 'erucic-acid_100g', 'nervonic-acid_100g', 'trans-fat_100g', 'cholesterol_100g', 'carbohydrates_100g',
                 'sugars_100g', 'sucrose_100g', 'glucose_100g', 'fructose_100g', 'lactose_100g', 'maltose_100g',
                 'maltodextrins_100g', 'starch_100g', 'polyols_100g', 'fiber_100g', 'proteins_100g', 'casein_100g',
                 'serum-proteins_100g', 'nucleotides_100g', 'salt_100g', 'sodium_100g', 'alcohol_100g',
                 'vitamin-a_100g', 'beta-carotene_100g', 'vitamin-d_100g', 'vitamin-e_100g', 'vitamin-k_100g',
                 'vitamin-c_100g', 'vitamin-b1_100g', 'vitamin-b2_100g', 'vitamin-pp_100g', 'vitamin-b6_100g',
                 'vitamin-b9_100g', 'folates_100g', 'vitamin-b12_100g', 'biotin_100g', 'pantothenic-acid_100g',
                 'silica_100g', 'bicarbonate_100g', 'potassium_100g', 'chloride_100g', 'calcium_100g',
                 'phosphorus_100g', 'iron_100g', 'magnesium_100g', 'zinc_100g', 'copper_100g', 'manganese_100g',
                 'fluoride_100g', 'selenium_100g', 'chromium_100g', 'molybdenum_100g', 'iodine_100g', 'caffeine_100g',
                 'taurine_100g', 'ph_100g', 'fruits-vegetables-nuts_100g', 'fruits-vegetables-nuts-estimate_100g',
                 'collagen-meat-protein-ratio_100g', 'cocoa_100g', 'chlorophyl_100g', 'carbon-footprint_100g',
                 'nutrition-score-fr_100g', 'nutrition-score-uk_100g', 'glycemic-index_100g', 'water-hardness_100g',
                 'choline_100g', 'phylloquinone_100g', 'beta-glucan_100g', 'inositol_100g', 'carnitine_100g' ]
    df = dataCenter.cleanData(df, colslist)
    cols = df.columns.values.tolist()
    df.info()
    print(cols)
