from sum_of_digit import digit_sum


def test_digit_sum():
    assert digit_sum(1234) == 10
    assert digit_sum(1) == 1
    assert digit_sum(100000) == 1
    assert digit_sum(0) == 0