def test_a1():
    assert 5<6

def test_a2():
    assert "Siva" == 'Siva'

def test_a3():
    assert ((5*9)%2) == 1

def test_a4():
    assert 1 in divmod(9,5)

def test_a5():
    assert 3 in divmod(7,2)
    assert "put" in "putup"
    assert "Siva" not in "SivKumari"
    assert 2 in [1,2,4]
    assert [1,2,4] < [1,2,5]

