def nextSmallerElement(arr,n):
    # taking a results array
    result = [-1] * n

    stack = []

    for i in range(n - 1, -1, -1):
        # popping elements greater than the current element as they wont be smaller than elements that come consecutively.
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        # if anything remains, the top of the stack is the next smaller
        if stack:
            result[i] = stack[-1]

        # pushing current element as a candidate for next elements
        stack.append(arr[i])

    return result
