# pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("🛒 E-commerce Sales Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])

    # Basic Stats
    st.subheader("📊 Summary Metrics")
    total_sales = df['Total'].sum()
    total_orders = df['OrderID'].nunique()
    total_customers = df['Customer'].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales ($)", f"{total_sales:,.2f}")
    col2.metric("Total Orders", total_orders)
    col3.metric("Unique Customers", total_customers)

    # Sales over time
    st.subheader("📈 Daily Sales Trend")
    sales_trend = df.groupby('Date')['Total'].sum().reset_index()
    st.line_chart(sales_trend.set_index('Date'))

    # Sales by Category
    st.subheader("📊 Sales by Category")
    category_sales = df.groupby('Category')['Total'].sum().sort_values(ascending=False)
    st.bar_chart(category_sales)

    # Pie chart: Category distribution
    st.subheader("🥧 Category Distribution")
    fig, ax = plt.subplots()
    ax.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%')
    ax.axis('equal')
    st.pyplot(fig)

    # Optional: Raw data
    with st.expander("See Raw Data"):
        st.write(df)
else:
    st.info("Please upload a CSV file to see the dashboard.")
