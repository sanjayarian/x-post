import os
import random
import requests
# Hapus import BeautifulSoup karena tidak lagi digunakan untuk ini
# from bs4 import BeautifulSoup 
import google.generativeai as genai
import tweepy
import urllib.parse
import feedparser # Tambahkan import ini

# --- FUNGSI UNTUK SCRAPING (DIPERBARUI DENGAN RSS) ---
def scrape_google_news_sports():
    """Mengambil satu berita olahraga teratas dari Google News RSS Feed untuk Amerika Serikat."""
    # URL RSS Feed untuk Google News seksi olahraga di Amerika Serikat
    rss_url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnpHZ0pKVGlnQVAB?hl=en-US&gl=US&ceid=US:en"
    try:
        # Parsing RSS feed
        news_feed = feedparser.parse(rss_url)

        if not news_feed.entries:
            print("Peringatan: Tidak ada berita yang ditemukan di RSS Feed.")
            return None

        # Mengambil semua judul berita dari feed
        news_titles = [entry.title for entry in news_feed.entries]

        # Memilih satu berita secara acak dari daftar
        selected_news = random.choice(news_titles)
        print(f"Ditemukan {len(news_titles)} berita dari RSS, memilih satu secara acak: {selected_news}")
        return selected_news

    except Exception as e:
        print(f"Error saat mengakses atau parsing RSS Feed: {e}")
        return None

# --- (Sisa kode Anda tidak perlu diubah) ---
