"""
=========================================================
E-COMMERCE SALES ANALYTICS DASHBOARD
=========================================================

Author  : Aftab Ahmad Khan
Project : End-to-End Data Engineering Project
Tool    : Streamlit
Database: PostgreSQL

Description
-----------
This dashboard connects to PostgreSQL database and displays:

1. Dataset Preview
2. Total Sales KPI
3. Total Profit KPI
4. Top 5 Products
5. Top Customers
6. Monthly Revenue Trend
7. Region-wise Sales
8. City-wise Sales

=========================================================
"""

# =======================================================
# IMPORT LIBRARIES
# =======================================================

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


# =======================================================
# PAGE CONFIGURATION
# =======================================================

st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


# =======================================================
# CUSTOM CSS STYLING
# =======================================================

st.markdown("""
<style>

/* Main Background */
.main {
    background-color: #f5f7fa;
}

/* Dashboard Title */
.dashboard-title {
    font-size: 40px;
    font-weight: bold;
    color: #1f2937;
    padding-bottom: 20px;
}

/* KPI Cards */
.kpi-card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    text-align: center;
}

.kpi-title {
    font-size: 18px;
    color: gray;
}

.kpi-value {
    font-size: 32px;
    font-weight: bold;
    color: #111827;
}

/* Section Heading */
.section-header {
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 10px;
    color: #111827;
}

</style>
""", unsafe_allow_html=True)


# =======================================================
# DATABASE CONNECTION
# =======================================================

username = 'postgres'
password = 'postgrey123'
host = 'localhost'
port = '5432'
database = 'ecommerce_db'

engine = create_engine(
    f'postgresql://{username}:{password}@{host}:{port}/{database}'
)


# =======================================================
# LOAD DATA
# =======================================================

query = "SELECT * FROM sales"

df = pd.read_sql(query, engine)


# =======================================================
# DATA PREPARATION
# =======================================================

# Convert order date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Remove null values
df = df.dropna()


# =======================================================
# DASHBOARD TITLE
# =======================================================

st.markdown(
    '<div class="dashboard-title">📊 E-Commerce Sales Analytics Dashboard</div>',
    unsafe_allow_html=True
)


# =======================================================
# KPI SECTION
# =======================================================

total_sales = df['sales'].sum()
total_profit = df['profit'].sum()
total_orders = df['order_id'].nunique()
total_customers = df['customer_name'].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Sales</div>
        <div class="kpi-value">₹ {total_sales:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Profit</div>
        <div class="kpi-value">₹ {total_profit:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Orders</div>
        <div class="kpi-value">{total_orders}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Customers</div>
        <div class="kpi-value">{total_customers}</div>
    </div>
    """, unsafe_allow_html=True)


# =======================================================
# DATASET PREVIEW
# =======================================================

st.markdown(
    '<div class="section-header">Dataset Preview</div>',
    unsafe_allow_html=True
)

st.dataframe(df.head(10), use_container_width=True)


# =======================================================
# CHART SECTION 1
# =======================================================

col1, col2 = st.columns(2)

# -------------------------------------------------------
# REGION-WISE SALES
# -------------------------------------------------------

with col1:

    st.markdown(
        '<div class="section-header">Region-wise Sales</div>',
        unsafe_allow_html=True
    )

    region_sales = (
        df.groupby('region')['sales']
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(region_sales)


# -------------------------------------------------------
# CITY-WISE SALES
# -------------------------------------------------------

with col2:

    st.markdown(
        '<div class="section-header">City-wise Performance</div>',
        unsafe_allow_html=True
    )

    city_sales = (
        df.groupby('city')['sales']
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(city_sales)


# =======================================================
# CHART SECTION 2
# =======================================================

col3, col4 = st.columns(2)

# -------------------------------------------------------
# TOP PRODUCTS
# -------------------------------------------------------

with col3:

    st.markdown(
        '<div class="section-header">Top 5 Best-Selling Products</div>',
        unsafe_allow_html=True
    )

    top_products = (
        df.groupby('product_name')['sales']
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    st.bar_chart(top_products)


# -------------------------------------------------------
# TOP CUSTOMERS
# -------------------------------------------------------

with col4:

    st.markdown(
        '<div class="section-header">Top Customers</div>',
        unsafe_allow_html=True
    )

    top_customers = (
        df.groupby('customer_name')['sales']
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    st.bar_chart(top_customers)


# =======================================================
# MONTHLY REVENUE TREND
# =======================================================

st.markdown(
    '<div class="section-header">Monthly Revenue Trend</div>',
    unsafe_allow_html=True
)

monthly_revenue = (
    df.groupby(df['order_date'].dt.to_period('M'))['sales']
    .sum()
)

monthly_revenue.index = monthly_revenue.index.astype(str)

st.line_chart(monthly_revenue)


# =======================================================
# FOOTER
# =======================================================

st.markdown("---")

st.markdown(
    """
    <center>
    Developed using Python, PostgreSQL, Pandas & Streamlit
    </center>
    """,
    unsafe_allow_html=True
)