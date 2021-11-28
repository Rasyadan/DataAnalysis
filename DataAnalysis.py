import pandas as pd
import os
import matplotlib.pyplot as plt
#Loading data dan mengetahui informasi data
#============================================================================
#PASTIKAN FILE "video_games.csv" ADA DI FOLDER YANG SAMA DENGAN KODE PROGRAM
#============================================================================
file_location = "video_games.csv"

#Deskripsi Data dan File
print("TUGAS 3: Deskripsi Data dan File")
print("="*50)
Data = pd.read_csv(file_location)
data_size = os.path.getsize(file_location)//1024
data_type = os.path.splitext(file_location)[1]
data_info = Data.shape


print("File size dari data adalah :",data_size, " kB")
print("Format data adalah :",data_type)
print("Dimensi dari data :",data_info[0],"Baris dan",data_info[1],"Kolom")
print("=" * 50)

#Karakteristik Data
print("TUGAS 4 : Karakteristik Data")
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
print("TUGAS 6 : Visualisasi Data")
# Histogram dari Review Score dan Sales untuk mengetahui persebaran data
df_review_sorted1 = Data.sort_values(["Metrics.Review Score"], ascending=[1])
df_review_sorted1["Metrics.Review Score"].plot(kind="hist",bins=[0,10,20,30,40,50,60,70,80,90,100], rwidth = 0.8, title = "Histogram of Review Score", xlabel = "Review Score", legend = True)
plt.legend(["Review Score"])
plt.show()

Data["Metrics.Sales"] = Data["Metrics.Sales"]/1000
df_review_sorted2 = Data.sort_values(["Metrics.Sales"], ascending=[1])
df_review_sorted2["Metrics.Sales"].plot(kind="hist",bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], rwidth = 0.8, title = "Histogram Total Penjualan", xlabel = "Total Penjualan", legend = True)
plt.legend(["Total Penjualan (Juta USD)"])
plt.show()

# Line graph untuk mengetahui perkembangan review score dan sales dari tahun ke tahun
year_mean_review_score = (Data.groupby("Release.Year")["Metrics.Review Score"].mean())
df2 = year_mean_review_score
df2.plot(kind="line", x="Release.Year", legend=True, xlabel = "Release Year", ylabel = "Review Score", title ="Review Score Setiap Tahun")
plt.legend(["Review Score"])
plt.show()

year_mean_sales = (Data.groupby("Release.Year")["Metrics.Sales"].mean())
dfsales = year_mean_sales
dfsales.plot(kind="line", x="Release.Year", legend=True, xlabel = "Release Year", ylabel = "Total Penjualan", title ="Perkembangan Sales Setiap Tahun")
plt.legend(["Total Penjualan"])
plt.show()

# Pie chart dari rating game dan tahun rilis game untuk mengetahui hierarki dan hubungan keseluruhan bagian
df3 = Data["Release.Rating"].value_counts()
df3.plot(kind="pie", title="Pie Chart Rating Game", y="Release Rating", legend=True)
plt.legend(["Everyone", "Teen", "Mature"])
plt.show()

dfyear = Data["Release.Year"].value_counts()
dfyear.plot(kind="pie", title="Pie Chart Tahun Perilisan Game", y="Tahun Rilis", legend=True)
plt.legend(["2007","2008","2006","2005","2004"])
plt.show()

# Scatter plot dari review score dan total penjualan untuk mengetahui hubungan antar keduanya
df4 = Data
df4.plot(kind="scatter", x="Metrics.Review Score",xlabel = "Review Score", y="Metrics.Sales", ylabel = "Total Penjualan (Miliar USD)", title ="Scatter Plot Review Score dan Total Penjualan")
plt.show()

#Scatter plot dari total penjualan dan used price
dfscatter2 = Data
dfscatter2["Metrics.Used Price"] = dfscatter2["Metrics.Used Price"]/100
dfscatter2.plot(kind="scatter", x="Metrics.Used Price", xlabel="Total Penjualan (Miliar USD)", y="Metrics.Sales", ylabel="Harga Bekas", title="Scatter Plot Total Penjualan dengan Harga Bekas")
plt.show()

#Korelasi review score dengan total penjualan
print("TUGAS 7 : Korelasi")
correlation = df4["Metrics.Review Score"].corr(df4["Metrics.Sales"])
print("Koefisien korelasi antara review score dengan penjualan adalah " + str(correlation))
print("="*50)
#Visualisasi korelasi dengan scatter plot
df4 = Data
df4.plot(kind="scatter", x="Metrics.Review Score",xlabel = "Review Score", y="Metrics.Sales", ylabel = "Total Penjualan (Miliar USD)", title ="Scatter Plot Review Score dan Total Penjualan")
plt.show()
#Korelasi total penjualan dengan harga bekas
corr2 = dfscatter2["Metrics.Used Price"].corr(dfscatter2["Metrics.Sales"])
print("Koefisien korelasi antara penjualan dengan harga bekas adalah " + str(corr2))
print("="*50)
#Visualisasi korelasi
dfscatter2 = Data
dfscatter2["Metrics.Used Price"] = dfscatter2["Metrics.Used Price"]/100
dfscatter2.plot(kind="scatter", x="Metrics.Used Price", xlabel="Total Penjualan (Miliar USD)", y="Metrics.Sales", ylabel="Harga Bekas", title="Scatter Plot Total Penjualan dengan Harga Bekas")
plt.show()
