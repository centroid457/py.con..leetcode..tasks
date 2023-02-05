import re
from typing import *
import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "abcdefghijklmnopqrstuvwxyz0123456789"

        finish_index = len(s) -1

        for start_index, start_value in enumerate(s):
            # get correct start
            start_value = start_value.lower()
            if start_value not in valid:
                continue

            # get correct finish
            finish_value = s[finish_index].lower()
            while start_index < finish_index and finish_value not in valid:
                finish_index -= 1
                finish_value = s[finish_index].lower()

            if start_index >= finish_index:
                return True

            if start_value != finish_value:
                return False
            else:
                finish_index -= 1
        return True



@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        # (["123"], False),
        # (["121"], True),
        # (["111"], True),
        # (["11"], True),
        # (["1"], True),
        (["A man, a plan, a canal: Panama"], True),


    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().isPalindrome
    result = test_obj_link(*params)
    assert result == EXPECTED

