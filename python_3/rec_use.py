import pandas as pd
from Recommender.models import WordVectRecommender


data_file_3= r'walmart\final_data.csv'
data_f = pd.read_csv(data_file_3,index_col=0 ,low_memory=False)
w_recommender = WordVectRecommender(title='NAME',target='DES')
w_recommender.train(data_f)


if __name__ == "__main__":
    # title = 'Kielz Ladies Boots'
    title = """Cereal Kellogg's Extra arándanos 420 g"""
    cols= ['NAME','PRICE','CAT','DES']
    item= data_f.loc[data_f['NAME']==title][cols]
    print(item)
    recommendations = w_recommender.recommend( title, 10 )
    print("RECOMENDATIONS: ----------->")
    print(recommendations[cols])
    print(f"\n\n###########\n{title}\nNAMES: ----------->")
    for index, name in enumerate( recommendations['NAME'].tolist() ):
        print(f"[{index}]:- {name}")