
class DataFrame:
    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.columns = column_order

    def to_array(self):
        output_array = []
        count_var = 0
        for num in range(len(self.data_dict[self.columns[0]])):
            output_array.append([])
            for key in self.columns:
                output_array[count_var].append(self.data_dict[key][num])
            count_var += 1
        return output_array

    def select_columns(self, cols_list):
        return DataFrame(self.data_dict, cols_list)
    
    def select_rows(self, row_list):
        new_dict = self.data_dict
        for key in self.columns:
            key_data = []
            for row in range(len(clone_dict[key])):
                if row in row_list:
                    key_data.append(new_dict[key][row])
            new_dict[key] = key_data
        return DataFrame(new_dict,self.columns)

    def apply(self, column, function):
        updated_data = []
        for num in self.data_dict[column]:
            updated_data.append(function(num))
        self.data_dict[column] = updated_data
        return self

    @classmethod
    def from_array(cls, arr, cols):
        data_dict = {}
        for num in range(len(cols)):
            data_dict[cols[num]] = []
            for i in range(len(arr)):
                data_dict[cols[num]].append(arr[i][num])
        return cls(data_dict, cols)

    def row_to_dict(self, row, cols):
        output_dict = {}
        for num in range(len(cols)):
            output_dict[cols[num]] = row[num]
        return output_dict


    def select_rows_where(self, test):
        output_arr = []
        new_arr = self.to_array()
        for data in new_arr:
            row_dict = self.row_to_dict(data, self.columns)
            if test(row_dict):
                output_arr.append(data)
        return DataFrame.from_array(output_arr, self.columns)

        for info in self.to_array():
            if test(convert_row_from_arr_to_dict(info, self.columns)) == True:
                output_array.append(None)
        return output_array

    def order_by(self, col, ascending):
        output_arr = []
        arr_index = self.columns.index(col)
        arr = self.to_array()
        while len(arr) > 0:
            first_row = arr[0]
            for data in arr:
                if data[arr_index] < first_row[arr_index]:
                    first_row = data
            output_arr.append(first_row)
            arr.remove(first_row)
        if ascending == True:
            return DataFrame.from_array(output_arr, self.columns)
        else:
            return DataFrame.from_array(output_arr[::-1], self.columns)

    def interaction_terms(self, col_1, col_2):
        output_data = {}
        for key in self.data_dict:
            new_data_dict[key] = self.data_dict[key]
        interact_terms = [col for col in self.columns]
        interact_terms.append(col_1 + ' * ' + col_2)
        col_1_arr = self.data_dict[col_1]
        col_2_arr = self.data_dict[col_2]
        new_cols = [col_1_arr[num]*col_2_arr[num] for num in range(len(col_1_arr))]
        new_data_dict[col_1 + ' * ' + col_2] = new_cols
        return DataFrame(output_data, new_cols)

    def create_dummy_variable(self, dum_var_name):
        target = [num for num in self.data_dict[dum_var]]
        dum_vars = []
        for num in target:
            for var in num:
                if var not in dum_vars:
                    dum_vars.append(var)
        adding_cols = []
        for col in self.columns:
            if col != dum_var_name:
                adding_cols.append(col)
            else:
                for var in dum_vars:
                    adding_cols.append(var)
        output_dict = dict(self.data_dict)
        del output_dict[dum_var_name]
        for var in dum_vars:
             output_dict[var] = [0 if var not in _ else 1 for _ in target]
        return DataFrame(output_dict, adding_cols)