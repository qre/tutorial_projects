import rock_paper_scissors

def test_is_win_working():
    assert rock_paper_scissors.is_win('s', 'p') == True
    assert rock_paper_scissors.is_win('r', 's') == True
    assert rock_paper_scissors.is_win('r', 'p') == None