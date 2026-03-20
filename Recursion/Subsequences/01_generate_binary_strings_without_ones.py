from typing import List

def generateString(N: int) -> List[str]:
    # taking a results string to store the results
    results = []

    # making a recursive function to append digits to the string
    def solve(current: str):
        # base case - when the string has reached length n, append it to the results arr
        if len(current) == N:
            results.append(current)
            return
        
        # recursive condition, we can always safely place a 0 in every position
        solve(current + '0')

        # placing 1 only if the string is empty or the last elemnt was not 1
        if not current or current[-1] != '1':
            solve(current + '1')

    # calling the function from an empty string
    solve("")

    return results

    pass
