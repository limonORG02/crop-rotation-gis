from src.rotation_planner import check_no_three_years_same, suggest_next_crop




def test_check_ok():
assert check_no_three_years_same(['wheat', 'corn', 'wheat'])




def test_check_not_ok():
assert not check_no_three_years_same(['wheat', 'wheat', 'wheat'])




def test_suggest():
assert suggest_next_crop(['wheat']) == 'soybean'
assert suggest_next_crop([]) == 'wheat'

