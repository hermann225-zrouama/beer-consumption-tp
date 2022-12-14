# fonction qui trouve la brasserie donnant le plus gros ABV
def find_max_features_by_features(df,feature_to_group,feature_to_find_max):
    return df.groupby(feature_to_group)[feature_to_find_max].max().idxmax()
    
# fonction qui transforme le timestamp en date
def transform_timestamp_to_date(df,pd):
    df['date'] = pd.to_datetime(df['review_time'],unit='s')
    return df