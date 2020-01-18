###############################
# QUANTUM GATES

def HL(state):
    a,b,c,d = state
    return (a+c, b+d, a-c, b-d)

def HR(state):
    a,b,c,d = state
    return (a+b, a-b, c+d, c-d)

# ensure we didn't goof up commutability
assert HL(HR((1,2,3,4))) == HR(HL((1,2,3,4)))

def flip00(state):
    a,b,c,d = state
    return (-a, b, c, d)


##############################
# GROVER'S ALGORITHM

def pipe(state, *fs):
    result = state
    for f in fs:
        result = f(result)
    return result

def grover(state, oracle):
    return pipe(state, oracle, HL, HR, flip00, HL, HR)




def oracle(state):
    a,b,c,d = state
    return (a, b, -c, d)

print(grover((1,1,1,1), oracle))
