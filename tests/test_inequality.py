import numpy as np
from ineqpy import inequality


def test_gini_2d():
    x = np.array([[57], [63], [81], [79], [88], [57], [42], [3], [77], [89]])
    w = np.array([[2], [5], [2], [9], [5], [7], [4], [5], [9], [9]])
    obtained = inequality.gini(income=x, weights=w)
    expected = 0.2134389018024818
    assert obtained==expected


def test_gini_1d():
    x = np.array([57, 63, 81, 79, 88, 57, 42, 3, 77, 89])
    w = np.array([2, 5, 2, 9, 5, 7, 4, 5, 9, 9])
    obtained = inequality.gini(income=x, weights=w)
    expected = 0.2134389018024818
    assert obtained==expected


def test_gini_1d_0_w():
    x = np.array([2,       2])
    w = np.array([1000000, 1])
    obtained = inequality.gini(income=x, weights=w)
    expected = 0
    assert obtained==expected


def test_gini_1d_0_series():
    x = np.array([2, 2])
    # w = np.array([1000000, 1])
    obtained = inequality.gini(income=x)
    expected = 0
    assert obtained==expected


def test_gini_1d_1_series():
    x = np.array([0, 1])
    # w = np.array([1000000, 1])
    obtained = inequality.gini(income=x)
    expected = 1
    assert obtained==expected


def test_gini_1d_1_w():
    x = np.array([0, 1])
    w = np.array([1, 1])
    obtained = inequality.gini(income=x, weights=w)
    expected = 1
    assert obtained==expected


def test_atkinson_2d():
    x = np.array([[57], [63], [81], [79], [88], [57], [42], [3], [77], [89]])
    w = np.array([[2], [5], [2], [9], [5], [7], [4], [5], [9], [9]])
    obtained = inequality.atkinson(income=x, weights=w)
    expected = 0.06537929778911322
    assert obtained==expected


def test_atkinson_1d():
    x = np.array([57, 63, 81, 79, 88, 57, 42, 3, 77, 89])
    w = np.array([2, 5, 2, 9, 5, 7, 4, 5, 9, 9])
    obtained = inequality.atkinson(income=x, weights=w)
    expected = 0.06537929778911322
    assert obtained==expected


def test_atkinson_1d_1_w():
    x = np.array([1, 1])
    w = np.array([1, 1])
    obtained = inequality.atkinson(income=x, weights=w)
    expected = 0
    assert obtained==expected


def test_theil_1d_1_w():
    # TODO check this
    x = np.array([1, 1])
    w = np.array([1, 1])
    obtained = inequality.theil(income=x, weights=w)
    expected = 0
    assert obtained==expected

def test_ratio_1d():
    x = np.array([57, 63, 81, 79, 88, 57, 42, 3, 77, 89])
    w = np.array([2, 5, 2, 9, 5, 7, 4, 5, 9, 9])
    obtained = inequality.ratio_top_rest(income=x, weights=w)
    expected = 0.2654955253563142
    assert obtained == expected

def test_ratio_2d():
    x = np.array([[57], [63], [81], [79], [88], [57], [42], [3], [77], [89]])
    w = np.array([[2], [5], [2], [9], [5], [7], [4], [5], [9], [9]])
    obtained = inequality.ratio_top_rest(income=x, weights=w)
    expected = 0.2654955253563142
    assert obtained == expected

def test_ratio_unweighted():
    x = np.array([
       11, 67, 93, 68, 80, 71,  0, 65, 45, 73, 56, 38, 18, 24, 94, 72, 56,
       37, 26, 34, 49, 30, 30, 31, 10,  0, 77,  6, 64, 75, 56, 79, 46, 87,
       39, 73, 63,  3, 49, 52, 94,  0, 68, 86, 42, 84, 58,  5, 45, 62, 49,
       97, 77, 94, 66, 84, 42, 39,  7, 24, 65, 52, 59, 52, 38, 27, 85, 43,
       26,  6, 93, 24, 48, 42, 50, 58, 89, 79, 94, 50,  2, 46, 82, 98, 69,
        9, 50, 33, 86, 77, 25, 39, 61, 78, 47, 29, 43, 20, 56, 35])
    obtained = inequality.ratio_top_rest(x)
    expected = 0.22203712517848642
    assert obtained == expected

def test_ratio_1d_0_w():
    x = np.array([2,       2])
    w = np.array([1000000, 1])
    obtained = inequality.ratio_top_rest(income=x, weights=w)
    expected = 2000000 / 2
    assert obtained == expected


def test_ratio_1d_0_series():
    x = np.array([2, 2])
    # w = np.array([1, 1])
    obtained = inequality.ratio_top_rest(income=x)
    expected = 1
    assert obtained == expected
