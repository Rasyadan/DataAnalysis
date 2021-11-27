import pandas as pd
import os

#Loading data dan mengetahui informasi data

file_location = "D:/Fajri/Downloads/video_games.csv"

Data = pd.read_csv(file_location)
data_size = os.path.getsize(file_location)//1024
data_type = os.path.splitext(file_location)[1]
data_info = Data.shape


print("File size dari data adalah :",data_size, " kB")
print("Format data adalah :",data_type)
print("Dimensi dari data :",data_info[0],"Baris dan",data_info[1],"Kolom")
print("=" * 50)

#Karakteristik Data
data_columns = Data.info()
print(data_columns)
print("=" * 50)

# Statistik
print("TUGAS 5: STATISTIK")
print("=" * 50)
# Sampel data
print("Sampel Data")
print("=" * 50)
# Sepuluh data pertama dari baris 1 s.d. 10
# Kolom Title dan Metrics.Review Score
print("Sepuluh data pertama dari baris 1 s.d. 10 pada kolom Title dan Metrics.Review Score")
print(Data.loc[:9, ["Title","Metrics.Review Score"]])
print("=" * 50)

# Urutan rating terbesar ke terkecil
print("Urutan dari rating terbesar ke terkecil")
print((Data.sort_values(["Metrics.Review Score"], ascending=[0]))[["Title", "Metrics.Review Score"]])
print("=" * 50)

# Sampel data setiap kolom
print("Sampel data tiap kolom pada indeks 0")
print(Data.loc[0])
print("=" * 50)

# Statistik
print("Statistik")
print("=" * 50)

# Rata-rata
print("Rata-rata pada kolom Metrics.Review Score")
mean = Data["Metrics.Review Score"].mean()
print(f"Rata-rata review score : {mean}")
print("=" * 50)

# Standar deviasi
print("Standar deviasi pada kolom Metrics.Review Score")
std = Data["Metrics.Review Score"].std()
print(f"Standar deviasi review score : {std}")
print("=" * 50)

# Percentile
# 10%
print("Percentile 10 % pada kolom Metrics.Review Score")
pct = Data["Metrics.Review Score"].quantile(.1)
print(f"Percentile 10 % review score : {pct}")
print("=" * 50)

# 25%
print("Percentile 25 % pada kolom Metrics.Review Score")
pct = Data["Metrics.Review Score"].quantile(.25)
print(f"Percentile 25 % review score : {pct}")
print("=" * 50)

# 50%
print("Percentile 50 % pada kolom Metrics.Review Score")
pct = Data["Metrics.Review Score"].quantile(.5)
print(f"Percentile 50 % review score : {pct}")
print("=" * 50)

# 75%
print("Percentile 75 % pada kolom Metrics.Review Score")
pct = Data["Metrics.Review Score"].quantile(.75)
print(f"Percentile 75 % review score : {pct}")
print("=" * 50)

# 90%
print("Percentile 90 % pada kolom Metrics.Review Score")
pct = Data["Metrics.Review Score"].quantile(.9)
print(f"Percentile 90 % review score : {pct}")
print("=" * 50)

# Ekstremum
# Maksimum
print("Nilai maksimum pada kolom Metrics.Review Score")
max = Data["Metrics.Review Score"].idxmax()
print(Data[max:max+1][["Title", "Metrics.Review Score"]])
print("=" * 50)

# Minimum
print("Nilai minimum pada kolom Metrics.Review Score")
min = Data["Metrics.Review Score"].idxmin()
print(Data[min:min+1][["Title", "Metrics.Review Score"]])
print("=" * 50)

# Distribusi frekuensi
print("Distribusi frekuensi pada kolom Metrics.Review Score")
disf = Data["Metrics.Review Score"].value_counts()
print(f"Distribusi frekuensi review score : {disf}")
print("=" * 50)

#Visualisasi Data

# Histogram dari Review Score untuk mengetahui persebaran data
df_review_sorted = Data.sort_values(["Metrics.Review Score"], ascending=[1])
df_review_sorted["Metrics.Review Score"].plot(kind="hist",bins=[0,10,20,30,40,50,60,70,80,90,100], rwidth = 0.8, title = "Histogram of Review Score", xlabel = "Review Score", legend = True)
plt.legend(["Review Score"])
plt.show()

# Line graph untuk mengetahui perkembangan review score dari tahun ke tahun
year_mean_review_score = (Data.groupby("Release.Year")["Metrics.Review Score"].mean())
df2 = year_mean_review_score
df2.plot(kind="line", x="Release.Year", legend=True, xlabel = "Release Year", ylabel = "Review Score", title ="Review Score Setiap Tahun")
plt.legend(["Review Score"])
plt.show()

# Pie chart dari rating game untuk mengetahui hierarki dan hubungan keseluruhan bagian
df3 = Data["Release.Rating"].value_counts()
df3.plot(kind="pie", title="Pie Chart of Game Ratings", y="Release Rating", legend=True)
plt.legend(["Everyone", "Teen", "Mature"])
plt.show()

# Scatter plot dari review score dan total penjualan untuk mengetahui hubungan antar keduanya
df4 = Data
df4.plot(kind="scatter", x="Metrics.Review Score",xlabel = "Review Score", y="Metrics.Sales", ylabel = "Total Penjualan (Miliar USD)", title ="Scatter Plot Review Score dan Total Penjualan")
plt.show()
