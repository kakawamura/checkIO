OPERATION_NAME = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
def boolean(x, y, operation):
    #x and y
    if operation == OPERATION_NAME[0]:
        return x and y
    #x or y
    elif operation == OPERATION_NAME[1]:
        return x or y
    #x => y
    elif operation == OPERATION_NAME[2]:
        return not(x) or y
    #x xor y
    elif operation == OPERATION_NAME[3]:
        return 1 if     (not(x) and y) or (x and not(y)) else 0
    elif operation == OPERATION_NAME[4]:
        return 1 if x==y else 0
        
    return 1
x = 0
y = 0
operation = "exclusive"
print boolean(x, y, operation)
