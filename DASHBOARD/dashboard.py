import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
hour_df = pd.read_csv("DASHBOARD/all_data.csv")  # Pastikan path benar

# Sidebar
st.sidebar.title("🚴‍♂️ Sharing Bike Dashboard")
analysis_type = st.sidebar.radio("Pilih Analisis:", [
    "📊 Hari Kerja vs Akhir Pekan",
    "⏳ Pola Peminjaman per Jam",
    "🌦️ Pengaruh Cuaca"
])

# 1️⃣ ANALISIS HARI KERJA VS AKHIR PEKAN
if analysis_type == "📊 Hari Kerja vs Akhir Pekan":
    st.title("📊 Hari Kerja vs Akhir Pekan")
    
    # Checkbox buat split casual & registered
    split_type = st.sidebar.checkbox("Pisahkan Casual & Registered")
    
    # Filter data
    workingday_summary = hour_df.groupby("workingday")[["casual", "registered", "count"]].sum()

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    
    if split_type:
        workingday_summary[["casual", "registered"]].plot(kind="bar", stacked=True, ax=ax)
    else:
        workingday_summary["count"].plot(kind="bar", ax=ax, color="red")

    ax.set_xlabel("Kategori Hari")
    ax.set_ylabel("Jumlah Peminjaman")
    ax.set_xticklabels(["Akhir Pekan", "Hari Kerja"], rotation=0)
    ax.set_title("Peminjaman Sepeda: Hari Kerja vs Akhir Pekan")
    ax.legend(["Casual", "Registered"] if split_type else ["Total"])
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    # Show plot
    st.pyplot(fig)

    # Insight Checkbox
    if st.checkbox("Tampilkan Insight 📌"):
        st.write("✅ **Hari kerja lebih ramai dibanding akhir pekan.**")
        st.write("✅ **Registered users lebih dominan di hari kerja.**")

# 2️⃣ POLA PEMINJAMAN PER JAM (FILTER JAM 01-23)
elif analysis_type == "⏳ Pola Peminjaman per Jam":
    st.title("⏳ Pola Peminjaman Sepeda dalam Sehari")

    # Pilihan filter jam (01:00 - 23:00)
    selected_hour = st.sidebar.slider("Pilih Jam (01-23):", 1, 23, 12)

    # Filter data berdasarkan jam yang dipilih
    df_filtered = hour_df[hour_df["hour"] == selected_hour]

    # Jika data tersedia untuk jam yang dipilih
    if not df_filtered.empty:
        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot total peminjaman untuk setiap jam
        sns.lineplot(data=hour_df.groupby("hour")["count"].sum(), marker="o", linewidth=2, label="Total Peminjaman")
        
        # Tandai jam yang dipilih
        sns.scatterplot(x=[selected_hour], y=[df_filtered["count"].sum()], color="red", s=150, label=f"Jam {selected_hour}")

        ax.set_xticks(range(0, 24))
        ax.set_xlabel("Jam")
        ax.set_ylabel("Jumlah Peminjaman")
        ax.set_title(f"Pola Peminjaman Sepeda pada Jam {selected_hour}")
        ax.legend()
        ax.grid(True)

        # Tampilkan plot
        st.pyplot(fig)
    else:
        st.warning(f"Tidak ada data untuk jam {selected_hour}. Silakan pilih jam lain.")

# 3️⃣ PENGARUH CUACA TERHADAP PEMINJAMAN
elif analysis_type == "🌦️ Pengaruh Cuaca":
    st.title("🌦️ Pengaruh Cuaca terhadap Peminjaman")

    # Pilihan filter musim (HANYA untuk Analisis Cuaca)
    season_mapping = {"semi": "Spring", "panas": "Summer", "gugur": "Fall", "dingin": "Winter"}
    selected_season = st.sidebar.selectbox("Pilih Musim:", ["Semua"] + list(season_mapping.values()))

    # Filter data berdasarkan musim
    if selected_season != "Semua":
        season_key = [key for key, value in season_mapping.items() if value == selected_season][0]
        df_filtered = hour_df[hour_df["season"] == season_key]
    else:
        df_filtered = hour_df

    # Grafik Kecepatan Angin vs Peminjaman
    st.subheader("🚴 Kecepatan Angin vs Peminjaman")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x=df_filtered["windspeed"], y=df_filtered["count"], alpha=0.7, ax=ax, color="blue")
    sns.regplot(x=df_filtered["windspeed"], y=df_filtered["count"], scatter=False, color="black", ax=ax)
    ax.set_xlabel("Kecepatan Angin")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title(f"Kecepatan Angin vs Peminjaman ({selected_season})")
    st.pyplot(fig)

    # Grafik Kelembaban vs Peminjaman
    st.subheader("💧 Kelembaban vs Peminjaman")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x=df_filtered["humidity"], y=df_filtered["count"], alpha=0.7, ax=ax, color="purple")
    sns.regplot(x=df_filtered["humidity"], y=df_filtered["count"], scatter=False, color="black", ax=ax)
    ax.set_xlabel("Kelembaban")
    ax.set_ylabel("Jumlah Peminjaman Sepeda")
    ax.set_title(f"Kelembaban vs Peminjaman ({selected_season})")
    st.pyplot(fig)

    # Insight Checkbox
    if st.checkbox("Tampilkan Insight 📌"):
        st.write(f"✅ **Musim yang dipilih: {selected_season if selected_season != 'Semua' else 'Semua Musim'}.**")
