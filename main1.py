import os
import pandas as pd

current_dir = os.path.dirname(os.path.realpath(__file__))
excel_file_path = os.path.join(current_dir, 'routine.xls.xlsx')
routine = pd.read_excel(excel_file_path)

# Print the entire DataFrame to inspect its structure
print("DataFrame:")
print(routine)

# Specify the day and timing you want to retrieve
day_to_retrieve = 'Sunday'
timing_to_retrieve = '7:10-7:45'

# Retrieve the value from the specified cell using .loc
cell_value = routine.iloc[routine['Day'] == day_to_retrieve, timing_to_retrieve].values[0]

# Print the result
print(f"Value for {day_to_retrieve} at {timing_to_retrieve}: {cell_value}")
