import pytest
import main


def test_open_log_file(sample_log_file):
    logs = main.open_log([sample_log_file])
    assert len(logs) == 3
    assert '{"@timestamp": "2025-06-22T13:57:32+00:00"' in logs[0]


def test_open_log_multiple_files(sample_log_file, second_sample_log_file):
    logs = main.open_log([sample_log_file, second_sample_log_file])
    assert len(logs) == 8


def test_open_log_empty_file(empty_log_file):
    logs = main.open_log([empty_log_file])
    assert len(logs) == 0