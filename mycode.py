import pandas as pd
import os

#create a sample data frame with column names
data = {'Nmae': ['atul', 'bikas', 'chandan'],
        'age': [25,26,27],
        'city': ['delhi', 'kolkata', 'lucknow']}

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#define the filepath
file_path = os.path.join(data_dir, 'sample_data.csv')

#save the dataframe to acsv file, including coloum names
df.to_csv(file_path, index=False)
print('csv_file save to'+file_path )