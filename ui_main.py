import streamlit as st
import pandas as pd
import plotly.express as px  # Vẽ biểu đồ

# Import các module con
import init_db
import weather_funcs
import db_funcs
import ui_helpers

# Khởi tạo
init_db.create_table()
ui_helpers.setup_page()
ui_helpers.show_header()

# --- SIDEBAR: QUẢN LÝ DANH SÁCH YÊU THÍCH ---
st.sidebar.header("❤️ Thành phố yêu thích")
df_cities = db_funcs.view_all_cities()

if not df_cities.empty:
    # Hiển thị danh sách trong sidebar
    list_city_names = df_cities['city_name'].tolist()
    st.sidebar.write("Danh sách đã lưu:")
    for city in list_city_names:
        st.sidebar.text(f"- {city}")

    st.sidebar.markdown("---")

    # Chức năng Xóa
    city_to_delete = st.sidebar.selectbox("Chọn thành phố để xóa", list_city_names)
    if st.sidebar.button("Xóa khỏi danh sách"):
        db_funcs.delete_city(city_to_delete)
        st.success(f"Đã xóa {city_to_delete}")
        st.rerun()  # Load lại trang ngay lập tức
else:
    st.sidebar.info("Chưa có thành phố nào được lưu.")

# --- MÀN HÌNH CHÍNH (Gồm 2 Tab) ---
tab1, tab2 = st.tabs(["🔍 Tra cứu & Lưu trữ", "📊 Thống kê & So sánh"])

# === TAB 1: TRA CỨU ===
with tab1:
    # input + search
    col1, col2 = st.columns([3, 1])
    with col1:
        city_input = st.text_input("Nhập tên thành phố:", placeholder="Ví dụ: Danang, Paris...")
    with col2:
        st.write("")
        st.write("")
        search_btn = st.button("Xem thời tiết")
    # xử lý kq search
    if search_btn:
        if not city_input:
            st.warning("Vui lòng nhập tên thành phố.")
        else:
            data = weather_funcs.get_weather(city_input)
            if data:
                st.session_state.weather_data = data
            else:
                st.session_state.weather_data = None
                st.error("❌ Không tìm thấy thành phố này.")
    # hiển thị kq và lưu vào database
    if "weather_data" in st.session_state and st.session_state.weather_data:
        data = st.session_state.weather_data
        # Hiển thị kết quả đẹp
        c1, c2, c3 = st.columns(3)
        c1.metric("Thành phố", data['city'])
        c2.metric("Nhiệt độ", f"{data['temp']} °C")
        c3.metric("Độ ẩm", f"{data['humidity']} %")

        st.image(f"http://openweathermap.org/img/wn/{data['icon']}@2x.png")
        st.info(f"Mô tả: {data['description']}")

        # Nút Lưu vào DB
        if st.button(f"❤️ Lưu {data['city']} vào danh sách"):
            saved = db_funcs.add_city(data['city'])
            if saved:
                st.success("Đã lưu thành công!")
                st.rerun()
            else:
                st.warning("Thành phố đã tồn tại hoặc lỗi khi lưu.")
        # else:
        #     st.error("Không tìm thấy thành phố này.")

# === TAB 2: THỐNG KÊ (DASHBOARD) ===
with tab2:
    st.subheader("So sánh thời tiết các thành phố đã lưu")

    if df_cities.empty:
        st.info("Hãy lưu ít nhất 1 thành phố để xem biểu đồ.")
    else:
        if st.button("Cập nhật dữ liệu mới nhất"):
            # Logic: Lấy list tên TP từ DB -> Gọi API cho từng TP -> Gom lại thành bảng mới
            list_names = df_cities['city_name'].tolist()
            report_data = []

            # Thanh tiến trình (Progress bar) cho chuyên nghiệp
            my_bar = st.progress(0)

            for i, name in enumerate(list_names):
                info = weather_funcs.get_weather(name)
                if info:
                    report_data.append(info)
                # Cập nhật thanh tiến trình
                my_bar.progress((i + 1) / len(list_names))

            # Chuyển list thành DataFrame để vẽ biểu đồ
            df_report = pd.DataFrame(report_data)

            # 1. Vẽ biểu đồ cột so sánh Nhiệt độ
            st.write("### 🌡️ So sánh Nhiệt độ (°C)")
            fig = px.bar(df_report, x='city', y='temp', color='temp',
                         color_continuous_scale='RdYlBu_r')  # Màu từ Xanh (Lạnh) sang Đỏ (Nóng)
            st.plotly_chart(fig, use_container_width=True)

            # 2. Hiển thị bảng chi tiết
            st.write("### 📋 Bảng dữ liệu chi tiết")
            st.dataframe(df_report)

            # 3. Nút Export Excel/CSV
            csv = ui_helpers.convert_df_to_csv(df_report)
            st.download_button(
                label="📥 Tải báo cáo về máy",
                data=csv,
                file_name='thoi_tiet_yeu_thich.csv',
                mime='text/csv',
            )