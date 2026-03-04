import pandas as pd

file = pd.read_csv(r"C:\Users\student\DSA-lab\DSA-lab\Read_and_write_data_files\data.csv")
print(file)

file.to_csv(r"C:\Users\student\DSA-lab\DSA-lab\Read_and_write_data_files\data2.csv")#,Index = False 
print(r"C:\Users\student\DSA-lab\DSA-lab\Read_and_write_data_files\data2.csv")