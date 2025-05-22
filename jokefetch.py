import requests

def fetch_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            joke = response.json()
            print("Here's a joke for you:")
            print(f"{joke['setup']}")
            print(f"{joke['punchline']}")
        else:
            print(f"Failed to fetch joke. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Run the joke fetcher
if __name__ == "__main__":
    fetch_joke()
