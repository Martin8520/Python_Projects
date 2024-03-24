import pandas as pd

input_file = 'input_data.csv'
output_file = 'output_data.csv'

data = pd.read_csv(input_file)

data.columns = data.columns.str.strip()

data['Senior'] = data['Age'].apply(lambda age: 'Yes' if age >= 60 else 'No')

seniors_data = data[data['Senior'] == 'Yes']

seniors_data.to_csv(output_file, index=False)

print("Senior citizens data has been written to 'output_data.csv'.")
