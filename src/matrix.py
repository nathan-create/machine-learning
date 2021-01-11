def first_nonzero_entry_index(elements, row_index):
    row = elements[row_index]
    first_nonzero_entry_index = 0
    for row_element in row:
        if row_element == 0:
            first_nonzero_entry_index += 1
        else:
            break
    return first_nonzero_entry_index

def remove_entries(elements, index_list):
    elements.remove(elements[index_list[0]])
    for row in range(len(elements)):
        for col in range(len(elements[0])):
            if col == index_list[1]:
                elements[row].remove(elements[row][col])
    return elements


class Matrix:
    def __init__(self, elements):
        self.elements = elements
        self.num_rows = len(elements)
        self.num_cols = len(elements[0])
    def elements(self):
        return self.elements

    def copy(self):
        new_matrix = []
        for elem in range(self.num_rows):
            new_matrix.append(self.elements[elem])
        return Matrix(new_matrix)

    def add(self, new_matrix):
        result = [[0 for space in range(self.num_cols)] for space in range(self.num_rows)]
        for row_index in range(self.num_rows):
            for col_index in range(self.num_cols):
                sum_of_elements = self.elements[row_index][col_index] + new_matrix.elements[row_index][col_index]
                result[row_index][col_index] = sum_of_elements
        return Matrix(result)

    def subtract(self, new_matrix):
        result = [[0 for space in range(self.num_cols)] for space in range(self.num_rows)]
        for row_index in range(self.num_rows):
            for col_index in range(self.num_cols):
                sum_of_elements = self.elements[row_index][col_index] - new_matrix.elements[row_index][col_index]
                result[row_index][col_index] = sum_of_elements
        return Matrix(result)

   
    def scalar_multiply(self, scalar):
        result = [[0 for space in range(self.num_cols)] for space in range(self.num_rows)]
        for row_index in range(self.num_rows):
            for col_index in range(self.num_cols):
                result[row_index][col_index] = round(scalar*self.elements[row_index][col_index], 1)

        return Matrix(result)

    def matrix_multiply(self, new_matrix):
        result = [[0 for space in range(self.num_rows)] for space in range(new_matrix.num_cols)]
        for row_index in range(self.num_rows):
            for col_index in range(new_matrix.num_cols):
                row = self.elements[row_index]
                col = [new_matrix.elements[k][col_index] for k in range(self.num_cols)]
                dot_product = 0
                for i in range(len(row)):
                    dot_product += row[i]*col[i]
                result[row_index][col_index] = dot_product
        return Matrix(result)

    def transpose(self):
        result = [[0 for space in range(self.num_rows)] for space in range(self.num_cols)]
        for row_index in range(self.num_rows):
            for col_index in range(self.num_cols):
                element = self.elements[row_index][col_index]
                result[col_index][row_index] = element
        return Matrix(result)

    def is_equal(self, matrix):     
        for row_index in range(self.num_rows):
            for col_index in range(self.num_cols):
                if self.elements[row_index][col_index] == matrix.elements[row_index][col_index]:
                    return True
                else:
                    return False
    
    def get_pivot_row(self, column_index):
        for row in range(self.num_rows):
            col_index = 0
            for col in range(self.num_cols):
                if self.elements[row][col] == 0:
                    col_index+=1

                elif col_index == column_index and self.elements[row][column_index] !=0:
                    return row
                
                    
    def swap_rows(self, row_index1, row_index2):
        result = [[0 for space in range(self.num_cols)] for space in range(self.num_rows)]   
        for row_index in range(self.num_rows):
            element = self.elements[row_index]
            if row_index == row_index1:
                result[row_index] = self.elements[row_index2]
            elif row_index == row_index2:
                result[row_index] = self.elements[row_index1]
            else:
                result[row_index] = self.elements[row_index]
        return Matrix(result)

    def normalize_row(self, row_index):
        result = [[0 for space in range(self.num_cols)] for space in range(self.num_rows)] 
        row = self.elements[row_index]
        index_of_first_nonzero_entry =  first_nonzero_entry_index(self.elements, row_index)
        norm_number = self.elements[row_index][index_of_first_nonzero_entry]
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if row_index == row:
                    result[row][col] = self.elements[row][col] / norm_number 
                else:
                    result[row][col]=self.elements[row][col]
        return Matrix(result)

    def clear_below(self, row_index):
        result = [[0 for space in range(self.num_cols)] for space in range(self.num_rows)]   
        for num in range(len(self.elements[row_index])):
            if self.elements[row_index][num] != 0:
                col_index = self.elements[row_index].index(self.elements[row_index][num])
                break
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                
                if row > row_index and self.elements[row][col_index] != 0:
                    result[row][col] = self.elements[row][col] - self.elements[row][col_index] * self.elements[row_index][col]
                else:
                    result[row][col] = self.elements[row][col]
        return Matrix(result)
                
    def clear_above(self, row_index):
        result = [[0 for space in range(self.num_cols)] for space in range(self.num_rows)]   
        for num in range(len(self.elements[row_index])):
            if self.elements[row_index][num] != 0:
                col_index = self.elements[row_index].index(self.elements[row_index][num])
                break
        
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if row < row_index and self.elements[row][col_index] != 0:
                    result[row][col] = self.elements[row][col] - self.elements[row][col_index] * self.elements[row_index][col]
                else:
                    result[row][col] = self.elements[row][col]
        return Matrix(result)
                
        
    def rref(self):
        matrix = self.copy()
        row_index = 0
        for col_index in range(matrix.num_cols):
            if matrix.get_pivot_row(col_index) != None:
                if matrix.get_pivot_row(col_index) != row_index:
                    matrix = matrix.swap_rows(matrix.elements[matrix.get_pivot_row(col_index)], matrix.elements[row_index])
                matrix = matrix.normalize_row(row_index)
                matrix = matrix.clear_below(row_index)
                matrix = matrix.clear_above(row_index)
                row_index+=1
        return matrix

    def augment(self, matrix):
        result = [[0 for space in range(self.num_cols)] for space in range(self.num_rows)]
        if self.num_rows == matrix.num_rows:
            for row in range(len(self.elements)):
                result[row] = self.elements[row] + matrix.elements[row]
        return Matrix(result)
       
    def get_rows(self,row_list):
        list_of_rows = []
        for row_index in row_list:
            list_of_rows.append(self.elements[row_index])
        return Matrix(list_of_rows)

    def get_cols(self, col_list):
        list_of_cols = []
        result = []
        for row in range(self.num_rows):
            for col_index in col_list:
                list_of_cols.append(self.elements[row][col_index])
            result.append(list_of_cols)
            list_of_cols = []
        return Matrix(result)

    def inverse(self):
        result = self.copy()
        
        identity = [[1 if num == num2 else 0 for num2 in range(self.num_cols)]for num in range(self.num_rows)]
                
        identity_matrix = Matrix(identity)

        if self.num_cols != self.num_rows:
            print("Matrix is not invertible as it is not square.")
        elif [0 for num in range(self.num_cols)] in result.rref().elements:
            print("Unable to get inverse of matrix as it is singular.")
        else:
            result_augmented = result.augment(identity_matrix)
           
            result_augmented = result_augmented.rref()
           
            result_augmented = result_augmented.get_cols([num for num in range(len(result.elements[0]),len(result_augmented.elements[0]))])
            return result_augmented

    def determinant(self):
        matrix = self.copy()
        num_swaps = 0
        factors = 1
        if matrix.rref() == [[1 if num == num2 else 0 for num2 in range(matrix.num_cols)]for num in range(matrix.num_rows)]:
            row_index = 0
            for col_index in range(matrix.num_cols):
                if matrix.get_pivot_row(col_index) != None:
                    if matrix.get_pivot_row(col_index) != row_index:
                        matrix = matrix.swap_rows(matrix.elements[matrix.get_pivot_row(col_index)], matrix.elements[row_index])
                    if matrix.elements[row_index][col_index] != 1:
                        factors = factors * matrix.elements[row_index][col_index]
                    matrix = matrix.normalize_row(row_index)
                    matrix = matrix.clear_below(row_index)
                    matrix = matrix.clear_above(row_index)
                    row_index+=1
                    
        deter = factors * (-1 ** num_swaps)
        return deter

    def exponent(self, num):
        result = self.copy()
        for times in range(num-1):
            result = result.matrix_multiply(self)
        return result

    def __add__(self,matrix):
        return self.add(matrix)
    
    def __sub__(self,matrix):
        return self.subtract(matrix)

    def __mul__(self, scalar):
        return self.scalar_multiply(scalar)

    def __matmul__(self, matrix):
        return self.matrix_multiply(matrix)

    def __eq__(self, matrix):
        return self.is_equal(matrix)

    def __rmul__(self, scalar):
        return self.scalar_multiply(scalar)

    def __pow__(self, scalar):
        return self.exponent(scalar)

    def cofactor_method_determinant(self):
        result = self.copy()
        deter = 0
        if len(self.elements) > 2:
            for num in range(len(result.elements[0])):
                print(num)
                curr_lower_matrix = Matrix(remove_entries(self.elements, [0,0]))
                print(curr_lower_matrix.elements)
                deter += result.elements[0][num] * curr_lower_matrix.cofactor_method_determinant()
                print(deter)
        else:
            deter += (result.elements[0][0] * result.elements[1][1]) - (result.elements[0][1] *result.elements[1][0])
        return deter
