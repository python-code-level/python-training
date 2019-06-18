# revise numbers and types

print(0o100)  # print an octal number
print(0x40)   # print a hexidecmial number
print(0xff)   # print a hexidecimal value
print('-----------------------------------------')
print (oct(64))
print(hex(64))
print(hex(255))
print('-----------------------------------------')
int1 = 4556
oct1 = 0o123
hex1 = 0xff
print('-----------------------------------------')
print(type(int1))
print(type(oct1))
print(type(hex1))
print('-----------------------------------------')
print(type(oct(64)))
print(type(hex(64)))
print(type(hex(255)))
print('-----------------------------------------')

# exponent represented by both E and e
# baseEexponent
# exponent always an integer, base can be float
sci0 = 5E5 # 5x10 to the power 5
sci = 5e5 # 5x10 to the power 5
sci2 = 10e2 # 10*10 to the power 2
sci3 = 10e1 # 10*10 to the power 1
sci4 = 5e1 # 5*10 to the power 1
print(sci0)
print(sci)
print(sci2)
print(sci3)
print(sci4)
# plancks = 6.62607 x 10 -34
planks = 6.62607E-34
print(planks)