import pandas as pd
import os

#Loading data dan mengetahui informasi data

file_location = "C:/Users/Faza/Downloads/video_games.csv"

Data = pd.read_csv(file_location)
data_size = os.path.getsize(file_location)//1024
data_type = os.path.splitext(file_location)[1]
data_info = Data.shape


print("File size dari data adalah :",data_size, " kB")
print("Format data adalah :",data_type)
print("Dimensi dari data :",data_info[0],"Baris dan",data_info[1],"Kolom")
print("")

#Karakteristik Data
data_columns = Data.info()
print(data_columns)

