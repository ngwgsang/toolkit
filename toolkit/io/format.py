import pandas as pd

def dict_list_to_dataframe(data):
    return pd.DataFrame(data)

def dataframe_to_dict_list(df):
    return df.to_dict(orient="records")

def flatten_dict(d, parent_key='', sep='.'):
    """Chuyển nested dict thành flat dict với key a.b.c"""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
