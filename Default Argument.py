#Default Argument
def DefArg(num=7, str="Good"):
    print(num)
    print(str)
    print("Call1")
    DefArg()
    print("Call2")
    DefArg(9)
    print("Call3")
    DefArg(9, "Nice")