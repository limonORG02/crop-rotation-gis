#!/usr/bin/env python3
"""
Генератор синтетических данных для проекта GIS Crop Rotation.
Создаёт:
- Поля (GeoJSON + Shapefile)
- Историю культур и урожайность (CSV)
- Почвенные анализы (CSV)
- Синтетический NDVI (GeoTIFF)
"""

import random
from pathlib import Path
import click
from shapely.geometry import Polygon
import geopandas as gpd
import pandas as pd
import numpy as np
import rasterio
from rasterio.transform import from_origin

CROP_TYPES = ["wheat", "corn", "soybean", "sunflower", "fallow"]


@click.command()
@click.option("--n-fields", default=12, help="Number of fields to generate")
@click.option("--out", default="data/sample_fields.geojson", help="Output GeoJSON path")
def main(n_fields, out):
    records = []

    # простая сетка для полей
    cols = int(max(3, round(n_fields**0.5)))
    size = 0.01  # ~1 км
    i = 0
    for r in range((n_fields + cols - 1) // cols):
        for c in range(cols):
            if i >= n_fields:
                break
            x0 = 60.0 + c * (size * 1.5) + random.uniform(-0.002, 0.002)
            y0 = 41.0 + r * (size * 1.2) + random.uniform(-0.002, 0.002)
            poly = Polygon(
                [
                    (x0, y0),
                    (x0 + size, y0),
                    (x0 + size, y0 + size),
                    (x0, y0 + size),
                ]
            )
            crop = random.choice(CROP_TYPES)
            history = [random.choice(CROP_TYPES) for _ in range(5)]
            rec = {
                "id": i,
                "crop_type": crop,
                "area_ha": round(random.uniform(1.0, 20.0), 2),
                "yield_t_ha": round(random.uniform(1.0, 5.0), 2),
                "history": history,
                "geometry": poly,
            }
            records.append(rec)
            i += 1

    gdf = gpd.GeoDataFrame(records, geometry="geometry", crs="EPSG:4326")

    out_path = Path(out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # сохраняем GeoJSON
    gdf.to_file(out, driver="GeoJSON")
    print(f"Wrote {out}")

    # shapefile
    shp_out = out_path.parent / "sample_fields.shp"
    gdf.to_file(shp_out)
    print(f"Wrote {shp_out}")

    # Soil tests CSV
    soil_records = []
    for rec in records:
        for year in range(2018, 2023):
            soil_records.append(
                {
                    "id": rec["id"],
                    "year": year,
                    "ph": round(random.uniform(5.5, 7.5), 2),
                    "n": round(random.uniform(10, 40), 1),
                    "p": round(random.uniform(5, 30), 1),
                    "k": round(random.uniform(50, 200), 1),
                    "organic_matter": round(random.uniform(1, 5), 2),
                }
            )
    pd.DataFrame(soil_records).to_csv(out_path.parent / "soil_tests.csv", index=False)
    print("Wrote soil_tests.csv")

    # Field yields CSV
    yield_records = []
    for rec in records:
        for year in range(2018, 2023):
            yield_records.append(
                {
                    "id": rec["id"],
                    "year": year,
                    "crop": random.choice(CROP_TYPES),
                    "yield_t_ha": round(random.uniform(1.0, 5.0), 2),
                }
            )
    pd.DataFrame(yield_records).to_csv(out_path.parent / "field_yields.csv", index=False)
    print("Wrote field_yields.csv")

    # NDVI raster (простая карта-градиент)
    width, height = 100, 100
    data = np.random.rand(height, width).astype("float32")
    transform = from_origin(60.0, 41.0 + size * cols, size / 100, size / 100)
    ndvi_path = out_path.parent / "ndvi_2022.tif"
    with rasterio.open(
        ndvi_path,
        "w",
        driver="GTiff",
        height=height,
        width=width,
        count=1,
        dtype="float32",
        crs="EPSG:4326",
        transform=transform,
    ) as dst:
        dst.write(data, 1)
    print(f"Wrote {ndvi_path}")


if __name__ == "__main__":
    main()
