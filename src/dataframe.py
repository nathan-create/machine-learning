def convert_row_from_arr_to_dict( arr, cols_list):
    output_dict = {}
    for key in cols_list:
        val_index = cols_list.index(key)
        output_dict[key] = arr[val_index]
    return output_dict



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

    def apply(self, column, function):
        new_dict = {}
        for key in self.data_dict:
            if key == column:
                new_values = []
                for num in self.data_dict[key]:
                    new_values.append(function(num))
                new_dict[key] = new_values
            else:
                new_dict[key] = self.data_dict[key]
        return DataFrame(new_dict, self.columns)

    @classmethod
    def from_array(cls, arr, cols):
        data_dict = {}
        for key in range(len(cols)):
            key_val = []
            for vals_list in arr:
                key_val.append(vals_list[key])
            data_dict[cols[key]] = key_val
        return cls(data_dict, cols)


    def select_rows_where(self, test):
        output_array = []
        for info in self.to_array():
            if test(convert_row_from_arr_to_dict(info, self.columns)) == True:
                output_array.append(None)
        return output_array

#    def order_by(self, col, ascending):
#        arr_index = self.columns.index(col)
#        arr = self.to_array()
#        for info in arr:
#            if ascending == True:
                
