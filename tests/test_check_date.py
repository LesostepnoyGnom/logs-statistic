import main
import pytest


@pytest.mark.parametrize(
    "date, res",
    [
        (None, True),
        (["1242-04-05"], True),
        (["1242.04.05"], False),
        (["1242.04"], False),
        (["793-06-08", "1066-09-25"], True),
        (["1066-09-25", "793-06-08"], False),
        (["1066-09-25", "793-06-08", "2077-01-01"], False),
        (["6-01-21"], True),
        (["2020-02-29"], True),
        (["0001-01-01", "9999-12-31"], True),
        (["вставить текст"], False),
        (["вставить текст", "aboba"], False),
        (["вставить текст", "aboba", "ъ"], False),
        (["вставить текст", "aboba", ""], False),
        ([""], False),
        ([None, None], False),
        ([None], False),
        ("None", False),
        ([None, None], False),
        ([2], False),
        (["793-06-08", 5], False),
        (["793-06-08", ''], False),
        ([], True)
    ]
)


def test_check_date(date, res):
    assert main.check_date(date) == res
