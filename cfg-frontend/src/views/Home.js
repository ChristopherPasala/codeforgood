import { Button, Divider, makeStyles, Typography } from "@material-ui/core";
import React from "react";
import { useHistory } from "react-router-dom";
import Parallax from "../components/Parallax";
import { container } from "../assets/jss";

const useStyles = makeStyles({
  container: {
    display: "flex",
    flexDirection: "column",
    marginLeft: "auto",
    marginRight: "auto",
    alignItems: "center",
    zIndex: "12",
    color: "#FFFFFF",
    ...container,
  },
  content: {
    padding: "1rem 3rem",
    width: "85%",
    marginTop: "-10%",
    marginLeft: "7.5%",
    background: "#FFFFFF",
    position: "relative",
    zIndex: "3",
    borderRadius: "6px",
    boxShadow:
      "0 16px 24px 2px rgba(0, 0, 0, 0.14), 0 6px 30px 5px rgba(0, 0, 0, 0.12), 0 8px 10px -5px rgba(0, 0, 0, 0.2)",
  },

  fontFace: {
    fontFamily: "oswald",
  },
});

export default function (props) {
  const classes = useStyles();
  const history = useHistory();

  const onJoin = (event) => {
    history.push("/signin");
  };

  return (
    <div>
      <Parallax filter image={require("../assets/img/hero.jpg")}>
        <div className={classes.container}>
          <Typography variant="h3" style={{ textAlign: "center" }}>
            Your Finance Starts <br /> With Us.
          </Typography>
          <br />
          <Button
            onClick={onJoin}
            variant="contained"
            color="primary"
            size="large"
          >
            Join
          </Button>
        </div>
      </Parallax>
      <div className={classes.content}>
        <Typography variant="h3" style={{ textAlign: "center" }}>
          What is MyPath Match?
        </Typography>
        <Divider />
        <Typography content="p">
          In response to the ongoing pandemic and social issues that have
          affected Americans across the nation, we believe that efforts to
          increase empathy will strengthen the bonds of a community.
          Subsequently, our platform MyPath Match encourages users to support
          one another through by:
          <ol>
            <li>
              Matching users based on common traits such as financial goals,
              lifestyle choices, demographics, etc. to encourage members to make
              genuine connections with alumni and other participants.
            </li>
            <li>
              Providing a chat bot to provide users with numerous financial
              resources customised for their needs, including the MyPath
              resources.
            </li>
          </ol>
        </Typography>
        <br />
        <Typography variant="h3" style={{ textAlign: "center" }}>
          The Opportunity
        </Typography>
        <Divider />
        <Typography>
          Reaching youth with financial tools and information as they are
          starting their first jobs gives them a real shot at upward mobility,
          regardless of their zip code. This teachable moment—a first
          paycheck—offers a powerful touchpoint where access to banking, saving
          and credit-building are especially relevant and timely. A growing body
          of research has linked savings behavior to college completion, upward
          economic mobility more broadly, and improved confidence and future
          outlook. What’s more, reaching young people before and as they
          transition into adulthood can prevent the kinds of financial
          challenges facing so many adults in America today, such as damaged
          credit, unmanageable debt and lack of emergency savings. Because
          municipal youth employment programs connect millions of low-income
          youth to their first jobs, they offer a powerful delivery channel to
          combine financial tools and information with those first income
          streams toward making youth jobs not just about income, but about
          upward economic mobility.
        </Typography>
      </div>
    </div>
  );
}
