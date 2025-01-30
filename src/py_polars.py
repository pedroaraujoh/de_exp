#%%
# import libs
import kaggle
import polars as pl
# %%
# download dataset
dataset = 'anandshaw2001/netflix-movies-and-tv-shows'
path = f'C:/Users/pedro/Documents/Kaggle/{dataset}'
kaggle.api.dataset_download_files(
    dataset, 
    path=path,
    unzip=True)
# %%
# load to polars abordagem eager
file = 'netflix_titles.csv'
df = pl.read_csv(
    f'{path}/{file}'
)
df_lazy = pl.scan_csv(
    f'{path}/{file}'
)
# %%
# simple manipulation
df2 = df \
    .group_by('country') \
    .agg([
        pl.len().alias('count'),
        pl.median('release_year').alias('release_year_median')
    ])
df2
# %%
df3 = df_lazy.sql(
    'select type, count(*) from self group by type'
)
df3.collect()