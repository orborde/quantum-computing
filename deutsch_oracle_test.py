import numpy as np
from deutsch_oracle import *



def test_tensor_product():
    assert (tensor_product(ZERO, ZERO) == np.mat([[1],[0],[0],[0]])).all()
    assert (tensor_product(ZERO, ONE)  == np.mat([[0],[1],[0],[0]])).all()
    assert (tensor_product(ONE, ZERO)  == np.mat([[0],[0],[1],[0]])).all()
    assert (tensor_product(ONE, ONE)   == np.mat([[0],[0],[0],[1]])).all()
    assert (tensor_product(
        np.mat(
            [
                [0,1],
                [1,0],
            ]
        ),
        np.mat(
            [
                [1,1],
                [1,1],
            ]
        )) == np.mat([
        [0,0,1,1],
        [0,0,1,1],
        [1,1,0,0],
        [1,1,0,0],
    ])).all()

def test_deutsch():
    # assert deutsch_oracle(NOT) == np.mat([[1],[0],[0],[0]])
    for op in OPS:
        print(deutsch_oracle(op))

test_deutsch()