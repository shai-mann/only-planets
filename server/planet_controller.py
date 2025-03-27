import random
import uuid
from typing import Dict, Optional, List


class PlanetController:
    def __init__(self):
        # Store planets as a dictionary with planet_id as key and vote status as value
        self.planets: Dict[int, Optional[bool]] = {}

    def create_planet(self) -> int:
        # Generate a unique planet ID (UUID)
        planet_id = str(uuid.uuid4())

        # Store the planet with no vote (None)
        self.planets[planet_id] = None

        # Return the planet ID, to send back to the client
        return planet_id

    def vote_on_planet(self, planet_id: int, vote: bool) -> bool:
        if planet_id not in self.planets:
            # raise an error if the planet is not found
            raise ValueError("Planet not found")

        # Store the vote
        self.planets[planet_id] = vote

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
                    "vote": self.planets[planet_id],
                }
            )

        # Return the massaged planets
        return massaged_planets
