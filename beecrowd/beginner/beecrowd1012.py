PI = 3.14159
value = str(input()).split()
A, B, C = value

triangle_rectangle = (float(A) * float(C)) / 2.0
area_circle = PI * (float(C) ** 2)
area_trapezium = ((float(A) + float(B)) * float(C)) / 2.0
area_square = (float(B) * float(B))
area_rectangle = (float(A) * float(B))

print("TRIANGULO: %.3f" % triangle_rectangle)
print("CIRCULO: %.3f" % area_circle)
print("TRAPEZIO: %.3f" % area_trapezium)
print("QUADRADO: %.3f" % area_square)
print("RETANGULO: %.3f" % area_rectangle)
