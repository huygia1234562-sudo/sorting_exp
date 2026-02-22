import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dữ liệu thực tế từ quá trình thử nghiệm
data = {
    'Dữ liệu': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Quicksort': [1127.42, 1044.2, 2251.83, 2167.5, 1812.51, 1708.82, 1971.04, 1950.23 ,1661.72, 1660.01],
    'Heapsort': [6990.21, 6471.57, 7022.09, 7092.53, 6848.8, 6701.97, 6812.23, 7307.83, 7551.85, 7463.16],
    'Mergesort': [2995.47, 3009.95, 3451.26, 3404.16, 3384.97, 3377.45, 3417.09, 3533.25, 3543.74 ,3600.14],
    'sort (C++)': [345, 197, 481, 404, 411, 427, 476, 563, 443, 407],
    'sort (numpy)': [36.95, 39.24, 38.89, 38.2, 37.93, 37.82, 38.94, 37.04, 36.88, 37.16]
}

df = pd.DataFrame(data)

# Thiết lập biểu đồ
plt.figure(figsize=(12, 6))
x = np.arange(len(df['Dữ liệu']))
width = 0.15

# Vẽ từng cột cho các thuật toán
plt.bar(x - 2*width, df['Quicksort'], width, label='Quicksort', color='#3498db')
plt.bar(x - width, df['Heapsort'], width, label='Heapsort', color='#e67e22')
plt.bar(x, df['Mergesort'], width, label='Mergesort', color='#95a5a6')
plt.bar(x + width, df['sort (C++)'], width, label='sort (C++)', color='#f1c40f')
plt.bar(x + 2*width, df['sort (numpy)'], width, label='sort (numpy)', color='#2ecc71')

# Thêm nhãn và tiêu đề
plt.xlabel('Bộ dữ liệu (1-10)')
plt.ylabel('Thời gian thực hiện (ms)')
plt.title('So sánh hiệu năng các thuật toán sắp xếp trên 1.000.000 phần tử')
plt.xticks(x, df['Dữ liệu'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Lưu biểu đồ
plt.savefig('sorting_comparison_chart.png')
plt.show()