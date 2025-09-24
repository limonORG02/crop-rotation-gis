# src/main.py
"""
Основной CLI для анализа и визуализации данных севооборота.
"""

import argparse
import geopandas as gpd
import matplotlib.pyplot as plt


def analyze(fields_path: str) -> None:
    """Простейший анализ полей: вывод статистики по культурам и урожайности."""
    gdf = gpd.read_file(fields_path)
    print("Всего полей:", len(gdf))
    print("Доступные колонки:", list(gdf.columns))

    if "crop_type" in gdf.columns:
        print("\nКультуры и количество полей:")
        print(gdf["crop_type"].value_counts())

        if "yield_t_ha" in gdf.columns:
            print("\nСредняя урожайность по культурам (т/га):")
            print(gdf.groupby("crop_type")["yield_t_ha"].mean())
    else:
        print("⚠️ В данных нет информации о культурах.")


def plot(fields_path: str, out_path: str) -> None:
    """Визуализация полей и культур."""
    gdf = gpd.read_file(fields_path)
    ax = gdf.plot(column="crop_type", legend=True, figsize=(8, 6))
    plt.title("Карта посевов")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Карта сохранена в {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Crop Rotation GIS CLI")
    subparsers = parser.add_subparsers(dest="command")

    # analyze
    analyze_parser = subparsers.add_parser("analyze", help="Анализ данных о полях")
    analyze_parser.add_argument("fields", help="Путь к GeoJSON с полями")

    # plot
    plot_parser = subparsers.add_parser("plot", help="Построить карту полей")
    plot_parser.add_argument("fields", help="Путь к GeoJSON с полями")
    plot_parser.add_argument("--out", required=True, help="Путь для сохранения PNG")

    args = parser.parse_args()

    if args.command == "analyze":
        analyze(args.fields)
    elif args.command == "plot":
        plot(args.fields, args.out)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
