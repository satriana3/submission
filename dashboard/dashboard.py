import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="RFM Dashboard", layout="wide")

st.title("📊 RFM Customer Segmentation Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('rfm_result.csv')

rfm_df = load_data()

# Sidebar filter
st.sidebar.header("Filter Segment")
segment_option = st.sidebar.multiselect(
    "Pilih Segment",
    options=rfm_df['Segment'].unique(),
    default=rfm_df['Segment'].unique()
)

filtered_df = rfm_df[rfm_df['Segment'].isin(segment_option)]

# KPI Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", filtered_df['customer_unique_id'].nunique())
col2.metric("Total Revenue", f"R$ {filtered_df['monetary'].sum():,.2f}")
col3.metric("Avg Frequency", f"{filtered_df['frequency'].mean():.2f}")

st.divider()

# Segment Distribution
st.subheader("Distribusi Segmentasi Pelanggan")
segment_counts = filtered_df['Segment'].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(segment_counts.index, segment_counts.values)
ax1.set_ylabel('Jumlah Pelanggan')
ax1.set_xlabel('Segment')
plt.xticks(rotation=45)

st.pyplot(fig1)

# Revenue per Segment
st.subheader("Kontribusi Revenue per Segment")
revenue_segment = filtered_df.groupby('Segment')['monetary'].sum().sort_values()

fig2, ax2 = plt.subplots()
ax2.barh(revenue_segment.index, revenue_segment.values)
ax2.set_xlabel('Total Revenue')

st.pyplot(fig2)

# Data preview
st.subheader("Preview Data RFM")
st.dataframe(filtered_df.head(20))
