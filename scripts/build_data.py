from sdg.open_sdg import open_sdg_build

def alter_data(df):
    column_fixes = {
        'Yeat': 'Year',
        'السنة': 'Year',
    }
    df = df.rename(columns=column_fixes)
    return df

open_sdg_build(config='config_data.yml', alter_data=alter_data)
