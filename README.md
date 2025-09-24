# Crop Rotation GIS

Учебный проект для демонстрации использования **ГИС** (геоинформационных систем)  
в задаче планирования севооборота.  

Программа загружает данные о полях из GeoJSON/Shape файлов, анализирует культуры и урожайность,  
и строит базовые графики для визуализации.

---

## Постановка задачи

- Использовать ГИС для визуализации и планирования стратегий севооборота.
- Собрать данные о текущих посевах.
- Использовать Python и библиотеки GIS для анализа.
- Построить графики урожайности и распределения культур.

---

## Стек технологий

- Python 3.12
- GeoPandas
- Pandas
- Matplotlib
- Rasterio (для работы с растровыми данными)

---

## Установка и запуск

### 1. Клонируй проект
```bash
git clone <https://github.com/limonORG02/crop-rotation-gis.git>
cd crop-rotation-gis
```

### 2. Создай виртуальное окружение
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установи зависимости
```bash
pip install -r requirements.txt
```

### 4. Запусти анализ данных
```bash
python -m src.main analyze data/sample_fields.geojson
```

---

## Структура проекта

```text
crop-rotation-gis/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   ├── sample_fields.geojson   # пример данных
│   └── .gitkeep                # чтобы папка осталась в git
│
└── src/
    ├── __init__.py
    └── main.py                 # основной скрипт анализа
```

---


## Пример использования

```bash
(.venv) ➜  crop-rotation-gis git:(develop) ✗ python -m src.main analyze data/sample_fields.geojson
Всего полей: 12
Доступные колонки: ['id', 'crop_type', 'area_ha', 'yield_t_ha', 'geometry']

Культуры и количество полей:
crop_type
fallow     4
corn       3
wheat      3
soybean    2

Средняя урожайность по культурам (т/га):
crop_type
corn       2.56
fallow     2.54
soybean    2.40
wheat      2.08
```

---

## Лицензия
Учебный проект. Свободно для использования в образовательных целях.
