

def binarycodes(n):
    all = []
    def helper(n, soFar):
        if len(soFar) == n:
            all.append("".join(soFar))
        else:
            soFar.append('0')
            helper(n, soFar)
            soFar[-1] = '1'
            helper(n, soFar)
            soFar.pop()

    helper(n, [])
    return all