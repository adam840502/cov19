import re
import pandas as pd
from tqdm import tqdm
tqdm.pandas()

def shorten_authors(authors):
    """Turn authors list into '<surname>' or '<surname> et al'"""
    if isinstance(authors, str):
        authors = authors.split(';')
        if len(authors) == 1:
            return authors[0].split(',')[0]
        else:
            return f'{authors[0].split(",")[0]} et al'
    else:
        return authors
    
    
def contain_keywords(series, keyword_list):
    """找 series 裡面每個 entry 是否有包含各個 keyword_list 中的字"""
    
    def contain_keywors_unit_function(entry):
        return [bool(re.search(kw, entry, re.IGNORECASE)) for kw in keyword_list]

    series = series.progress_apply(contain_keywors_unit_function)
    df = series.progress_apply(pd.Series)    # result will be a df
    df.columns = keyword_list
    
    return df