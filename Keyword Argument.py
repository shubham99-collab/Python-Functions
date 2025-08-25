#Keyword Argument
def KeyArg(a_int, a_float, a_str):
    print("int :",a_int)
    print("float :",a_float)
    print("String :",a_str)
    print("Call1")
    KeyArg(a_int=6, a_float=2.9, a_str="M")
    print("Call2")
    KeyArg(a_float=5.3, a_int=74, a_str="j")
    print("Call3")
    KeyArg(a_str="c", a_float=4.9, a_int=4)