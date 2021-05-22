# imports pytest functionality
import pytest
# imports leapyear program
import leapyear # type: ignore


def test1():
    year = 2020
    assert leapyear.checkyear(year) == True

def test2():
    year = 2011
    assert leapyear.checkyear(year) == False

def test3():
    year = 2000
    assert leapyear.checkyear(year) == True


if __name__ == "__main__":
    pytest.main()