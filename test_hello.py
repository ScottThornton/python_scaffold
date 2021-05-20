from hello import add, hypotenuse

def test_add():
    assert add(1,2) == 3


def test_hypotenuse():
    assert hypotenuse(3,6) == 6.708203932499369