import pytest
from src.diff import diff, return_all

@pytest.fixture
def get_test_data1():
    data_source=[{"id":123, "trn_date":20251009, "qty":5,"price":123},
             {"id":124, "trn_date":20251019, "qty":5,"price":123},
             {"id":125, "trn_date":20251029, "qty":5,"price":123},
             {"id":126, "trn_date":20251109, "qty":5,"price":123}
             ]
    return data_source

@pytest.fixture
def get_test_data2():
    data_source=[{"id":123, "trn_date":20251009, "qty":5,"price":123},
             {"id":124, "trn_date":20251019, "qty":5,"price":123},
             {"id":125, "trn_date":20251029, "qty":5,"price":123},
             {"id":127, "trn_date":20251109, "qty":5,"price":123}
             ]
    return data_source

@pytest.fixture
def get_diff_result1():
    data_source=[ {"id":126, "trn_date":20251109, "qty":5,"price":123}]
    return data_source

@pytest.fixture
def get_diff_result2():
    data_source=[{"id":127, "trn_date":20251109, "qty":5,"price":123}]
    return data_source

def test_diff1(get_test_data1, get_test_data2):
    print(f"result========={get_diff_result1}")
    assert diff(get_test_data1,get_test_data2)==get_diff_result1

def test_diff2(get_test_data2, get_test_data1):
    assert diff(get_test_data1,get_test_data2)==get_diff_result2

def test_match(get_test_data1, get_test_data2):
    assert return_all(get_test_data1,get_test_data2)==(get_test_data1+get_test_data2)







