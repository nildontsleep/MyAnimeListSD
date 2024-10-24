import requests
from PIL import Image, ImageDraw, ImageFont
from pystyle import Colorate, Colors

# Define the Dracula color palette for the image output
colors = {
    'background': (40, 42, 54),
    'foreground': (248, 248, 242),
    'comment': (98, 114, 164),
    'cyan': (139, 233, 253),
    'green': (80, 250, 123),
    'orange': (255, 184, 108),
    'pink': (255, 85, 85),
    'purple': (189, 147, 249),
}

def fetch_genre_data(username):
    # Fetch the user's genre data from MyAnimeList
    url = f"https://myanimelist.net/profile/{username}/chart-data.json?type=anime-genre-table"
    response = requests.get(url)

    if response.status_code != 200:
        print(Colorate.Diagonal(Colors.red_to_white, f"★ Error fetching data: {response.status_code}"))
        return None

    return response.json()

def calculate_simp_percentage(genre_data):
    # Define "simp" genres
    simp_genres = {
        'shoujo', 'romance', 'slice of life', 'harem', 
        'reverse harem', 'drama', 'josei', 'school', 'hentai'
    }

    # Extract anime genre data and calculate totals
    items = genre_data.get('items', [])
    total_anime = sum(item['item_count'] for item in items)

    # Track simp anime counts and genres
    simp_anime_count = 0
    simp_genre_counts = {genre: 0 for genre in simp_genres}

    # Count how many "simp" anime by genre
    for item in items:
        genre = item['item'].lower()
        count = item['item_count']
        
        if genre in simp_genres:
            simp_anime_count += count
            simp_genre_counts[genre] += count

    percentage = (simp_anime_count / total_anime * 100) if total_anime > 0 else 0
    return percentage, simp_genre_counts, total_anime, simp_anime_count

def create_stat_image(username, percentage, simp_genre_counts, total_anime, simp_anime_count):
    # Create the canvas for the stats image
    img_width, img_height = 580, 440
    img = Image.new('RGBA', (img_width, img_height), colors['background'])
    draw = ImageDraw.Draw(img)

    # Load fonts, fallback to default if unavailable
    try:
        font_large = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
        font_medium = ImageFont.truetype("DejaVuSans-Bold.ttf", 18)
    except IOError:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()

    # Title of the stats section
    draw.text((20, 20), f"★ {username}'s simp stats ★", fill=colors['cyan'], font=font_large)

    # Main simp stats
    draw.text((20, 60), f"• They watched {percentage:.2f}% simp anime", fill=colors['foreground'], font=font_medium)
    draw.text((20, 100), f"• Total anime watched: {total_anime}", fill=colors['foreground'], font=font_medium)
    draw.text((20, 140), f"• Simp anime count: {simp_anime_count}", fill=colors['foreground'], font=font_medium)

    # Genre-based breakdown of simp anime
    draw.text((20, 180), "• Simp anime by genre:", fill=colors['orange'], font=font_medium)
    
    y_offset = 220
    for genre, count in simp_genre_counts.items():
        draw.text((40, y_offset), f"- {genre.capitalize()}: {count}", fill=colors['comment'], font=font_medium)
        y_offset += 20

    # Watermark
    draw.text((20, img_height - 30), "@planetwiide - github", fill=colors['purple'], font=font_medium)

    # Save the image to the username-specific filename
    img.save(f"{username}_simp_stats.png")

def simp_detector(username):
    # Fetch and calculate simp stats for the given username
    genre_data = fetch_genre_data(username)
    if genre_data:
        percentage, simp_genre_counts, total_anime, simp_anime_count = calculate_simp_percentage(genre_data)
        print(Colorate.Diagonal(Colors.blue_to_purple, f"★ {username} has {percentage:.2f}% 'simp' anime in their watch list."))
        print(Colorate.Diagonal(Colors.blue_to_purple, "★ Simp animes sorted by genre/themes:"))
        for genre, count in simp_genre_counts.items():
            print(Colorate.Diagonal(Colors.blue_to_purple, f"  - {genre.capitalize()}: {count}"))
        print(Colorate.Diagonal(Colors.blue_to_purple, f"★ Out of {total_anime} anime, {simp_anime_count} are categorized as 'simp'."))

        # Generate the stats image
        create_stat_image(username, percentage, simp_genre_counts, total_anime, simp_anime_count)

if __name__ == "__main__":
    username = input(Colorate.Diagonal(Colors.blue_to_purple, "★ Enter MyAnimeList username: "))
    simp_detector(username)
    input()
