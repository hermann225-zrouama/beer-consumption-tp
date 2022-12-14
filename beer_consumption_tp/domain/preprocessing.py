import pandas as pd

def strong_beer_abv(df):
    """Cette fonction retourne la brasserie qui fabrique la biere la plus alcolisé"""
    return df[df['beer_abv']==df['beer_abv'].max()].brewery_name

def all_year_info(df,y):
    beer_id = list(df[df["year"]>y]['beer_beerid'])
    return df[df['beer_beerid'].isin(beer_id)]

def top_beers(df):
    tmp = df.groupby(['beer_name']).aggregate({'review_overall': 'mean',
                                         'review_aroma': 'mean',
                                         'review_palate': 'mean',
                                         'review_taste': 'mean',
                                         'review_appearance': 'mean'})
    mask = (tmp['review_overall'] == tmp['review_overall'].max()) & ((tmp['review_aroma'] == tmp['review_aroma'].max()) | (tmp['review_palate'] == tmp['review_palate'].max()) |  (tmp['review_taste'] == tmp['review_taste'].max()) | (tmp['review_appearance'] == tmp['review_appearance'].max()))
    tmp = tmp[mask]
    return df[df['beer_name'].isin(tmp.index)]

def most_influence_factor(df):
    df3 = df[["review_overall",'review_aroma',"review_appearance","review_taste","review_palate"]]
    corr=df3.corr().drop(index="review_overall")[["review_overall"]]
    res = list(corr[corr["review_overall"]==corr["review_overall"].max()].index)    
    return res 
