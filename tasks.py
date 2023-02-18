import re
from typing import *
import pytest


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]


@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([36.50], [309.65000,97.70000]),
        ([122.11], [395.26000,251.79800]),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().convertTemperature
    result = test_obj_link(*params)
    assert result == EXPECTED
