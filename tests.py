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


def test_fizzbuzz_count_to_fifteen():
    result = fizzbuzz(15)
    assert (
        result == '1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n'
    )


def test_fizzbuzz_count_to_5_with_another_words():
    result = fizzbuzz(5, fizz='ogorek', buzz='ziemniak')
    assert result == '1\n2\nogorek\n4\nziemniak\n'


def test_fizzbuzz_count_to_15_with_another_words():
    result = fizzbuzz(15, fizz='ogorek', buzz='ziemniak')
    assert (
        result == '1\n2\nogorek\n4\nziemniak\nogorek\n7\n8\nogorek\nziemniak\n11\nogorek\n13\n14\nogorekziemniak\n'
    )

