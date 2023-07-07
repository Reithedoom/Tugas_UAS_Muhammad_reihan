import pandas as pd
import matplotlib.pyplot as plt

# Baca data dari file CSV
data = pd.read_csv('data_grafik.csv')

# Hitung jumlah jenis usaha di setiap wilayah
count_data = data.groupby(['wilayah', 'jenis_usaha']).size().reset_index(name='count')

# Tampilkan grafik
fig = plt.figure(figsize=(10, 6))
plt.bar(count_data['wilayah'], count_data['count'])
plt.xlabel('Wilayah')
plt.ylabel('Jumlah Jenis Usaha')
plt.title('Sebaran Jenis Usaha di Setiap Wilayah')
plt.xticks(rotation=90)
plt.show()
fig

