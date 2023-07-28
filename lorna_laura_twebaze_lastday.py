# WEB-SCRAPPING

# pip3 install beautifulsoup4

# URL to scrape: https://xeno-canto.org/

# import libraries
# from bs4 import BeautifulSoup
# import requests

# url = "https://xeno-canto.org/"
# response = requests.get(url)

# Get title of the page
# soup = BeautifulSoup(response.text, 'html.parser')
# title = soup.find('title')
# print(title)


# Assignment A12: Extract all bird species from the website and generate
# the csv or JSON file for the bird species, family and more
# Extract all bird songs from the website https://xeno-canto.org/
# Use the following api to get the data: The endpoint for the webservice is at https://xeno-canto.org/api/2/recordings.
# Extract all bird species from the website and generate the csv or JSON file for the bird species family and more

# without out using API
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


# Get title of the page
def get_webpage_title(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        return title
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    url = "https://xeno-canto.org/"
    webpage_title = get_webpage_title(url)

    if webpage_title:
        print(f"The title of the web page is: {webpage_title}")


def fetch_bird_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        return None


def extract_bird_species(soup):
    bird_species_data = []
    bird_cards = soup.find_all("div", class_="jp-card")

    for bird_card in bird_cards:
        species = bird_card.find("div", class_="jp-x-cname").text.strip()
        family = bird_card.find("div", class_="jp-x-fam").text.strip()

        bird_species_data.append({"Species": species, "Family": family})

    return bird_species_data


def generate_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


def generate_json(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    target_url = "https://xeno-canto.org/"
    website_html = fetch_bird_data(target_url)

    if website_html:
        soup = BeautifulSoup(website_html, "html.parser")
        bird_species_data = extract_bird_species(soup)
        generate_csv(bird_species_data, "bird_species.csv")
        generate_json(bird_species_data, "bird_species.json")
        print("CSV and JSON files generated successfully!")

# With API
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


# Get title of the page
def get_webpage_title(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        return title
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    url = "https://xeno-canto.org/"
    webpage_title = get_webpage_title(url)

    if webpage_title:
        print(f"The title of the web page is: {webpage_title}")


def fetch_website_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data from website. Status code: {response.status_code}")
        return None


def extract_bird_species_from_website(html_content):
    bird_species_data = []
    soup = BeautifulSoup(html_content, "html.parser")
    bird_cards = soup.find_all("div", class_="bird-card")

    for bird_card in bird_cards:
        species = bird_card.find("div", class_="bird-name").text.strip()
        family = bird_card.find("div", class_="bird-family").text.strip()

        bird_species_data.append({"Species": species, "Family": family})

    return bird_species_data


def fetch_bird_songs_from_api():
    url = "https://xeno-canto.org/api/2/recordings"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Error fetching data from Xeno-Canto API. Status code: {response.status_code}"
        )
        return None


def generate_csv_or_json(data, filename, file_format="csv"):
    if file_format == "csv":
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
    elif file_format == "json":
        with open(filename, "w") as json_file:
            json.dump(data, json_file)
    else:
        print("Invalid file format. Please choose 'csv' or 'json'.")


if __name__ == "__main__":
    website_url = "https://xeno-canto.org/"
    website_data = fetch_website_data(website_url)
    bird_species_website_data = extract_bird_species_from_website(website_data)

    bird_songs_api_data = fetch_bird_songs_from_api()

    # Example: Combining both datasets
    combined_data = bird_species_website_data + bird_songs_api_data

    # Generate CSV or JSON file (Choose either 'csv' or 'json')
    generate_csv_or_json(combined_data, "bird_species_data.csv", file_format="csv")
    generate_csv_or_json(combined_data, "bird_species_data.json", file_format="json")

    print("CSV and JSON files generated successfully!")
