import hangman

def test_valid_words():
    assert hangman.get_valid_words('someword') == 'SOMEWORD'

def test_word_list():
    assert hangman.word_list['A----'] == 'A - - - -'
