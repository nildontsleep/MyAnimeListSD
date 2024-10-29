![ico](https://github.com/user-attachments/assets/bd6a7a9d-b55c-45a5-baf7-94ac1ed59544)

# 👘 Simp Detector for MyAnimeList & AniList!


**Simp Detector** is a Python tool that identifies the "simp" content in your anime watchlist on either MyAnimeList or AniList. It fetches data using `requests` and outputs colorful statistics, including a visual breakdown of simp genres in your watched anime. Choose your preferred platform and get your simp stats with a detailed breakdown.

![GitHub issues](https://img.shields.io/github/issues/planetwiide/MyAnimeListSD?style=flat-square) 
![GitHub stars](https://img.shields.io/github/stars/planetwiide/MyAnimeListSD?style=flat-square) 
![GitHub license](https://img.shields.io/github/license/planetwiide/MyAnimeListSD?style=flat-square)

---

## 📊 Features

- **Genre-Based Simp Analysis**: Calculates the percentage of "simp" anime in your list.
- **Detailed Genre Breakdown**: Counts and lists simp genres like Romance, Shoujo, Slice of Life, etc.
- **MAL and AniList Support**: Fetch genre data from MyAnimeList or AniList.
- **Image-Based Stats**: Generates a stats image with the Dracula or custom color themes.

## 📈 Statistics

| Metric                          | Value       |
|---------------------------------|-------------|
| **Total Anime Watched**         | `total_anime` |
| **Total 'Simp' Anime**          | `simp_anime_count` |
| **Percentage of 'Simp' Anime**  | `percentage%` |

### 🗂️ Genre Breakdown of 'Simp' Anime

| Genre             | Count |
|-------------------|-------|
| Shoujo            | `count` |
| Romance           | `count` |
| Slice of Life     | `count` |
| Harem             | `count` |
| Reverse Harem     | `count` |
| Drama             | `count` |
| Josei             | `count` |
| School            | `count` |
| Hentai            | `count` |

## 📷 Preview

Check out Simp Detector in action with these sample outputs:

![Preview of Simp Detector Output](https://github.com/user-attachments/assets/cf74767c-650f-4394-85c5-bc5cea002783)
![Sample Analysis](https://github.com/user-attachments/assets/60a37fb2-ac0e-4c13-9a9e-9cfd58da2b83)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/planetwiide/MyAnimeListSD.git
   ```
   
2. **Enter the project directory**:
   ```bash
   cd MyAnimeListSD
   ```
   
3. **Install dependencies**:
   ```bash
   pip install requests pystyle Pillow
   ```

## 🔍 Usage

Run the application for either MyAnimeList or AniList:

- **For MyAnimeList analysis**:
  ```bash
  python MyAnimeListSD.py
  ```
  
- **For AniList analysis**:
  ```bash
  python AniList.py
  ```

Enter your MyAnimeList or AniList username when prompted. The tool will fetch your anime genre data, analyze the simp genres, and generate both text output and a stats image for a visual breakdown.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue for bug reports or feature requests, or submit a pull request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Discover your simp stats and see which genres dominate your watchlist! 😎
