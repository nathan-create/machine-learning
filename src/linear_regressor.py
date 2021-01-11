import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame

class LinearRegressor:
    def __init__(self, dataframe, dependant_var):
        self.dataframe = dataframe
        self.dep_var = dependant_var
        self.coefficients = self.calculate_coefficients()

    def calculate_coefficients(self):
        dataframe_arr = self.dataframe.to_array()
        d_index = self.df.columns.index(self.dep_var)
        end_matrix = []
        for num in range(len(dataframe_arr)):
            end_matrix.append([])
            end_matrix[num].append(dataframe_arr[num[d_index]])
        end_matrix = Matrix(end_matrix)
        eq_matrix=[]
        for num in range(len(dataframe_arr)):
            eq_matrix.append([])
            for num2 in range(len(dataframe_arr[0])):
                if num2 == 0:
                    eq_matrix[num].append(1)
                if num2 != d_index:
                    eq_matrix[num].append(dataframe_arr[num][num2])
        system_mat = Matrix(eq_matrix)
        transpose = system_mat.transpose()    
        new_system_mat = transpose @ system_mat
        inverse = new_system_mat.inverse()
        coefficients_mat = inverse @ transpose @ end_matrix
        coefficient_dict = {}
        for num in range(len(coefficients_mat.elements)):
            if num == 0:
                coefficient_dict['constant'] = coefficients_mat.elements[num][0]
            elif num != 0:
                coefficient_dict[self.dataframe_arr.columns[num-1]]=coefficients_mat.elements[num][0]
        return coefficient_dict

    def predict(self, input_dict):
        result = 0
        for key in self.coefficients:
            if key in input_dict:
                result += self.coefficients[key]*input_dict[key]
            else:
                result += self.coefficients[key]
        return result