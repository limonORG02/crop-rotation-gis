"""
Загрузка и подготовка данных полей
"""
import geopandas as gpd
import pandas as pd
from typing import Tuple




def load_fields(path: str) -> gpd.GeoDataFrame:
"""Загружает геоданные полей (GeoJSON / Shapefile) и возвращает GeoDataFrame.
Ожидается колонка 'crop_type' и 'history' (optional).
"""
gdf = gpd.read_file(path)
# Normalize column names
if 'history' in gdf.columns:
# if stored as string, try to parse
gdf['history'] = gdf['history'].apply(lambda x: x if isinstance(x, list) else (eval(x) if isinstance(x, str) else []))
else:
gdf['history'] = gdf.apply(lambda row: [], axis=1)
return gdf




def summarize_by_crop(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
"""Возвращает сводку по культурам: count, total_area (approx)"""
df = gdf.groupby('crop_type').agg(count=('id', 'count'))
return df.reset_index()
