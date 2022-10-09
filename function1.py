
import random
import pytest

# 1st Requirement
player_action = ""
selection_list = ("Rock", "Paper", "Scissors")
def computer_random_selection(s):

         computer_action = random.choice(selection_list)
         print(f"\n computer choses {computer_action}.\n")

         return computer_action

# Test cases

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
