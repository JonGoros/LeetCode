from typing import List, Optional
from type_annotations import *
from check import check_solution

###################### START THE CODE HERE ######################


class Solution:

    def solution(self, input: List[str]) -> int:

        return 0
    
    
########################## TEST CASES ###########################

output_function = None

test_cases = [
    {
        "input": (0,),
        "output": 0,
    },
    {
        "input": (1,),
        "output": 1,
    },
    {
        "input": (2,),
        "output": 2,
    },
]

####################### END THE CODE HERE #######################

check_solution(Solution(), test_cases, output_function)