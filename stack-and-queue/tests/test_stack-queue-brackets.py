from stack_and_queue.stack_queue_brackets import validate_brackets

def test_brackets1():
    expected = True
    actual = validate_brackets('{}')
    assert expected == actual

def test_brackets2():
    expected = True
    actual = validate_brackets("{}(){}")
    assert expected == actual

def test_brackets3():
    expected = True
    actual = validate_brackets("()[[Extra Characters]]")
    assert expected == actual

def test_brackets4():
    expected = True
    actual = validate_brackets("(){}[[]]")
    assert expected == actual

def test_brackets5():
    expected = True
    actual = validate_brackets("{}{Code}[Fellows](())")
    assert expected == actual

def test_brackets6():
    expected = False
    actual = validate_brackets("[({}]")
    assert expected == actual

def test_bracket7():
    expected = False
    actual = validate_brackets("(](")
    assert expected == actual

def test_brackets8():
    expected = False
    actual = validate_brackets("{(})")
    assert expected == actual

def test_empty_input():
    expected = 'invalid input'
    actual = validate_brackets('')
    assert expected == actual