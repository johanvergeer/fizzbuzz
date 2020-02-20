from fizbuzz import fizzbuzz


def test_fizzbuzz__1():
    assert fizzbuzz(1) == "1"


def test_fizzbuzz__2():
    assert fizzbuzz(2) == "2"


def test_fizzbuzz__3():
    assert fizzbuzz(3) == "Fizz"


def test_fizzbuzz__4():
    assert fizzbuzz(4) == "4"


def test_fizzbuzz__5():
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz__6():
    assert fizzbuzz(6) == "Fizz"


def test_fizzbuzz__7():
    assert fizzbuzz(7) == "7"


def test_fizzbuzz__10():
    assert fizzbuzz(10) == "Buzz"


def test_fizzbuzz_12():
    assert fizzbuzz(12) == "Fizz"


def test_fizzbuzz_15():
    assert fizzbuzz(15) == "Fizz Buzz"


def test_fizzbuzz__18():
    assert fizzbuzz(18) == "Fizz"


def test_fizzbuzz__20():
    assert fizzbuzz(20) == "Buzz"
