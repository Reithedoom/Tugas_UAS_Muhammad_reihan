import pandas as pd
import matplotlib.pyplot as plt

# Baca data dari file CSV
data = pd.read_csv('data_grafik.csv')

# Hitung jumlah jenis usaha di setiap kecamatan
count_data = data.groupby(['jenis_usaha', 'kecamatan']).size().reset_index(name='count')

# Tampilkan grafik
fig = plt.figure(figsize=(10, 6))
plt.bar(count_data['kecamatan'], count_data['count'])
plt.xlabel('Kecamatan')
plt.ylabel('Jumlah Jenis Usaha')
plt.title('Sebaran Jenis Usaha di Setiap Kecamatan')
plt.xticks(rotation=90)
plt.show()
fig