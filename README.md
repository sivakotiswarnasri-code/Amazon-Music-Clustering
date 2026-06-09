# 🎵 Amazon Music Clustering

## 📌 Project Overview

Amazon Music Clustering is an **Unsupervised Machine Learning** project that groups songs into meaningful clusters based on their audio characteristics. Since manually categorizing millions of songs is difficult, this project uses **K-Means Clustering** to automatically organize songs with similar musical properties.

The clustering is performed using features such as:

* Danceability
* Energy
* Loudness
* Speechiness
* Acousticness
* Instrumentalness
* Liveness
* Valence
* Tempo
* Duration

This project helps identify hidden patterns in music and can support recommendation systems, playlist generation, and music analysis.

---

## 📌 Problem Statement

With millions of songs available on streaming platforms like Amazon Music, manually organizing tracks into genres or categories is impractical.

The goal of this project is to automatically group similar songs based on their audio characteristics using **clustering techniques**. By analyzing patterns in features such as tempo, energy, danceability, and acousticness, songs can be organized into meaningful groups without using predefined labels.

---

## 📂 Dataset Information

**Dataset Name:** `single_genre_artists.csv`

### Dataset Features Used

* `danceability`
* `energy`
* `loudness`
* `speechiness`
* `acousticness`
* `instrumentalness`
* `liveness`
* `valence`
* `tempo`
* `duration_ms`

### Removed Columns

The following columns were removed because they are not useful for clustering:

* `id_songs`
* `name_song`
* `id_artists`
* `release_date`
* `genres`
* `name_artists`

---

## 🛠 Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Streamlit**

---

## ⚙️ Project Workflow

### 1. Data Loading

* Loaded dataset using Pandas
* Checked dataset shape and column information

### 2. Data Cleaning

* Removed duplicate records
* Removed unnecessary text columns
* Converted features into numeric format
* Handled missing values

### 3. Feature Selection

Selected 10 important audio features for clustering.

### 4. Data Scaling

Used **StandardScaler** to normalize the data because K-Means is distance-based and scaling is important.

### 5. Clustering

Applied **K-Means Clustering** to group similar songs.

### 6. Optimal Cluster Selection

Used:

* **Elbow Method**
* **Silhouette Score**

Selected **K = 4** for better interpretability and meaningful music segmentation.

### 7. Cluster Evaluation

Evaluation metrics used:

* **Silhouette Score**
* **Davies-Bouldin Score**

### 8. Visualization

Created:

* Feature Distribution Graphs
* Correlation Heatmap
* Elbow Method Plot
* Silhouette Score Plot
* PCA Cluster Visualization
* Cluster Heatmap

### 9. Final Export

Saved final clustered dataset as:

`amazon_music_clusters.csv`

---

## 📊 Cluster Interpretation

### Cluster 0 — Party / Energetic Tracks

* High energy
* High danceability
* High valence

### Cluster 1 — Rap / Speech-heavy Tracks

* High speechiness
* Spoken-word style songs

### Cluster 2 — Instrumental Tracks

* High instrumentalness
* Instrument-focused songs

### Cluster 3 — Acoustic / Chill Tracks

* High acousticness
* Low energy
* Calm music

---

## 💼 Business Use Cases

### Personalized Playlist Curation

Automatically group similar songs for better playlist recommendations.

### Improved Song Discovery

Recommend similar tracks based on listening behavior.

### Artist Analysis

Identify competing songs and similar musical styles.

### Market Segmentation

Analyze listening preferences for recommendation optimization.

---

## 📈 Project Evaluation Metrics

| Metric               | Description                 |
| -------------------- | --------------------------- |
| Silhouette Score     | Measures cluster quality    |
| Davies-Bouldin Index | Measures cluster separation |
| PCA Visualization    | Helps visualize clusters    |
| Cluster Balance      | Checks cluster distribution |

---

## 🚀 Streamlit Application

The project includes an interactive **Streamlit Dashboard** with:

* Dataset Preview
* Cluster Distribution
* Cluster Summary
* Cluster Heatmap
* Cluster Filtering
* Cluster Interpretation

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run Streamlit App

```bash
streamlit run app.py
```

---

## 📌 Project Outcome

This project successfully grouped Amazon Music songs into meaningful clusters based on their audio characteristics. The model helps understand music patterns and provides a foundation for recommendation systems and playlist generation.

---

**Author:** Swarna Sri Sivakoti
