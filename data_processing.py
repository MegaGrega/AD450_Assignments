import pandas as pd

def rename_columns(df):
    rename_dict = {
        'Original titlÊ': 'original_title',
        'Genrë¨': 'genre',
        'Unnamed: _8': 'unnamed_8'
    }

    df.columns = [
        rename_dict.get(col, col.strip().lower().replace(' ', '_')) 
        for col in df.columns
    ]

    return df

def remove_fully_null_columns_rows(df):
    df_cleaned = df.dropna(axis=0, how='all').dropna(axis=1, how='all')

    return df_cleaned

def clean_and_fill_content_rating(df):
    df_new = df.copy()
    
    df_new['content_rating'] = df_new['content_rating'].fillna('Unrated')
    
    df_new['content_rating'] = df_new['content_rating'].replace('Not Rated', 'Unrated')

    return df_new

def clean_release_year(df):
    df_new = df.copy()
    
    df_new['release_year_coerce'] = pd.to_datetime(df_new['release_year'], errors='coerce')
    
    df_new['release_year_mixed'] = pd.to_datetime(df_new['release_year'], errors='coerce', format="mixed")

    return df_new

def clean_income(df):
    df_new = df.copy()
    
    df_new['income'] = (
        df_new['income']
        .astype(str)
        .str.replace(r'[$,\s]', '', regex=True)
    )
    
    df_new['income'] = pd.to_numeric(df_new['income'], errors='coerce').astype('Int64')
    
    return df_new