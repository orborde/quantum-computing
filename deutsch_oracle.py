import numpy as np

ZERO = np.mat([[1],[0]])
ONE  = np.mat([[0],[1]])

def tensor_product(a, b):

    rows = a.shape[0]
    cols = a.shape[1]

    out = []
    for ri in range(rows):
        nrow = []
        for ci in range(cols):
            nrow.append(a[ri,ci] * b)
        out.append(np.concatenate(nrow, axis=1))
    return np.concatenate(out)

HADAMARD = 1/np.sqrt(2) * np.mat([[1,1],[1,-1]])
# HADAMARD = np.mat([[1,1],[1,-1]])

NOT = np.mat(
    [
        [0,1,0,0],
        [1,0,0,0],
        [0,0,1,0],
        [0,0,0,1],
    ]
)

IDENTITY = np.mat([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
])

ALWAYS_ONE = np.mat([
    [0,0,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,1,1],
])

OPS=[NOT, IDENTITY, ALWAYS_ONE]

def deutsch_oracle(op):
    inp = HADAMARD * ZERO
    out = HADAMARD * ZERO

    pre_op = tensor_product(inp, out)
    post_op = op * pre_op
    
    post_hadamard_transform = tensor_product(HADAMARD, HADAMARD)
    return post_hadamard_transform * post_op
