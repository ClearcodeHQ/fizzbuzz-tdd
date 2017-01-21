from fizzbuzz import fizzbuzz


def test_fizzbuzz_count_to_two():
    result = fizzbuzz(2)
    assert result == '1\n2\n'


def test_fizzbuzz_count_to_three():
    result = fizzbuzz(3)
    assert result == '1\n2\nfizz\n'


def test_fizzbuzz_count_to_five():
    result = fizzbuzz(5)
    assert result == '1\n2\nfizz\n4\nbuzz\n'

