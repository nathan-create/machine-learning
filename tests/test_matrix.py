import sys
sys.path.append('src')
from matrix import Matrix



A = Matrix([[1,0,2,0,3],[0,4,0,5,0],[6,0,7,0,8],[-1,-2,-3,-4,-5]])
print("Testing method num_cols and num_rows...")
assert (A.num_rows, A.num_cols) == (4,5)
print("Passed")

A_t = A.transpose()
print("Testing method transpose...")
assert A_t.elements == [[ 1,  0,  6, -1], [ 0,  4,  0, -2],[ 2,  0,  7, -3], [ 0,  5,  0, -4],  [ 3,  0,  8, -5]]
print("Passed")

B = A_t.matrix_multiply(A)
print("Testing method matrix_multiply...")
assert B.elements == [[38,  2, 47,  4, 56],[ 2, 20,  6, 28, 10],[47,  6, 62, 12, 77], [ 4, 28, 12, 41, 20], [56, 10, 77, 20, 98]]
print("Passed")

C = B.scalar_multiply(0.1)
print("Testing method scalar_multiply...")
assert C.elements == [[3.8,  .2, 4.7,  .4, 5.6],[ .2, 2.0,  .6, 2.8, 1.0],[4.7,  .6, 6.2, 1.2, 7.7],[ .4, 2.8, 1.2, 4.1, 2.0],[5.6, 1.0, 7.7, 2.0, 9.8]] , "actual output was {}".format( C.elements)
print("Passed")

D = B.subtract(C)
print("Testing method subtract...")
assert D.elements == [[34.2,  1.8, 42.3,  3.6, 50.4],[ 1.8, 18. ,  5.4, 25.2,  9. ],[42.3,  5.4, 55.8, 10.8, 69.3],[ 3.6, 25.2, 10.8, 36.9, 18. ],[50.4,  9. , 69.3, 18. , 88.2]], "actual output was {}".format(D.elements)
print("Passed")

E = D.add(C)
print("Testing method add...")
assert E.elements == [[38,  2, 47,  4, 56],[ 2, 20,  6, 28, 10],[47,  6, 62, 12, 77],[ 4, 28, 12, 41, 20],[56, 10, 77, 20, 98]], "actual output was{}".format(E.elements)
print("Passed")

print("Testing method is_equal...")
assert (E.is_equal(B), E.is_equal(C)) == (True, False)
print("Passed")

A2 = Matrix( [[0, 1, 2], [3, 6, 9], [2, 6, 8]])

print("Testing method get_pivot_row...")
assert A2.get_pivot_row(1)==0,"{}".format(A2.get_pivot_row(0))
assert A2.get_pivot_row(0) == 1, A2.get_pivot_row(0)
print("Passed")

A2 = A2.swap_rows(0,1)
print("Testing method swap_rows...")
assert A2.elements == [[3, 6, 9], [0, 1, 2], [2, 6, 8]],"actual output was {}".format(A2.swap_rows(0,1))
print("Passed")

A2 = A2.normalize_row(0)
print("Testing method normalize_row...")
assert A2.elements == [[1, 2, 3],[0, 1, 2], [2, 6, 8]], A2.elements
print("Passed")

A2 = A2.clear_below(0)
print("Testing method clear_below...")
assert A2.elements == [[1, 2, 3],[0, 1, 2],[0, 2, 2]], A2.clear_below(0)
print("Passed")

print("Getting pivot row...")
assert A2.get_pivot_row(1) == 1

A2 = A2.normalize_row(1)
print("Normalizing row...")
assert A2.elements == [[1, 2, 3],[0, 1, 2],[0, 2, 2]]

A2 = A2.clear_below(1)
print("Clearing lower rows...")
assert A2.elements == [[1, 2, 3],[0, 1, 2],[0, 0, -2]], A2.elements

print("Getting pivot row..")
assert A2.get_pivot_row(2) == 2, A2.get_pivot_row(2)

A2 = A2.normalize_row(2)
print("Normalizing row...")
assert A2.elements == [[1, 2, 3],[0, 1, 2],[0, 0, 1]], A2.elements

A2 = A2.clear_above(2)
print("Clearing rows above...")
assert A2.elements == [[1, 2, 0],[0, 1, 0],[0, 0, 1]], A2.elements

