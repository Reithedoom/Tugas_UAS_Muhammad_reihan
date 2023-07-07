import pandas as pd
import matplotlib.pyplot as plt

# Baca data dari file CSV
data = pd.read_csv('data_grafik.csv')

# Hitung jumlah kecamatan yang memiliki jenis usaha pada setiap wilayah
count_data = data.groupby(['wilayah', 'kecamatan']).size().reset_index(name='count')

# Tampilkan grafik
fig = plt.figure(figsize=(10, 6))
plt.bar(count_data['wilayah'], count_data['count'])
plt.xlabel('Wilayah')
plt.ylabel('Jumlah Kecamatan')
plt.title('Sebaran Kecamatan dengan Jenis Usaha pada Setiap Wilayah')
plt.xticks(rotation=90)
plt.show()
fig