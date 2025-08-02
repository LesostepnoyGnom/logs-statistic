import main


def test_no_date_filter(sample_logs):
    """без фильтра по дате"""
    result = main.get_stat(sample_logs, None)
    assert len(result) == 3

    api_stat = [item for item in result if item["handler"] == "/api/context/..."][0]
    print(api_stat)
    assert api_stat["total"] == 3
    assert api_stat["avg_response_time"] == round((0.072 + 0.032 + 0.024)/3, 3)


def test_single_date_filter(sample_logs):
    """фильтрация по одной дате"""
    result = main.get_stat(sample_logs, ["2025-06-22"])
    
    assert len(result) == 3
    assert [ item["handler"] for item in result ] == ["/api/homeworks/...", "/api/context/...", "/api/specializations/..."]


def test_date_range_filter(sample_logs):
    """фильтрация по диапазону дат"""
    result = main.get_stat(sample_logs, ["2025-06-22", "2025-07-22"])
    
    assert len(result) == 3
    
    contact_stat = next(item for item in result if item["handler"] == "/api/context/...")
    assert contact_stat["total"] == 2
    assert contact_stat["avg_response_time"] == round((0.024 + 0.032) / 2, 3)


def test_empty_logs():
    """с пустыми входными данными"""
    result = main.get_stat([], None)
    assert result == []