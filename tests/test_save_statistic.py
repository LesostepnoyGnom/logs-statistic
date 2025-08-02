import pytest
import main
import json
import os


def test_save_statistic_creates_file(temp_file, sample_stat):
    """Проверяет создание файла"""
    main.save_statistic(sample_stat, temp_file)
    assert os.path.exists(temp_file)


def test_save_statistic_content(temp_file, sample_stat):
    """Проверяет содержимое файла"""
    main.save_statistic(sample_stat, temp_file)

    with open(temp_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        assert line.rstrip() == str(sample_stat[i])


def test_save_statistic_empty_list(temp_file):
    """Проверяет запись пустого списка"""
    main.save_statistic([], temp_file)

    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()

    assert content == ""
