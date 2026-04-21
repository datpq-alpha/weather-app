# ⛅ Weather App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://weather-app-klp8casuwv7j9thfdqje3z.streamlit.app/)
# Demo
<p align="center">
  <img src="images/weather.gif" width="800px" alt="Demo ứng dụng weather">
</p>
## 📌 Tổng quan dự án (Overview)
Ứng dụng **Weather App** là một công cụ dự báo thời tiết thông minh cho phép người dùng tra cứu thông tin thời gian thực từ khắp nơi trên thế giới. Điểm nổi bật của phiên bản này là hệ thống lưu trữ danh sách thành phố yêu thích và khả năng phân tích, so sánh nhiệt độ trực quan thông qua biểu đồ.

## ✨ Tính năng nổi bật (Key Features)
* **Real-time Data:** Truy xuất dữ liệu thời tiết chính xác (nhiệt độ, độ ẩm, trạng thái) thông qua OpenWeatherMap API.
* **Favorite System (SQLite):** Tích hợp cơ sở dữ liệu SQLite để lưu trữ, quản lý và xóa danh sách các thành phố quan tâm.
* **Advanced Analytics:** * So sánh nhiệt độ giữa các thành phố đã lưu bằng biểu đồ cột tương tác (`Plotly`).
    * Thanh tiến trình (`Progress bar`) khi cập nhật dữ liệu hàng loạt.
* **Data Export:** Hỗ trợ xuất báo cáo chi tiết ra file định dạng `.csv` (UTF-8-sig) để lưu trữ ngoại tuyến.
* **Responsive UI:** Giao diện chia Tab hiện đại với Sidebar điều hướng tiện lợi.

## 🛠 Công nghệ sử dụng (Tech Stack)
* **Ngôn ngữ:** Python 3.x
* **Giao diện:** Streamlit (Wide mode)
* **API:** OpenWeatherMap API
* **Cơ sở dữ liệu:** SQLite (SQL)
* **Xử lý & Trực quan hóa:** Pandas, Plotly Express

## 🏗 Kiến trúc dự án
Dự án được xây dựng theo mô hình module hóa:
1. **Database Layer:** Quản lý kết nối và các truy vấn SQL (Insert, Delete, Select).
2. **API Layer:** Xử lý các yêu cầu HTTP và chuẩn hóa dữ liệu JSON từ API.
3. **State Management:** Sử dụng `st.session_state` để duy trì dữ liệu người dùng giữa các lần tương tác.

## 🚀 Hướng dẫn cài đặt
1. Clone dự án về máy:
   ```bash
   git clone (https://github.com/datpq-alpha/weather-app.git)
2. Cài đặt thư viện:

   ```bash
   pip install -r requirements.txt
3. Cấu hình API Key:
Mở file weather_funcs.py và thay thế your_api_key bằng API Key từ OpenWeatherMap hoặc cấu hình API trong secrets của Streamlit Cloud

4. Khởi chạy:

   ```bash
   streamlit run ui_main.py
