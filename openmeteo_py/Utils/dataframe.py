def getDataframe(filename):
    import pandas as pd

    dfJson=pd.read_json(filename+'.json')
    df = pd.DataFrame()
    for i, var in enumerate(dfJson.index):
        df[var] = dfJson.iloc[i].hourly
    return df
