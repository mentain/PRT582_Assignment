import random

#requirement 4

points_to_win = 5
selection_list = ("Rock", "Paper", "Scissors")


def is_get_enough_point(user_counter, points_to_win):
    if user_counter >= points_to_win:
        return True
    return False
