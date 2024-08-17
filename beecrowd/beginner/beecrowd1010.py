productOne = str(input()).split()
productTwo = str(input()).split()
a, b, c = productOne
x, y, z = productTwo
total_value = (int(b) * float(c) + (int(y) * float(z)))
print("VALOR A PAGAR: R$ %.2f" % total_value)
