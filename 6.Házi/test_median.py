from median import median_value


def test_median_value():
    assert median_value([0,1,2,3,4]) == 2
    assert median_value([0,1,2,3,4,5]) == 2.5
    assert median_value([1,1,1,1,4]) == 1
    assert median_value([100,10,20,300,4.4]) == 20
    assert median_value([0.1,100,200,30000,400000,0.5]) == 150
    assert median_value((1,2,3)) == 2
    assert median_value((3,1,2,1)) == 1.5