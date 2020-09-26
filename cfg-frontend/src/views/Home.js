import {
  Avatar,
  Button,
  Divider,
  Grid,
  makeStyles,
  Typography,
} from "@material-ui/core";
import React from "react";
import { useHistory } from "react-router-dom";
import Parallax from "../components/Parallax";
import { container, title } from "../assets/jss";
import AccessibilityNewIcon from "@material-ui/icons/AccessibilityNew";
import ChatIcon from "@material-ui/icons/Chat";

const useStyles = makeStyles({
  container: {
    ...container,
    marginLeft: "12%",
    alignItems: "center",
    zIndex: "12",
    color: "#FFFFFF",
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
  title: {
    ...title,
    display: "inline-block",
    position: "relative",
    marginTop: "30px",
    marginBottom: "20px",
    minHeight: "32px",
    textDecoration: "none",
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
          <Grid container>
            <Grid item xs={12} sm={12} md={6}>
              <h1
                className={classes.title}
                style={{ color: "white", fontSize: "3rem" }}
              >
                Your Finance Starts With Us.
              </h1>
              <h4>
                Everyone deserves financial freedom, especially the youth. Join
                us to find out more!
              </h4>
              <br />
              <Button
                onClick={onJoin}
                variant="contained"
                color="secondary"
                size="large"
              >
                Join Now
              </Button>
            </Grid>
          </Grid>
        </div>
      </Parallax>
      <div className={classes.content}>
        <div style={{ margin: "auto", maxWidth: "1000px" }}>
          <div style={{ marginBottom: "10rem", textAlign: "center" }}>
            <h2 className={classes.title}>What is MyPath Match?</h2>
            <p>
              In response to the ongoing pandemic and social issues that have
              affected Americans across the nation, we believe that efforts to
              increase empathy will strengthen the bonds of a community.
              Subsequently, our platform MyPath Match encourages users to
              support one another through by:
            </p>
            <br />
            <Grid container justify="space-around" alignContent="center">
              <Grid item xs={12} sm={12} md={5}>
                <Avatar style={{ margin: "auto", backgroundColor: "green" }}>
                  <AccessibilityNewIcon />
                </Avatar>
                <p>
                  Matching users based on common traits such as financial goals,
                  lifestyle choices, demographics, etc. to encourage members to
                  make genuine connections with alumni and other participants.
                </p>
              </Grid>
              <Grid item xs={12} sm={12} md={5}>
                <Avatar style={{ margin: "auto", backgroundColor: "green" }}>
                  <ChatIcon />
                </Avatar>
                <p>
                  Providing a chat bot to provide users with numerous financial
                  resources customised for their needs, including the MyPath
                  resources.
                </p>
              </Grid>
            </Grid>
          </div>
          <div style={{ marginBottom: "10rem" }}>
            <h2 className={classes.title}>Meet the Team</h2>
            <br /> <br />
            <img
              src={require("../assets/img/team.png")}
              style={{ width: "100%" }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}
