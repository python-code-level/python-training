# examples from tests

#throws errro because in is a reserved keyword!!
#def fun(in=2,out=3):
#    return in * out
#print(fun())



def fun(inward=2, outward=3):
    return inward * outward


print(fun())
print(fun(1,1))
print(fun(3))
