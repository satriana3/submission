import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="RFM Customer Segmentation Dashboard",
    layout="wide"
)

# ===============================
# HEADER
# ===============================
st.markdown(
    """
    <h1 style='text-align: center;'>📊 RFM Customer Segmentation Dashboard</h1>
    <p style='text-align: center; color: gray;'>
    Analisis segmentasi pelanggan berbasis Recency, Frequency, dan Monetary (RFM)
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ===============================
# LOAD DATA (CLOUD SAFE)
# ===============================
@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'rfm_result.csv')
    return pd.read_csv(file_path)

rfm_df = load_data()

# ===============================
# SIDEBAR
# ===============================
st.sidebar.markdown("## ⚙️ Filter Dashboard")

segment_option = st.sidebar.multiselect(
    "Pilih Segment Pelanggan",
    options=rfm_df['Segment'].unique(),
    default=rfm_df['Segment'].unique()
)

filtered_df = rfm_df[rfm_df['Segment'].isin(segment_option)]

st.sidebar.markdown("---")
st.sidebar.markdown("### 📌 Tentang Dashboard")
st.sidebar.write(
    "Dashboard ini menampilkan hasil segmentasi pelanggan "
    "menggunakan metode **RFM (Recency, Frequency, Monetary)** "
    "untuk membantu memahami perilaku dan kontribusi pelanggan."
)

# ===============================
# KPI METRICS
# ===============================
st.subheader("📈 Ringkasan Utama")

col1, col2, col3 = st.columns(3)

col1.metric(
    "👥 Total Customers",
    f"{filtered_df['customer_unique_id'].nunique():,}"
)

col2.metric(
    "💰 Total Revenue",
    f"R$ {filtered_df['monetary'].sum():,.2f}"
)

col3.metric(
    "🔁 Rata-rata Frequency",
    f"{filtered_df['frequency'].mean():.2f}"
)

st.divider()

# ===============================
# VISUALIZATION ROW 1
# ===============================
col_left, col_right = st.columns(2)

# ---- PIE CHART: Segment Distribution
with col_left:
    st.subheader("🧩 Distribusi Segmentasi Pelanggan")

    segment_counts = filtered_df['Segment'].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(
        segment_counts.values,
        labels=segment_counts.index,
        autopct='%1.1f%%',
        startangle=90
    )
    ax1.axis('equal')

    st.pyplot(fig1)

# ---- BARH CHART: Revenue per Segment
with col_right:
    st.subheader("💰 Kontribusi Revenue per Segment")

    revenue_segment = (
        filtered_df.groupby('Segment')['monetary']
        .sum()
        .sort_values()
    )

    fig2, ax2 = plt.subplots()
    bars = ax2.barh(revenue_segment.index, revenue_segment.values)

    for bar in bars:
        ax2.text(
            bar.get_width(),
            bar.get_y() + bar.get_height() / 2,
            f" R$ {bar.get_width():,.0f}",
            va='center'
        )

    ax2.set_xlabel("Total Revenue")
    st.pyplot(fig2)

st.divider()

# ===============================
# VISUALIZATION ROW 2
# ===============================
col_a, col_b = st.columns(2)

# ---- RFM SCORE DISTRIBUTION
with col_a:
    st.subheader("📊 Distribusi RFM Score")

    fig3, ax3 = plt.subplots()
    ax3.hist(filtered_df['RFM_Score'], bins=10)
    ax3.set_xlabel("RFM Score")
    ax3.set_ylabel("Jumlah Pelanggan")

    st.pyplot(fig3)

# ---- INSIGHT BOX
with col_b:
    st.subheader("💡 Insight Otomatis")

    top_segment = revenue_segment.idxmax()
    top_revenue = revenue_segment.max()

    st.success(
        f"""
        **Segmen dengan kontribusi pendapatan terbesar adalah _{top_segment}_.**

        Total pendapatan dari segmen ini mencapai  
        **R$ {top_revenue:,.2f}**, menunjukkan bahwa pelanggan dalam segmen ini
        memiliki nilai bisnis yang sangat tinggi dan perlu dipertahankan.
        """
    )

st.divider()

# ===============================
# DATA PREVIEW
# ===============================
st.subheader("📄 Preview Data RFM (Top 20)")
st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)
