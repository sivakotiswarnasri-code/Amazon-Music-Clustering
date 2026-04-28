import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Amazon Music Clustering", layout="wide")

st.title("🎵 Amazon Music Clustering App")

st.write("""
This app shows the clustered songs based on audio features using K-Means clustering.
""")

df = pd.read_csv("amazon_music_clusters.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Cluster Distribution")
cluster_counts = df["Cluster"].value_counts().sort_index()
st.bar_chart(cluster_counts)

st.subheader("Cluster Summary")

features = [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo', 'duration_ms'
]

cluster_summary = df.groupby("Cluster")[features].mean()
st.dataframe(cluster_summary)

st.subheader("Cluster Heatmap")

cluster_summary_scaled = (
    cluster_summary - cluster_summary.min()
) / (cluster_summary.max() - cluster_summary.min())

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(cluster_summary_scaled, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.subheader("Filter Songs by Cluster")

selected_cluster = st.selectbox(
    "Select Cluster",
    sorted(df["Cluster"].unique())
)

filtered_df = df[df["Cluster"] == selected_cluster]

st.write("Total songs in selected cluster:", filtered_df.shape[0])

st.dataframe(filtered_df.head(100))

st.subheader("Cluster Interpretation")

cluster_info = {
    0: "Party / Energetic Tracks – high energy, danceability and valence.",
    1: "Rap / Speech-heavy Tracks – very high speechiness.",
    2: "Instrumental Tracks – very high instrumentalness.",
    3: "Acoustic / Chill Tracks – high acousticness and low energy."
}

st.write(cluster_info.get(selected_cluster, "Cluster information not available."))