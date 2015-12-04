import numpy as np


def updateweights(eta, Win, Wout, inword, outwords):

    V = np.size(Win, 0)
    C = len(outwords)

    h = Win[inword]
    h = h.T

    softmax = 0
    for j in range(V):
        softmax += np.exp(np.dot(Wout[:, j].T, h))

    gradin = 0
    for j in range(V):
        gradout = 0
        for c in range(C):
            gradout += np.exp(np.dot(Wout[:, j].T, h))/softmax - 1

        Wout[:, j] -= eta*gradout*h
        gradin += gradout*Wout[:, j]

    Win[inword] -= eta*gradin

    return Win, Wout


def updateweights_negative(eta, Win, Wout, inword, outwords):

    V = np.size(Win, 0)
    C = len(outwords)

    h = Win[inword]
    h = h.T
    softmax = 0
    for j in range(V):
        softmax += np.exp(np.dot(Wout[:, j].T, h))

    gradin = 0
    for j in range(V):
        gradout = 0
        for c in range(C):
            gradout += np.exp(np.dot(Wout[:, j].T, h))/softmax - 1

        Wout[:, j] -= eta*gradout*h
        gradin += gradout*Wout[:, j]

    Win[inword] -= eta*gradin

    return Win, Wout