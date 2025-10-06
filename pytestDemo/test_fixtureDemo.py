import pytest

# wrap all you testcases under class - to avoid using fixtures again
#whenever declare function- method inside class -self parameter is mandatory

@pytest.mark.usefixtures("test_fixture1")
class Testexmpl:

    def test_fixture002(self):
        print("after test fixture1 i will be executed")

    def test_fixture003(self):
        print("after test fixture1 i will be executed")

    def test_fixture004(self):
        print("after test fixture1 i will be executed")