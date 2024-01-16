import os 
import pandas as pd 

current_dir = os.path.dirname(os.path.realpath(__file__))
excel_file_path = os.path.join(current_dir, 'routine.xls.xlsx')
routine = pd.read_excel(excel_file_path)

cell_value = routine.iloc[0,1]
print(f'the value of the first cell is {cell_value}')

# print(routine)



