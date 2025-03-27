import uuid
from typing import Dict, List


class PlanetController:
    def __init__(self):
        # Store planets as a dictionary with planet_id as key and an object
        # with the planet name, image URL, and vote status as the value
        self.planets: Dict[int, Dict] = {}

    def create_planet(self, planet: Dict) -> int:
        # Generate a unique planet ID (UUID)
        planet_id = str(uuid.uuid4())

        # Store the planet
        self.planets[planet_id] = planet

        # Set the vote to None
        self.planets[planet_id]["vote"] = None

        # Return the planet, to send back to the client, including the vote status and planet ID
        return {**self.planets[planet_id], "id": planet_id}

    def vote_on_planet(self, planet_id: int, vote: bool) -> bool:
        if planet_id not in self.planets:
            # raise an error if the planet is not found
            raise ValueError("Planet not found")

        # Store the vote
        self.planets[planet_id]["vote"] = vote

        # Return the planet, to send back to the client, including the vote status
        return self.planets[planet_id]

    def get_all_planets(self) -> List[Dict]:
        # Massaged is a term for the process of transforming data into a new format.
        # Here, we're transforming the planets dictionary into a list of objects,
        # with the planet_id and vote status for each.
        massaged_planets = []

        for planet_id in self.planets:
            # Add it to the list
            massaged_planets.append(
                {
                    "id": planet_id,
                    **self.planets[planet_id],
                }
            )

        # Return the massaged planets
        return massaged_planets
