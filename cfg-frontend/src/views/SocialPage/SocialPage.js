import { makeStyles } from "@material-ui/core";
import classNames from "classnames";
import React, { useEffect, useState } from "react";
import Parallax from "../../components/Parallax";
import { container, title } from "../../assets/jss";
import Feed from "./Feed";

const useStyles = makeStyles({
  container: {
    ...container,
    margin: "auto",
    padding: "3rem",
  },
  main: {
    background: "#FFFFFF",
    position: "relative",
    zIndex: "3",
  },
  mainRaised: {
    margin: "-60px 30px 0px",
    borderRadius: "6px",
    boxShadow:
      "0 16px 24px 2px rgba(0, 0, 0, 0.14), 0 6px 30px 5px rgba(0, 0, 0, 0.12), 0 8px 10px -5px rgba(0, 0, 0, 0.2)",
  },
});

export default function () {
  const classes = useStyles();
  const [feed, setFeed] = useState([]);

  useEffect(() => {
    setFeed([
      {
        user: "John",
        content: "I DID THIS TODAY! HOORAY!",
      },
      {
        user: "John",
        content: "I DID THIS TODAY! HOORAY!",
      },
      {
        user: "John",
        content: "I DID THIS TODAY! HOORAY!",
      },
      {
        user: "John",
        content: "I DID THIS TODAY! HOORAY!",
      },
    ]);
  }, []);

  return (
    <div>
      <Parallax small filter image={require("../../assets/img/hero.jpg")}>
        <div className={classes.container}>SOCIAL FEED</div>
      </Parallax>
      <div className={classNames(classes.main, classes.mainRaised)}>
        <div className={classes.container}>
          {feed.map((f) => {
            return (
              <>
                <Feed content="TEST" user={{ name: "John" }} />
                <br /> <br />
              </>
            );
          })}
        </div>
      </div>
    </div>
  );
}
