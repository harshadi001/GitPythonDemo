# Any pytest file should start with test_ or end with _test
# pytest method name should start with test
# Any code should be wrapped in method only
#py.test -m sanity -v -s  (grouping by any keyword like -sanity here )
#@pytest.mark.xfail -- it is used when its failing testcase but dont want in report - but it should be excuted for further steps
# data driven and parametrization can be done in Tuple format.
import pytest


def test_first():
    print("Hello Python")

@pytest.mark.sanity

def test_secondcredit():
    print("Hello Python learning world")

def test_crossbrowser(crossbrowsertest):
    print(crossbrowsertest)
