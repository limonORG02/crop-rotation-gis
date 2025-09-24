"""
Алгоритмы проверки и предложения севооборота.
"""
from typing import List




def check_no_three_years_same(history: List[str]) -> bool:
"""Возвращает False, если та же культура посевалась 3 года подряд или более."""
if len(history) < 3:
return True
for i in range(2, len(history)):
if history[i] == history[i-1] == history[i-2]:
return False
return True




ROTATION_RULES = {
'wheat': 'soybean',
'soybean': 'corn',
'corn': 'wheat',
'sunflower': 'fallow',
'fallow': 'wheat'
}




def suggest_next_crop(history: List[str]) -> str:
"""Простейший советник: возвращает следующую культуру по правилу ROTATION_RULES, если есть история.
Если истории нет — выбирает наиболее подходящую (в данном примере — 'wheat').
"""
if not history:
return 'wheat'
last = history[-1]
return ROTATION_RULES.get(last, 'wheat')




def plan_rotation_for_gdf(gdf):
"""Добавляет колонку 'suggested_next' с предложенной культурой для каждого поля."""
gdf = gdf.copy()
gdf['suggested_next'] = gdf['history'].apply(suggest_next_crop)
gdf['rotation_ok'] = gdf['history'].apply(check_no_three_years_same)
return gdf
