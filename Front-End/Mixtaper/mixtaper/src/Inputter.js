import React, { useEffect, useState } from "react";
import "./css/Inputter.css";

function Inputter() {
  const [links, setLinks] = useState("");
  const [currLink, setcurrLink] = useState("");
  const [linksJson, setlinksJson] = useState([]);

  const addLink = (e) => {
    e.preventDefault();
    setLinks(links + currLink + "<br>");
  };

  useEffect(() => {
    if(currLink!=""){
      setlinksJson([...linksJson, currLink]);
    }
  }, [links]);

  const mixtape = (e) =>{
    e.preventDefault();
    let jsonReq = {
      "links":linksJson
    }
    
  }
  return (
    <div className="inputter">
      <div className="inputter__inputText">
        <h3>enter your youtube links:</h3>
      </div>
      
        <form className="inputter__inputBox">
        <input
          className="inputBox__editText"
          value={currLink}
          placeholder="Enter links here"
          onChange={(e) => setcurrLink(e.target.value)}
        />
        <button className="inputBox__addButton" onClick={addLink} type="submit">
          <strong>add to mixtape</strong>
        </button>
        </form>
      
      <div className="inputter__mixtape">
        <button className="mixtape__button" onClick={mixtape}>
          <b>mixtape</b>
        </button>
      </div>
      <div className="inputter__linkHistory">
        <p>Links added:</p>
        <p
          className="inputter_links"
          dangerouslySetInnerHTML={{ __html: links }}
        ></p>
      </div>
    </div>
  );
}

export default Inputter;
