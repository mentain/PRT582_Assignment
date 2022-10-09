import pytest
from function3 import who_win

def test_case7():
    ss = who_win('Rock', 'Paper')
    assert ss == 2
def test_case8():
    ss = who_win('Paper', 'Rock')
    assert ss == 1
def test_case9():
    ss = who_win('Rock', 'scissors')
    assert ss == 1
def test_case10():
    ss = who_win('scissors', 'Rock')
    assert ss == 2
def test_case11():
    ss = who_win('Paper', 'Scissors')
    assert ss == 2
def test_case12():
    ss = who_win('Scissors', 'Paper')
    assert ss == 1
