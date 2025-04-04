import "./App.css";
import React, { useState, useEffect } from "react";
import VoteList from "./VoteList";

// This is the URL of the API we are using to fetch the planet data
const API_URL = "http://localhost:8080";

function App() {
  // This is a state variable that will store the planet object
  // When there is no planet, it will be null
  const [planet, setPlanet] = useState(null);

  // These are the planets that the user has generated
  const [planetsList, setPlanetsList] = useState([]);

  // This function fetches the planet data from the API
  // It's "async", because it isn't instantaneous. While the API call is happening,
  // we still want to be able to do other things, so we tell React the function is async.
  async function fetchPlanet() {
    // We use the await keyword to wait for asynchronous operations to complete.
    const response = await fetch(API_URL + "/planet");
    const data = await response.json();

    // Once we have the data, we update the state variable with the new data.
    setPlanet(data.planet);
  }

  // This is a useEffect hook, which will run the code inside it when the component is "mounted"
  // A component is mounted when it is created and added to the page (sometimes called the DOM).
  useEffect(() => {
    fetchPlanet();
  }, []);

  /* Voting Logic */

  function handleVote(vote) {
    // Notice that we don't await this fetch - we want to vote and get a new planet
    // without waiting for the vote to be processed.
    fetch(`${API_URL}/vote/${planet.id}?vote=${vote}`, {
      method: "POST",
    });

    // Remove current planet
    setPlanet(null);
    // Fetch a new planet
    fetchPlanet();
  }

  /* Planet List Logic */

  useEffect(() => {
    // This is another way to handle asnychronous operations.
    // It's a bit more concise than the async/await syntax.
    // The function passed into the .then() method will be called when the fetch operation is complete.
    // The response is passed into the function as an argument.
    fetch(API_URL + "/planets")
      .then((response) => response.json())
      .then((data) => setPlanetsList(data.planets));

    // This is a dependency array. The useEffect hook will only run when the planet state changes.
    // When empty, it only runs once, when the component is rendered.
    // In this case, it will run every time the planet state changes, so our
    // list should stay up to date.
  }, [planet]);

  return (
    <div className="app-container">
      {/* Title and subtitle */}
      <h1 className="app-title">Only Planets</h1>
      <h2 className="app-subtitle">
        Vote yes if you want to see more of this planet...
      </h2>
      {/* Planet image */}
      {planet !== null && (
        <img src={planet.image} alt={"planet"} className="planet-image" />
      )}
      <p className="planet-name">
        {planet === null ? "Loading..." : planet.name}
      </p>
      {/* Vote buttons */}
      <div className="vote-buttons-container">
        {/* Note that the buttons use the same class - this is allowed! */}
        {/* Note they also use multiple classes - this is also allowed! */}
        <button
          className="vote-button vote-button-yes"
          onClick={() => handleVote(true)}
        >
          Yes
        </button>
        <button
          className="vote-button vote-button-no"
          onClick={() => handleVote(false)}
        >
          No
        </button>
      </div>
      <VoteList planets={planetsList} />
    </div>
  );
}

export default App;
