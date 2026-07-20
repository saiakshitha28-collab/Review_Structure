import pandas as pd
import streamlit as st
import plotly.express as px
from src.processor import extract_review_data

st.set_page_config(page_title="Universal Review Structurizer", layout="wide")
st.title("📦 Universal Review Structurizer & Analytics Engine")

# ------------------------------------------------------------------------------
# Sidebar: Upload & Sample Data Options
# ------------------------------------------------------------------------------
with st.sidebar:
    st.header("📥 Data Input")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    st.divider()
    use_sample = st.checkbox("Use Sample Dataset (For Testing)")

# Pre-packaged sample data for instant testing
SAMPLE_REVIEWS = [
    "The battery on this phone drains in 2 hours. Very disappointed with the purchase.",
    "This dress fits perfectly and the fabric is so soft! Highly recommend.",
    "The blender worked fine for a week but then stopped turning on.",
    "Shampoo scent is great and leaves hair shiny without feeling greasy.",
    "Shoes are way too tight and scratchy on the ankle. Returning them.",
    "Fast delivery and amazing sound quality on these bluetooth earbuds!"
]

# ------------------------------------------------------------------------------
# Data Processing Engine
# ------------------------------------------------------------------------------
df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)
elif use_sample:
    df = pd.DataFrame({"review_body": SAMPLE_REVIEWS})

if df is not None:
    if 'review_body' not in df.columns:
        st.error("❌ CSV missing required column: `review_body`")
    else:
        if st.button("🚀 Process & Analyze Reviews", type="primary"):
            results = []
            progress_bar = st.progress(0)
            
            for idx, row in df.iterrows():
                data = extract_review_data(str(row['review_body']))
                results.append(data)
                progress_bar.progress((idx + 1) / len(df))
            
            extracted_df = pd.DataFrame(results)
            final_df = pd.concat([df.reset_index(drop=True), extracted_df], axis=1)
            
            st.session_state['structured_df'] = final_df
            st.success("Analysis Complete!")

# ------------------------------------------------------------------------------
# Interactive Analytics & Output Dashboard
# ------------------------------------------------------------------------------
if 'structured_df' in st.session_state:
    final_df = st.session_state['structured_df']
    
    st.divider()
    st.subheader("📈 High-Level Executive Metrics")
    
    # 1. KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    total_reviews = len(final_df)
    pos_pct = round((final_df['sentiment'] == 'Positive').mean() * 100, 1) if 'sentiment' in final_df else 0
    top_sector = final_df['domain_sector'].mode()[0] if 'domain_sector' in final_df else "N/A"
    top_attr = final_df['primary_attribute'].mode()[0] if 'primary_attribute' in final_df else "N/A"

    col1.metric("Total Reviews", total_reviews)
    col2.metric("Positive Sentiment %", f"{pos_pct}%")
    col3.metric("Top Domain Sector", top_sector)
    col4.metric("Top Extracted Attribute", top_attr)
    
    st.divider()

    # 2. Visual Analytics Charts
    if 'domain_sector' in final_df.columns and 'sentiment' in final_df.columns:
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            st.markdown("##### Sentiment Breakdown per Sector")
            fig_sector = px.histogram(
                final_df, x="domain_sector", color="sentiment", 
                barmode="group", color_discrete_map={"Positive": "#2ecc71", "Negative": "#e74c3c", "Neutral": "#f39c12"}
            )
            st.plotly_chart(fig_sector, use_container_width=True)
            
        with chart_col2:
            st.markdown("##### Sentiment Distribution")
            fig_pie = px.pie(final_df, names="sentiment", hole=0.4, color="sentiment",
                             color_discrete_map={"Positive": "#2ecc71", "Negative": "#e74c3c", "Neutral": "#f39c12"})
            st.plotly_chart(fig_pie, use_container_width=True)

    # 3. Search & Filter Controls
    st.subheader("🔍 Filter & Search Data")
    f_col1, f_col2, f_col3 = st.columns([1, 1, 2])
    
    with f_col1:
        selected_sector = st.multiselect("Sector:", options=final_df["domain_sector"].unique(), default=final_df["domain_sector"].unique())
    with f_col2:
        selected_sentiment = st.multiselect("Sentiment:", options=final_df["sentiment"].unique(), default=final_df["sentiment"].unique())
    with f_col3:
        search_query = st.text_input("Search Text:", placeholder="e.g. tight, battery, refund...")

    # Apply Filters
    filtered_df = final_df[
        (final_df["domain_sector"].isin(selected_sector)) & 
        (final_df["sentiment"].isin(selected_sentiment))
    ]
    if search_query:
        filtered_df = filtered_df[filtered_df["review_body"].str.contains(search_query, case=False, na=False)]

    st.dataframe(filtered_df, use_container_width=True)
    
    # Export Option
    csv_bytes = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Filtered CSV", data=csv_bytes, file_name='structured_analytics_reviews.csv', mime='text/csv')