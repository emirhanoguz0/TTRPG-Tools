import pandas as pd
import random

def random_row_selector(ad):
    df = pd.read_csv(ad)
    l = len(df)
    n = random.randint(0,l-1)
    return df.iloc[n,0]