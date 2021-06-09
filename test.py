def driver(input):
    helper(input, 0, [])

def helper(input, idx, soFar):
    if (idx == len(input)):
        print(soFar)
    else:
        helper(input, idx+1, soFar)
        soFar.append(input[idx])
        helper(input, idx+1, soFar)
        soFar.pop(-1)

driver([1, 3, 5, 7])