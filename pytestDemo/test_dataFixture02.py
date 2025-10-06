import pytest

# in case of return data need to pass fixturename -- datafixture2 with self, if declared globally , still need to
# if not returning something then globally declared fixture will work


@pytest.mark.usefixtures("datafixture2")
class Testexmp2:

    def test_editProfile(self, datafixture2):
        #print(datafixture2)
        print(datafixture2[0])