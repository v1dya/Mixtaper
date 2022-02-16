import React from "react";
import "./css/Inputter.css";

function Inputter() {
  return (
    <div className="inputter">
      <div className="inputter__container">
        <div className="inputter__mainBox">
          <p className="inputter__inputLink">enter youtube links:</p>
          <input className="inputter__text" type="text" />
          <button className="inputter__addButton">add to mixtape</button>
        </div>
      </div>
      <div className="converter__container">
        <div className="converter__button">mixtape</div>
      </div>
    </div>
  );
}

export default Inputter;
