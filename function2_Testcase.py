import pytest
import mock
import builtins
from function2 import player_action_selection


# Test cases

def test_case4():
    with mock.patch.object(builtins, 'input', lambda _: 'Rock'):
        assert player_action_selection() == 'Rock'


def test_case5():
    with mock.patch.object(builtins, 'input', lambda _: 'Paper'):
        assert player_action_selection() == 'Paper'


def test_case6():
    with mock.patch.object(builtins, 'input', lambda _: 'Scissors'):
        assert player_action_selection() == 'Scissors'