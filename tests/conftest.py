import pytest


@pytest.fixture
def sample_log_file(tmp_path):
    log_content = (
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context", "response_time": 0.024}\n'
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/users", "response_time": 0.02}\n'
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/users", "response_time": 0.024}\n'
    )
    log_file = tmp_path / "sample.log"

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(log_content)

    return log_file


@pytest.fixture
def second_sample_log_file(tmp_path):
    log_content = (
        '{"@timestamp": "2025-06-22T13:57:41+00:00", "status": 200, "url": "/api/homeworks/...", "request_method": "GET", "response_time": 0.12, "http_user_agent": "..."}\n'
        '{"@timestamp": "2025-06-22T13:57:41+00:00", "status": 200, "url": "/api/homeworks/...", "request_method": "GET", "response_time": 0.136, "http_user_agent": "..."}\n'
        '{"@timestamp": "2025-06-22T13:57:41+00:00", "status": 200, "url": "/api/homeworks/...", "request_method": "GET", "response_time": 0.3, "http_user_agent": "..."}\n'
        '{"@timestamp": "2025-06-22T13:57:41+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.036, "http_user_agent": "..."}\n'
        '{"@timestamp": "2025-06-22T13:57:42+00:00", "status": 200, "url": "/api/homeworks/...", "request_method": "GET", "response_time": 0.112, "http_user_agent": "..."}\n'
    )
    log_file = tmp_path / "sample2.log"

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(log_content)

    return log_file


@pytest.fixture
def empty_log_file(tmp_path):

    log_content = ""

    log_file = tmp_path / "empty.log"

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(log_content)

    return log_file


@pytest.fixture
def sample_stat():
    stat_content = [
        {'handler': '/api/homeworks/...', 'total': 71, 'avg_response_time': 0.158},
        {'handler': '/api/context/...', 'total': 21, 'avg_response_time': 0.043},
        {'handler': '/api/specializations/...', 'total': 6, 'avg_response_time': 0.035},
        {'handler': '/api/users/...', 'total': 1, 'avg_response_time': 0.072},
        {'handler': '/api/challenges/...', 'total': 1, 'avg_response_time': 0.056}
    ]

    return stat_content


@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_stats.txt"


@pytest.fixture
def sample_logs():
    return [
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/homeworks/...", "request_method": "GET", "response_time": 0.076, "http_user_agent": "..."}',
        '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.024, "http_user_agent": "..."}',
        '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200, "url": "/api/specializations/...", "request_method": "GET", "response_time": 0.016, "http_user_agent": "..."}',
        '{"@timestamp": "2025-07-22T13:57:34+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.032, "http_user_agent": "..."}',
        '{"@timestamp": "2025-08-22T13:57:34+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.072, "http_user_agent": "..."}',
        '{"@timestamp": "2025-08-22T13:57:34+00:00", "status": 200, "url": "/api/specializations/...", "request_method": "GET", "response_time": 0.016, "http_user_agent": "..."}'
    ]

