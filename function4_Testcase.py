import pytest
from function4 import is_get_enough_point


# testcase
def test_case13():
    ss = is_get_enough_point(5, 5)
    print(f"test_case13 result: {ss}")
    assert ss == True


def test_case14():
    ss = is_get_enough_point(3, 5)
    print(f"test_case14 result: {ss}")
    assert ss == False


def test_case15():
    ss = is_get_enough_point(5, 5)
    print(f"test_case15 result: {ss}")
    assert ss == True


def test_case16():
    ss = is_get_enough_point(2, 5)
    print(f"test_case16 result: {ss}")
    assert ss == False
