value = str(input()).split()
A, B, C, D = value
int_a = int(A)
int_b = int(B)
int_c = int(C)
int_d = int(D)

if int_b > int_c and int_d > int_a and (
        (int_c + int_d) > (int_a + int_b)) and int_c > 0 and int_d > 0 and int_a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
