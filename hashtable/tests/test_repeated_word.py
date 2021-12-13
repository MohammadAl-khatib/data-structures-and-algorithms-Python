from hashtable.hashtable import Hashtable, repeated_word

def test_repeated_word():
    expected = 'a'
    actual = repeated_word("Once upon a time, there was a brave princess who...")
    assert expected ==  actual

def test_repeated_word2():
    expected = 'it'
    actual = repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    assert expected ==  actual


def test_repeated_word3():
    expected = 'summer'
    actual = repeated_word( "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    assert expected ==  actual

def test_repeated_word_empty():
    expected = 'No repeated word'
    actual = repeated_word('')
    assert expected ==  actual

def test_first_and_last():
    expected = 'hello'
    actual = repeated_word('hello my name is Mohammad, again, hello')
    assert expected ==  actual

def test_multiple_repeated_words():
    expected = 'as'
    actual = repeated_word('as long as it goes, it must continue')
    assert expected ==  actual
   