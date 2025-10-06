import pytest

#Conftest file to generalize - and same methods can be used in different files. - test_fixture1 --mentioned in method
#C:\Users\harsh\PycharmProjects\PythonTest\pytestDemo>py.test --html=report.html  -- to generate html report command
@pytest.fixture()
def test_fixture1():
    print("first i will be executed")
    yield
    print("last execution")

@pytest.fixture()
def datafixture2():
    print("User profile data creation")
    return["Harsh", "Aditya", "hadi@gmail.com"]   #Tuple


#parametrization -- Run test with multiple data sets
#@pytest.fixture(params=[("chrome","Rahul), "Firefox", "IE"]) -- parametrizing multiple values
@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossbrowsertest(request):
    return request.param