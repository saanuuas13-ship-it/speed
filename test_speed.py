from speed import calculate_speed

def test_normal_speed():
    assert calculate_speed(100, 2) == 50

def test_another_speed():
    assert calculate_speed(200, 4) == 50

def test_zero_time():
    assert calculate_speed(100, 0) == "Invalid time"

def test_decimal_speed():
    assert calculate_speed(50, 2) == 25