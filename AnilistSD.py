import requests
from PIL import Image, ImageDraw, ImageFont
from pystyle import Colorate, Colors

# Define color palette for the visual output
colors = {
    'background': (28, 28, 34),
    'foreground': (255, 255, 255),
    'pink': (255, 105, 180),
    'blue': (70, 130, 180),
}

def fetch_genre_data(username):
    # Query the AniList API to retrieve the user's watched anime genres
    query = """
    query ($username: String) {
      MediaListCollection(userName: $username, type: ANIME) {
        lists {
          entries {
            media {
              id
              genres
            }
          }
        }
      }
    }
    """
    
    response = requests.post(
        'https://graphql.anilist.co',
        json={'query': query, 'variables': {"username": username}}
    )

    if response.status_code != 200:
        print(Colorate.Diagonal(Colors.red_to_white, f"★ Error fetching data: {response.status_code}"))
        return None

    return response.json()

def calculate_simp_percentage(genre_data):
    # Define the set of genres considered "simp"
    simp_genres = {
        'shoujo', 'romance', 'slice of life', 'harem', 
        'reverse harem', 'drama', 'josei', 'school', 'hentai'
    }

    # Flatten all anime entries across lists and count total
    items = [entry for list_ in genre_data['data']['MediaListCollection']['lists'] for entry in list_['entries']]
    total_anime = len(items)

    simp_anime_set = set()  # Track unique simp anime by ID
    simp_genre_counts = {genre: 0 for genre in simp_genres}

    # Check each anime's genres for "simp" ones
    for item in items:
        for genre in item['media']['genres']:
            genre_lower = genre.lower()
            if genre_lower in simp_genres:
                simp_anime_set.add(item['media']['id'])
                simp_genre_counts[genre_lower] += 1

    simp_anime_count = len(simp_anime_set)
    percentage = (simp_anime_count / total_anime * 100) if total_anime > 0 else 0
    return percentage, simp_genre_counts, total_anime, simp_anime_count

def create_stat_image(username, percentage, simp_genre_counts, total_anime, simp_anime_count):
    # Set image size and create the canvas
    img_size = (580, 440)
    img = Image.new('RGBA', img_size, colors['background'])
    draw = ImageDraw.Draw(img)

    # Load fonts for text (fall back to default if unavailable)
    try:
        font_large = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
        font_medium = ImageFont.truetype("DejaVuSans-Bold.ttf", 18)
    except IOError:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()

    # Draw the stats header
    draw.text((20, 20), f"★ {username}'s simp stats ★", fill=colors['pink'], font=font_large)

    # Display simp stats
    draw.text((20, 60), f"• They watched {percentage:.2f}% simp anime", fill=colors['foreground'], font=font_medium)
    draw.text((20, 100), f"• Total anime watched: {total_anime}", fill=colors['foreground'], font=font_medium)
    draw.text((20, 140), f"• Simp anime count: {simp_anime_count}", fill=colors['foreground'], font=font_medium)

    # List genres and their simp counts
    draw.text((20, 180), "• Simp anime by genre:", fill=colors['blue'], font=font_medium)
    y_offset = 220
    for genre, count in simp_genre_counts.items():
        draw.text((40, y_offset), f"- {genre.capitalize()}: {count}", fill=colors['pink'], font=font_medium)
        y_offset += 20

    # Add a watermark to the image
    draw.text((20, img_size[1] - 30), "@planetwiide - github", fill=colors['foreground'], font=font_medium)

    # Save the image with the username in the filename
    img.save(f"{username}_simp_stats.png")

def simp_detector(username):
    # Fetch user's anime genre data and calculate simp-related stats
    genre_data = fetch_genre_data(username)
    if genre_data:
        percentage, simp_genre_counts, total_anime, simp_anime_count = calculate_simp_percentage(genre_data)
        print(Colorate.Diagonal(Colors.red_to_white, f"★ {username} has {percentage:.2f}% 'simp' anime in their watch list."))
        print(Colorate.Diagonal(Colors.red_to_white, "★ Number of 'simp' anime by genre:"))
        for genre, count in simp_genre_counts.items():
            print(Colorate.Diagonal(Colors.red_to_white, f"  - {genre.capitalize()}: {count}"))
        print(Colorate.Diagonal(Colors.red_to_white, f"★ Out of {total_anime} animes, {simp_anime_count} are categorized as 'simp'."))

        # Generate an image with the simp stats
        create_stat_image(username, percentage, simp_genre_counts, total_anime, simp_anime_count)

if __name__ == "__main__":
    username = input(Colorate.Diagonal(Colors.red_to_white, "★ Enter AniList username: "))
    simp_detector(username)
    input()
