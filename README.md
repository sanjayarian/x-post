# x-posting

## Buat file autopost.yml 

.github/workflows/autopost.yml

## Link API

1. Gemini API : https://aistudio.google.com/apikey
2. x.com API : https://developer.x.com/en/portal/dashboard

## Konfigurasi GitHub Secrets
1. Di repositori GitHub Anda, buka Settings > Secrets and variables > Actions.
2. Klik New repository secret untuk setiap kunci API.
3. Buat secret dengan nama-nama berikut (sesuai yang ada di file .yml dan .py):

            GEMINI_API_KEY
            X_API_KEY
            X_API_SECRET
            X_BEARER_TOKEN
            X_ACCESS_TOKEN
            X_ACCESS_TOKEN_SECRET

Salin dan tempel nilai kunci API Anda ke masing-masing secret.

4. Setelah semua langkah di atas selesai, GitHub Actions akan secara otomatis menjalankan skrip main.py pada jadwal yang telah Anda tentukan di autopost.yml.
