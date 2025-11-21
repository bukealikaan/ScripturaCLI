import requests

base_url = "https://bible-api.com/data/web/random/NT"

def get_random_verse():
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()

        verse_data = data["random_verse"]
        book = verse_data["book"]
        chapter = verse_data["chapter"]
        verse = verse_data["verse"]
        text = verse_data["text"]

        print(f"\nRandom Bible Verse\nBook: {book}\nChapter: {chapter}\nVerse: {verse}\nText: {text}")

if __name__ == "__main__":
    get_random_verse()