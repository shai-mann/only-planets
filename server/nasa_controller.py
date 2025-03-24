import requests
import random
from typing import Dict


# From testing the NASA API, we know it has 5862 planets in the scope we are searching.
NUM_PLANETS = 5862

# If the exoplanet has no image, we'll use this default image.
# I chose an image of Kepler-22b as our default.
DEFAULT_IMAGE_URL = "https://images-assets.nasa.gov/image/PIA14883/PIA14883~medium.jpg"

# Since a lot of exoplanets don't have images, this list is planets that do have images.
# We'll use this list to randomly select a planet from the list.
PLANETS_WITH_IMAGES = [
    "Kepler-22b",
    "Kepler-16b",
    "Kepler-186f",
    "Kepler-452b",
    "TRAPPIST-1e",
    "TRAPPIST-1f",
    "TRAPPIST-1g",
    "WASP-39b",
    "HD 209458 b",
    "GJ 1214 b",
    "55 Cancri e",
]


def generate_fake_planet_name():
    return random.choice(PLANETS_WITH_IMAGES)


def generate_planet_name_api_request():
    # generate a random planet id
    planet_id = random.randint(0, NUM_PLANETS - 1)

    # generate the URL using the planet id
    # this is using some complex SQL magic, along with Python's f-string formatting,
    # to generate a URL that will fetch the planet data from the NASA API.
    url = f"""https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=
    SELECT pl_name FROM (
        SELECT pl_name, ROW_NUMBER() OVER (ORDER BY pl_name) as rn FROM pscomppars
    ) WHERE rn = {planet_id}&format=json"""

    # remove new line characters (API doesn't like them)
    url = url.replace("\n", "")

    # return the URL
    return url


def generate_planet_image_api_request(planet_name: str):
    # generate the URL for the planet image
    url = f"https://images-api.nasa.gov/search?q={planet_name}&media_type=image"

    # return the URL
    return url


class NASAController:
    def get_random_planet(self) -> Dict:
        try:
            # generate the URL
            # url = generate_planet_name_api_request()

            # # fetch the data for the planet name
            # planet_name = requests.get(url).json()[0]["pl_name"]
            planet_name = generate_fake_planet_name()

            # generate the URL for the planet image
            planet_image_url = generate_planet_image_api_request(planet_name)

            # fetch the data for the planet image
            planet_image_data = requests.get(planet_image_url).json()["collection"][
                "items"
            ]

            if len(planet_image_data) == 0:
                # if there is no image, return the default image
                return {"name": planet_name, "image": DEFAULT_IMAGE_URL}

            # get a random image URL from the data
            planet_image_url = random.choice(planet_image_data[0]["links"])["href"]

            # return the planet data
            return {"name": planet_name, "image": planet_image_url}

        except requests.RequestException as e:
            raise Exception(f"Failed to fetch planet data from NASA: {str(e)}")
