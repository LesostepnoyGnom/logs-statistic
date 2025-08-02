import main
import pytest

@pytest.mark.parametrize(
    "log_file, res",
    [
        (None, False),
        ([], False),
        (["."], False),
        (".", False),
    ]
)


def test_check_log_file(log_file, res):
    assert main.check_log_file(log_file) == res


def test_exist_log_file(sample_log_file):
    assert main.check_log_file([sample_log_file]) == True


def test_open_log_nonexistent_file():
    assert main.check_log_file(["non_existent_file.log"]) == False