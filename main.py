import requests
from pystyle import Colorate, Center, Colors

def fetch_genre_data(username):
    url = f"https://myanimelist.net/profile/{username}/chart-data.json?type=anime-genre-table"
    response = requests.get(url)

    if response.status_code != 200:
        print(Colorate.Diagonal(Colors.red_to_white, f"★ Error fetching data: {response.status_code}"))
        return None

    return response.json()

def calculate_simp_percentage(genre_data):
    simp_genres = {
        'shoujo', 'romance', 'slice of life', 'harem', 'reverse harem', 
        'drama', 'josei', 'school', 'hentai'
    }

    items = genre_data.get('items', [])
    total_anime = sum(item['item_count'] for item in items)
    
    simp_anime_count = 0
    simp_genre_counts = {genre: 0 for genre in simp_genres}

    for item in items:
        genre = item['item'].lower()
        count = item['item_count']
        
        if genre in simp_genres:
            simp_anime_count += count
            simp_genre_counts[genre] += count

    percentage = (simp_anime_count / total_anime * 100) if total_anime > 0 else 0
    return percentage, simp_genre_counts, total_anime, simp_anime_count

def simp_detector(username):
    genre_data = fetch_genre_data(username)
    if genre_data:
        percentage, simp_genre_counts, total_anime, simp_anime_count = calculate_simp_percentage(genre_data)
        print(Colorate.Diagonal(Colors.blue_to_purple, f"★ {username} has {percentage:.2f}% 'simp' anime in their watch list."))
        print(Colorate.Diagonal(Colors.blue_to_purple, f"★ Number of 'simp' anime by genre:"))
        for genre, count in simp_genre_counts.items():
            print(Colorate.Diagonal(Colors.blue_to_purple, f"  - {genre.capitalize()}: {count}"))
        print()
        print(Colorate.Diagonal(Colors.blue_to_purple, f"★ Out of {total_anime} animes, {simp_anime_count} are categorized as 'simp'."))

if __name__ == "__main__":
    username = input(Colorate.Diagonal(Colors.blue_to_purple, "★ Enter MyAnimeList username: "))
    simp_detector(username)
    input()
