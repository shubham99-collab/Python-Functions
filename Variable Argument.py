# Variable Number of Argument
def MultiArg(*argTuple):
    print(argTuple)
    print(argTuple[0])
    print(argTuple[1])
    print(argTuple[2])
    for i in argTuple:
        print(i)
MultiArg(7, 45, "forest")