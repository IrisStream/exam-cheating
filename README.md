# Phân tích gian lận thi cử tỉnh Hà Giang 2018

## Danh sách thành viên

| MSSV     | Họ Tên               |
| -------- | -------------------- |
| 18120078 | Ngô Phù Hữu Đại Sơn  |
| 18120253 | Mai Ngọc Tú          |
| 18120201 | Nguyễn Bảo Long      |
| 18120227 | Phạm Văn Minh Phương |
| 1712424  | Hàn Văn Gia Hiên     |

## Tiền xử lý:

Điểm khối D của 1 số tỉnh có giá trị bất thường (#VALUE!), loại bỏ hết các giá trị trên ([source code][7])

## Phân công

1. Histogram phân bố điểm từng môn:

   - Sơn: Toán, ngữ văn, A
   - Tú: Ngoại ngữ, vật lý, B
   - Bảo Bảo: Hóa học, sinh học, C
   - Phương: Lịch sử, địa lý D
   - Hiên: GDCD, A1

2. Pie chart so sánh số thí sinh trên 27đ các khối của tỉnh Hà Giang so với cả nước.
   - Sơn: Khối A
   - Tú: Khối B
   - Bảo Long: Khối C
   - Minh Phương: Khối D
   - Gia Hiên: Khối A1

## Nội dung

[Phân tích thống kê điểm thi THPT QG 2018 tỉnh Hà Giang so với cả nước.][6]

## Nguồn dữ liệu

[Điểm thi THPT QG 2018][1]

## Tài liệu tham khảo

- [Pie chart using plotly][2]
- [Histogram in matplotlib][3]
- [Subplots in matplotlib][4]
- [Pandas][5]

[1]: https://github.com/dnanhkhoa/nhse-dataset
[2]: https://plotly.com/python/pie-charts/
[3]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
[4]: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
[5]: https://pandas.pydata.org/docs/
[6]: src/report.ipynb
[7]: src/preprocessing.py
