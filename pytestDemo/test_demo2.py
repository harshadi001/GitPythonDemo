# Any pytest file should start with test_ or end with _test
# pytest method name should start with test
# Any code should be wrapped in method only
# Method (function) name should be meaningful - means test case
import pytest


# cd path >py.test , py.test -v -s (detailed) , py.test -k credit -v -s (for specific methods name)
#Run specific file : py.test filename.py -v -s

@pytest.mark.sanity
@pytest.mark.skip
def test_third():
    msg = "Python"
    assert msg == "HiPy" , "doesnt match then test failed"

def test_creditprog():
    a=7
    b=8
    assert a+1 == 8 , "Test data matched and passed"