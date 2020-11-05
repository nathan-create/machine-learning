import sys
sys.path.append('src')
from dataframe import DataFrame

data_dict = {'Pete': [1, 0, 1, 0],'John': [2, 1, 0, 2],'Sarah': [3, 1, 4, 0]}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sarah'])

print("Testing to to_array")
assert df1.to_array() == [[1, 2, 3],[0, 1, 1],[1, 0, 4],[0, 2, 0]]
print("Passed")

df2 = df1.select_columns(['Sarah', 'Pete'])

print("Testing select_columns")
assert df2.to_array() == [[3, 1],[1, 0],[4, 1],[0, 0]]
print("Passed")

assert df2.columns == ['Sarah', 'Pete']

print("Testing select_rows")
df3 = df1.select_rows([1,3])
print("Passed")

assert df3 == [[0, 1, 1],[0, 2, 0]]