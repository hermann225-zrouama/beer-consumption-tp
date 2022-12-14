# fonction qui trouve la brasserie donnant le plus gros ABV
def find_max_features_by_features(df,feature_to_group,feature_to_find_max):
    # grouper par brasserie
    df = df.groupby(feature_to_group)
    # trouver la brasserie avec le plus gros ABV
    max_abv_brewery = df[feature_to_find_max].max().idxmax()
    return max_abv_brewery