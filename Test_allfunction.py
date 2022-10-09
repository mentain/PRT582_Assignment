import function1
import function2
import function3
import pytest
import mock
import builtins
from function1 import computer_random_selection
from function1 import selection_list
from function2 import player_action_selection
from function3 import who_win
from function4 import is_get_enough_point

##PLEASE DISABLE OTHER TEST CASES OF OTHER REQUIREMENTS IF YOU WANT TO TEST ANY SPECIFIC REQUIREMENT.
# Test cases

# 1st Requirement
def test_case1():
    ss = computer_random_selection("computer_action")
    print(f"test_case1 result: {ss}")
    assert ss in selection_list

def test_case2():
    ss = computer_random_selection("computer_action")
    print(f"test_case1 result: {ss}")
    assert ss in selection_list

def test_case3():
    ss = computer_random_selection("computer_action")
    print(f"test_case1 result: {ss}")
    assert ss in selection_list

# 2nd Requirement
def test_case4():
    with mock.patch.object(builtins, 'input', lambda _: 'Rock'):
        assert player_action_selection() == 'Rock'


def test_case5():
    with mock.patch.object(builtins, 'input', lambda _: 'Paper'):
        assert player_action_selection() == 'Paper'


def test_case6():
    with mock.patch.object(builtins, 'input', lambda _: 'Scissors'):
        assert player_action_selection() == 'Scissors'
    
# 3rd requirement
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

#4th requirement
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