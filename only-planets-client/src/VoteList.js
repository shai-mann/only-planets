import React from "react";
// This is a component that will display a list of votes we have already made.
const VoteList = ({ planets }) => {
  function getVoteEmoji(vote) {
    if (vote === null) {
      return "🤷‍♂️";
    }

    // This is a ternary operator. It's a way to write an if statement in one line.
    // If the vote is true, return a thumbs up emoji, otherwise return a thumbs down emoji.
    return vote === "true" ? "👍" : "👎";
    // Since the data is in JSON, the booleans are stored as "true" and "false".
  }

  return (
    <div>
      <h2>Past Votes</h2>
      <ul>
        {planets.map((planet) => (
          <li key={planet.id}>
            {planet.name}: {getVoteEmoji(planet.vote)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default VoteList;
