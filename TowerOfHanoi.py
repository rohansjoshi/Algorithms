

class Hanoi:

    def __init__(self, n) -> None:
        self.n = n
        self.src = list(range(n, 0, -1))
        self.aux = []
        self.dst = []
        self.towers = [self.src, self.aux, self.dst]
    
    def move(self, i, j):
        """ Move block from tower i to tower j, if valid.
        Else do nothing. i, j in [0, 1, 2] """
        if len(self.towers[i]) > 0:
            if len(self.towers[j]) == 0 or self.towers[i][-1] < self.towers[j][-1]:
                self.towers[j].append(self.towers[i].pop(-1))
    
    def isComplete(self):
        if not (len(self.src) == 0 and len(self.aux) == 0):
            return False
        for i in range(1, self.n+1):
            if self.dst[-i] != i:
                return False
        return True


other = lambda x, y: 3-x-y
n = 10
hanoi = Hanoi(n)
def solve(hanoi, k, i, j):
    """ Assuming that we have a tower of size at least k on towers[i], 
    move the top k blocks to tower[j], validly """
    if k == 1:
        hanoi.move(i, j)
    else:
        solve(hanoi, k-1, i, other(i, j))
        hanoi.move(i, j)
        solve(hanoi, k-1, other(i, j), j)

print(hanoi)