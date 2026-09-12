import os
import pandas as pd

data = {
      'name':["ritesh" , 'suman' , 'krushna'],
      'age' : [25,23,28],
      'city' : ['banglore' , 'hydrabad' , 'bbsr']
}

df = pd.DataFrame(data)


# adding new row to df
new_row = { "name" : "rajesh" , "age" : 30 , "city" : "cuttack" }
df.loc[len(df.index)] = new_row

new_row2 = {'name':'trinath' , 'age':23 , 'city':'balasore'}
df.loc[len(df.index)] = new_row2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir , 'sample_data.csv')

df.to_csv(file_path , index=False)

print(f"csv file saved to {file_path}")






