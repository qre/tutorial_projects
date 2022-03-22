import madlib

def test_madlib():
    if madlib.adj == 'cool' and madlib.verb1 == 'VERB!' and madlib.verb2 == 'vErB2' and madlib.person == 'me':
        assert madlib.madlib == 'Python is so cool! It is exciting too because i love to VERB!. Anyway,\
stay safe and vErB2 like you are me'