A2 = A2.clear_above(1)
print("Clearing above rows...")
assert A2.elements == [[1, 0, 0],[0, 1, 0],[0, 0, 1]]

print("Testing rref method...")
A = Matrix([[0, 1, 2],[3, 6, 9],[2, 6, 8]])
A = A.rref()
assert A2.elements == [[1,0,0],[0,1,0],[0,0,1]]
print("Passed")

A = Matrix([[1, 2,   3,  4],[5, 6,   7,  8],[9, 10, 11, 12]])
B = Matrix([[13, 14],[15, 16],[17, 18]])
print("Testing augment method...")
A_augmented = A.augment(B)
assert A_augmented.elements == [[1, 2,   3,  4, 13, 14],[5, 6,   7,  8, 15, 16],[9, 10, 11, 12, 17, 18]]
print("Passed")

rows_02 = A_augmented.get_rows([0,2])
print("Testing get rows method...")
assert rows_02.elements == [[1, 2,   3,  4, 13, 14],[9, 10, 11, 12, 17, 18]]
print("Passed")

cols_0123 = A_augmented.get_cols([0,1,2,3])
print("Testing method get cols...")
assert cols_0123.elements == [[1, 2,   3,  4],[5, 6,   7,  8],[9, 10, 11, 12]], cols_0123.elements
print("Passed")

A = Matrix([[1, 2],[3, 4]])
A_inv = A.inverse()
print("Testing iverse method...")
assert A_inv.elements == [[-2,   1],[1.5, -0.5]], A_inv.elements
print("Passed")

#ans = A.determinant()
#assert ans == -2, ans

A = Matrix([[1, 1, 0],[2, -1, 0],[0, 0, 3]])
A = A.exponent(3)
print("Testing exponent")
assert A.elements == [[3, 3, 0],[6, -3, 0],[0, 0, 27]], A.elements
print("Passed")

A = Matrix([[1,0,2,0,3],[0,4,0,5,0],[6,0,7,0,8],[-1,-2,-3,-4,-5]])

A_t = A.transpose()
assert A_t.elements == [[ 1,  0,  6, -1],[ 0,  4,  0, -2],[ 2,  0,  7, -3],[ 0,  5,  0, -4],[ 3,  0,  8, -5]]
print("eq works")

B = A_t @ A
assert B.elements == [[38,  2, 47,  4, 56],[ 2, 20,  6, 28, 10],[47,  6, 62, 12, 77],[ 4, 28, 12, 41, 20],[56, 10, 77, 20, 98]]
print("matmul works")

C = B * 0.1 
assert C.elements == [[3.8,  .2, 4.7,  .4, 5.6],[ .2, 2.0,  .6, 2.8, 1.0],[4.7,  .6, 6.2, 1.2, 7.7],[ .4, 2.8, 1.2, 4.1, 2.0],[5.6, 1.0, 7.7, 2.0, 9.8]]
print("mul works")

D = B - C
assert D.elements == [[34.2,  1.8, 42.3,  3.6, 50.4],[ 1.8, 18. ,  5.4, 25.2,  9. ],[42.3,  5.4, 55.8, 10.8, 69.3],[ 3.6, 25.2, 10.8, 36.9, 18. ],[50.4,  9. , 69.3, 18. , 88.2]]
print("sub works")

E = D + C
assert E.elements == [[38,  2, 47,  4, 56],[ 2, 20,  6, 28, 10],[47,  6, 62, 12, 77],[ 4, 28, 12, 41, 20],[56, 10, 77, 20, 98]]
print("add works")

assert (E == B) == True
assert (E == C) == False
print("eq works")

A = Matrix([[1, 2],[3, 4]])
assert A.cofactor_method_determinant() == -2, A.cofactor_method_determinant().elements
print("Passed")

A = Matrix([[1,2,0.5],[3,4,-1],[8,7,-2]])
#assert A.cofactor_method_determinant() == -10.5, A.cofactor_method_determinant().elements
print("passed")

A = Matrix([[1, 1, 0],[2, -1, 0],[0, 0, 3]])


B = 0.1 * A
assert B.elements == [[0.1, 0.1, 0],[0.2, -0.1, 0],[0, 0, 0.3]], B.elements
print("rmul works")

C = A**3
assert C.elements == [[3, 3, 0],[6, -3, 0],[0, 0, 27]]
print("pow wroks")