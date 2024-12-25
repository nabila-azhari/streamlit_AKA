import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# Definisi kelas Video
class Video:
    def __init__(self, title, category, viewers):
        self.title = title
        self.category = category
        self.viewers = viewers

# Fungsi untuk generate video acak
def generate_random_videos(n):
    categories = ["music", "gaming", "film"]
    videos = []
    for i in range(1, n + 1):
        title = f"Video{i}"
        category = random.choice(categories)
        viewers = random.randint(1000, 1000000)  # Random viewer count
        videos.append(Video(title, category, viewers))
    return videos

# Quick Sort (Pendekatan Rekursif)
def quick_sort(videos):
    if len(videos) <= 1:
        return videos

    pivot = videos[0].viewers
    less_pivot = [x for x in videos[1:] if x.viewers <= pivot]
    greater_pivot = [x for x in videos[1:] if x.viewers > pivot]

    return quick_sort(less_pivot) + [videos[0]] + quick_sort(greater_pivot)

# Selection Sort (Pendekatan Iteratif)
def selection_sort(videos):
    n = len(videos)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if videos[j].viewers > videos[max_idx].viewers:  # Sorting descending
                max_idx = j
        videos[i], videos[max_idx] = videos[max_idx], videos[i]

# Fungsi untuk mengkategorikan video berdasarkan kategori
def categorize_videos(videos):
    music = []
    gaming = []
    film = []

    for video in videos:
        if video.category == "music":
            music.append(video)
        elif video.category == "gaming":
            gaming.append(video)
        else:
            film.append(video)

    return music, gaming, film

# Fungsi untuk sorting dan mengkategorikan video (Rekursif)
def sort_and_categorize_recursive(videos):
    if len(videos) > 0:
        videos_sorted = quick_sort(videos)
        top30 = videos_sorted[:30]
        return categorize_videos(top30)
    else:
        return [], [], []

# Fungsi untuk sorting dan mengkategorikan video (Iteratif)
def sort_and_categorize_iterative(videos):
    selection_sort(videos)
    top30 = videos[:30]
    return categorize_videos(top30)

# Streamlit App
st.title("Visualisasi Perbandingan Sorting Video")

# Input ukuran
input_size = st.number_input("Masukkan ukuran input video:", min_value=10, max_value=5000, value=100, step=10)

# Tombol untuk memproses
if st.button("Proses"):
    videos = generate_random_videos(input_size)

    # Proses Rekursif
    videos_recursive = videos.copy()
    start_time = time.time()
    music_recursive, gaming_recursive, film_recursive = sort_and_categorize_recursive(videos_recursive)
    recursive_time = time.time() - start_time

    # Proses Iteratif
    videos_iterative = videos.copy()
    start_time = time.time()
    music_iterative, gaming_iterative, film_iterative = sort_and_categorize_iterative(videos_iterative)
    iterative_time = time.time() - start_time

    # Menampilkan hasil waktu eksekusi
    st.write(f"Waktu eksekusi Rekursif (Quick Sort): {recursive_time:.5f} detik")
    st.write(f"Waktu eksekusi Iteratif (Selection Sort): {iterative_time:.5f} detik")

    # Membuat grafik perbandingan waktu
    fig, ax = plt.subplots()
    ax.bar(["Rekursif", "Iteratif"], [recursive_time, iterative_time], color=["blue", "red"])
    ax.set_title("Perbandingan Waktu Eksekusi")
    ax.set_ylabel("Waktu (detik)")
    st.pyplot(fig)

