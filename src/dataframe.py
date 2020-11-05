class DataFrame:
    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.columns = column_order

    def to_array(self):
        output_array = []
        values = []
        for key in self.data_dict:
            values.append(self.data_dict[key])
        for num in range(len(values[0])):
            curr_vals = []
            for col in values:
                curr_vals.append(col[num])
            output_array.append(curr_vals)
        return output_array

    def select_columns(self, cols_list):
        new_dict = {}
        for key in cols_list:
            new_dict[key] = self.data_dict[key]
        return DataFrame(new_dict, cols_list)
    
    def select_rows(self, row_list):
        output_array = []
        for row in row_list:
            output_array.append(self.to_array()[row])
        return output_array

                    

