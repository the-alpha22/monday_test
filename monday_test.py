biscuits = int(input("how many biscuits are present please:"))
if biscuits ==3:
    print("still full")
elif 0<biscuits<3:
    print("partly eaten")
elif biscuits == 0:
    print("totally eaten")
else:
    print("not applicable")