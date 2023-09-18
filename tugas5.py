A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}
print(A^B)
print(B^A)
# print(A^C)
# print(B^C)
print(A.symmetric_difference(C))
print(B.symmetric_difference(C))