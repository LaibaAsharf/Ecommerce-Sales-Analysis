import streamlit as st
import pandas as pd

# =========================
# LOAD CSS
# =========================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("🛍️ E-Commerce Sales Dashboard")

# =========================
# READ CSV
# =========================

df = pd.read_csv("ecommerce_sales_dashboard_data_with_loss.csv")

# =========================
# SIDEBAR
# =========================

st.sidebar.markdown(
    """
    <div style="
        background-color:#f0f2f6;
        padding:20px;
        border-radius:15px;
        margin-bottom:20px;
        text-align:center;
    ">
        <h2>📊 Dashboard</h2>
        <p>Sales Analysis</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("### 🔍 Filters")
st.sidebar.markdown("---")


city = st.sidebar.multiselect(
    "Select City",
    df["City"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique()
)


# =========================
# APPLY FILTERS
# =========================

filtered_df = df.copy()

if city:
    filtered_df = filtered_df[
        filtered_df["City"].isin(city)
    ]

if category:
    filtered_df = filtered_df[
        filtered_df["Category"].isin(category)
    ]

# =========================
# GRAPH SELECTOR
# =========================

st.subheader("📊 Select a Graph")

graph_choice = st.selectbox(
    "Choose a graph to display:",
    [
        "Sales by City",
        "Sales by Category",
        "Sales by Product",
        "Sales by Customer Type",
        "Profit by Category",
        "Profit by Product",
        "Quantity Sold by Product",
        "Sales vs Profit by Category",
        "Sales by Category & Payment Method",
        "Sales Trend Over Time",
        "Customer Rating by Product"
    ]
)

# =========================
# KPI CALCULATIONS
# =========================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df.loc[
    filtered_df["Profit"] > 0,
    "Profit"
].sum()

total_loss = abs(
    filtered_df.loc[
        filtered_df["Profit"] < 0,
        "Profit"
    ].sum()
)

total_quantity = filtered_df["Quantity"].sum()

total_discount = (
    filtered_df["Unit_Price"]
    * filtered_df["Quantity"]
    * filtered_df["Discount_%"]
    / 100
).sum()

total_orders = filtered_df["Order_ID"].nunique()

# =========================
# KPI CARDS
# =========================

st.subheader("📊 Key Performance Indicators")

kpi_style = """
<style>
.kpi-container {
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #ddd;
    background-color: #f8f9fa;
    text-align: center;
    margin-bottom: 15px;
}

.kpi-title {
    font-size: 16px;
    font-weight: 600;
}

.kpi-value {
    font-size: 25px;
    font-weight: bold;
}
</style>
"""

st.markdown(kpi_style, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="kpi-container">
            <div class="kpi-title">💰 Total Sales</div>
            <div class="kpi-value">Rs. {total_sales:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-container">
            <div class="kpi-title">📈 Total Profit</div>
            <div class="kpi-value">Rs. {total_profit:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="kpi-container">
            <div class="kpi-title">📉 Total Loss</div>
            <div class="kpi-value">Rs. {total_loss:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown(
        f"""
        <div class="kpi-container">
            <div class="kpi-title">📦 Total Quantity</div>
            <div class="kpi-value">{total_quantity:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col5:
    st.markdown(
        f"""
        <div class="kpi-container">
            <div class="kpi-title">🏷️ Total Discount</div>
            <div class="kpi-value">Rs. {total_discount:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col6:
    st.markdown(
        f"""
        <div class="kpi-container">
            <div class="kpi-title">🛒 Total Orders</div>
            <div class="kpi-value">{total_orders:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
# =========================
# DATA TABLE
# =========================

st.subheader("📋 Sales Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# =========================
# GRAPH DISPLAY
# =========================


    #  sales by city

if graph_choice == "Sales by City":

    st.subheader("🏙️ Sales by City")

    city_sales = filtered_df.groupby(
        "City"
    )["Sales"].sum()

    st.bar_chart(city_sales)

    #  sales by category
elif graph_choice == "Sales by Category":

    st.subheader("📊 Sales by Category")

    category_sales = filtered_df.groupby(
        "Category"
    )["Sales"].sum()

    st.bar_chart(category_sales)


       #  sales by  Product

elif graph_choice == "Sales by Product":

    st.subheader("🛍️ Sales by Product")

    product_sales = filtered_df.groupby(
        "Product"
    )["Sales"].sum()

    st.bar_chart(product_sales)



     
        # Sales by Customer Type
elif graph_choice == "Sales by Customer Type":

    st.subheader("👥 Sales by Customer Type")

    customer_type_sales = filtered_df.groupby(
        "Customer_Type"
    )["Sales"].sum()

    st.bar_chart(customer_type_sales)



        # Profit by Category
elif graph_choice == "Profit by Category":

    st.subheader("💰 Profit by Category")

    category_profit = filtered_df.groupby(
        "Category"
    )["Profit"].sum()

    st.bar_chart(category_profit)




    #   Profit by Product
elif graph_choice == "Profit by Product":

    st.subheader("💰 Profit by Product")

    product_profit = filtered_df.groupby(
        "Product"
    )["Profit"].sum()

    st.bar_chart(product_profit)



    #   Quantity Sold by Product
elif graph_choice == "Quantity Sold by Product":

    st.subheader("📦 Quantity Sold by Product")

    product_quantity = filtered_df.groupby(
        "Product"
    )["Quantity"].sum()

    st.bar_chart(product_quantity)




    #   Sales vs Profit by Category
elif graph_choice == "Sales vs Profit by Category":

    st.subheader("📊 Sales vs Profit by Category")

    category_comparison = filtered_df.groupby(
        "Category"
    )[["Sales", "Profit"]].sum()

    st.bar_chart(category_comparison)




    #   Sales by Category & Payment Method
elif graph_choice == "Sales by Category & Payment Method":

    st.subheader("💳 Sales by Category & Payment Method")

    category_payment = filtered_df.groupby(
        ["Category", "Payment_Method"]
    )["Sales"].sum().reset_index()

    st.bar_chart(
        category_payment,
        x="Category",
        y="Sales",
        color="Payment_Method"
    )


    #    Sales Trend Over Time

elif graph_choice == "Sales Trend Over Time":

    st.subheader("📈 Sales Trend Over Time")

    sales_trend = filtered_df.groupby(
        "Date"
    )["Sales"].sum()

    st.line_chart(sales_trend)




    #  Customer Rating by Product
elif graph_choice == "Customer Rating by Product":

    st.subheader("⭐ Customer Rating by Product")

    product_rating = filtered_df.groupby(
        "Product"
    )["Customer_Rating"].mean()

    st.bar_chart(product_rating)

    # target enconding
    import pandas as pd
    df.houses=pd.DataFrame({
        "city": ["lahore","lahore", "lahore",
                 "karachi","karachi","karachi",
                 "Islamabad","Islamabad","Islamabad"],
        "Tatal Sales":        
    })