import numpy as np

class Perceptron:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.w = (np.random.random(size=(self.n+1,self.m)) / 10 + .45) - .5

    def test(self, vec):
        vec = np.append(vec, 1)
        o = np.dot(vec, self.w) > 0
        return o

    def train(self, p, t):
        # p is input pattern
        # t is target pattern
        

    def __str__(self):
        p = "A perceptron with " + str(self.n) +  " inputs and " + str(self.m) + " outputs."
        return p

pcp = Perceptron(2,10)
vec1 = np.zeros(2)
vec2 = np.ones(2)
print(pcp.test(vec1))
print(pcp.test(vec2))
print(pcp)


