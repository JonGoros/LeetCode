from typing import List, Optional
from type_annotations import *
from check import check_solution

###################### START THE CODE HERE ######################


class Solution:

    def solution(self, input: Optional[ListNode]) -> Optional[ListNode]:
    
        return ListNode()

    
########################## TEST CASES ###########################

output_function = ListNode2Array

test_cases = [
    {
        "input": (Array2ListNode([0]),),
        "output": [0],
    },
    {
        "input": (Array2ListNode([1]),),
        "output": [1],
    },
    {
        "input": (Array2ListNode([2]),),
        "output": [2],
    },
]

####################### END THE CODE HERE #######################

check_solution(Solution(), test_cases, output_function)