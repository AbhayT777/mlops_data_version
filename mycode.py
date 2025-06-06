import pandas as pd
import os

#create a sample data frame with column names
data = {'Name': ['atul', 'bikas', 'chandan'],
        'age': [25,26,27],
        'city': ['delhi', 'kolkata', 'lucknow']}

df = pd.DataFrame(data)

new_row = {'Name': 'rupa', 'age': 20, 'city': 'mumbai'}   #adding new row for v2
df.loc[len(df.index)] = new_row

new_row2 = {'Name': 'sonam', 'age': 25, 'city': 'bihar'}   #adding new row for v3
df.loc[len(df.index)] = new_row2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#define the filepath
file_path = os.path.join(data_dir, 'sample_data.csv')

#save the dataframe to acsv file, including coloum names
df.to_csv(file_path, index=False)
print('csv_file save to'+file_path )