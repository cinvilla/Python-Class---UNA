def test_division_entera ():
    num1 = 9
    num2 = 3
    mydiv = num1 // num2
    print(mydiv)
    assert 9 == mydiv

def test_division_entera_falla ():
    num3 = 15
    num4 = 5
    mydiv_q5 = num3 // num4
    print(mydiv_q5)
    assert (num4 - 2) == mydiv_q5