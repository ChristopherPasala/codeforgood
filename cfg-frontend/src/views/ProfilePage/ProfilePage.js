import {
  Avatar,
  Card,
  CardHeader,
  makeStyles,
  Typography,
  withStyles,
} from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import classNames from "classnames";
import React, { useEffect, useState } from "react";
import Parallax from "../../components/Parallax";
import { container, title } from "../../assets/jss";
import profile from "../../assets/img/profile.jpg";

// Timeline imports
import Timeline from "@material-ui/lab/Timeline";
import TimelineItem from "@material-ui/lab/TimelineItem";
import TimelineSeparator from "@material-ui/lab/TimelineSeparator";
import TimelineConnector from "@material-ui/lab/TimelineConnector";
import TimelineContent from "@material-ui/lab/TimelineContent";
import TimelineOppositeContent from "@material-ui/lab/TimelineOppositeContent";
import TimelineDot from "@material-ui/lab/TimelineDot";
import Paper from "@material-ui/core/Paper";
import Axios from "axios";
import { useRecoilState } from "recoil";
import { authState } from "../../atoms";
import {
  Redirect,
  useHistory,
} from "react-router-dom/cjs/react-router-dom.min";
//

const WhiteTextTypography = withStyles({
  root: {
    color: "#FFFFFF",
  },
})(Typography);

const useStyles = makeStyles((theme) => ({
  paper: {
    padding: "6px 16px",
    textAlign: "center",
  },
  secondaryTail: {
    backgroundColor: theme.palette.secondary.main,
  },
  container: {
    ...container,
    zIndex: "12",
  },
  profile: {
    textAlign: "center",
    "& img": {
      maxWidth: "160px",
      width: "100%",
      margin: "0 auto",
      transform: "translate3d(0, -50%, 0)",
    },
  },
  description: {
    margin: "1.071rem auto 0",
    maxWidth: "600px",
    color: "#999",
    textAlign: "center !important",
  },
  main: {
    background: "#FFFFFF",
    position: "relative",
    zIndex: "3",
  },
  mainRaised: {
    margin: "-60px 30px 20px",
    borderRadius: "6px",
    boxShadow:
      "0 16px 24px 2px rgba(0, 0, 0, 0.14), 0 6px 30px 5px rgba(0, 0, 0, 0.12), 0 8px 10px -5px rgba(0, 0, 0, 0.2)",
  },
  imgFluid: {
    maxWidth: "100%",
    height: "auto",
  },
  imgRoundedCircle: {
    borderRadius: "50% !important",
  },
  imgRaised: {
    boxShadow:
      "0 5px 15px -8px rgba(0, 0, 0, 0.24), 0 8px 10px -5px rgba(0, 0, 0, 0.2)",
  },
  name: {
    marginTop: "-80px",
  },
  title: {
    ...title,
    display: "inline-block",
    position: "relative",
    marginTop: "30px",
    minHeight: "32px",
    textDecoration: "none",
  },
}));

export default function () {
  const classes = useStyles();
  const imageClasses = classNames(
    classes.imgRaised,
    classes.imgRoundedCircle,
    classes.imgFluid
  );
  const [auth, setAuth] = useRecoilState(authState);
  const history = useHistory();
  const [goals, setGoals] = useState([]);
  const [timeline, setTimeline] = useState([]);
  const [matches, setMatches] = useState([]);

  useEffect(() => {
    Axios.get(`/api/user/${auth.user_id}`).then((res) => {
      if (res.data.status !== "ok") {
        history.push("/demographics");
        return;
      }
      Axios.get(`/api/goals/${auth.user_id}`).then((res) => {
        if (res.data.status !== "ok") {
          history.push("/questionaire");
          return;
        } else {
          setGoals(res.data.goals);
          Axios.get(`/api/timeline/${auth.user_id}`).then((res) => {
            // do stuff with timeline
            setTimeline(res.data.timeline);
          });
          Axios.get(`/api/match/${auth.user_id}`).then((res) => {
            // do stuff with the match data!
            setMatches(res.data.matches);
          });
        }
      });
    });
  }, []);

  return (
    <div>
      {auth.loggedIn ? (
        <div>
          <Parallax small filter image={require("../../assets/img/hero.jpg")}>
            <div
              className={classes.container}
              style={{ marginLeft: "auto", marginRight: "auto" }}
            >
              <WhiteTextTypography
                variant="h3"
                style={{ textAlign: "center", zIndex: "12" }}
              >
                Your Profile
              </WhiteTextTypography>
            </div>
          </Parallax>
          <div className={classNames(classes.main, classes.mainRaised)}>
            <div>
              <div className={classes.container}>
                <Grid container justify="center">
                  <Grid item xs={12} sm={12} md={6}>
                    <div className={classes.profile}>
                      <div>
                        <img src={profile} alt="..." className={imageClasses} />
                      </div>
                      <div className={classes.name}>
                        <h3 className={classes.title}>{auth.name}</h3>
                        <h6>STUDENT</h6>
                      </div>
                    </div>
                  </Grid>
                </Grid>
                <Grid container justify="space-around">
                  <Grid item xs={12} sm={12} md={7}>
                    {/* ---- BEGIN USER TIMELINE ---- */}
                    <h3 className={classes.title}>Timeline</h3>
                    <Timeline align="alternate">
                      {goals.map((goal, i) => {
                        return (
                          <TimelineItem key={i} style={{ textAlign: "center" }}>
                            <TimelineOppositeContent>
                              <Typography variant="body2" color="textSecondary">
                                Age {goal.goalAge}
                              </Typography>
                            </TimelineOppositeContent>
                            <TimelineSeparator>
                              <TimelineDot variant="outlined" color="primary" />
                              <TimelineConnector />
                            </TimelineSeparator>
                            <TimelineContent>
                              <Paper elevation={3} className={classes.paper}>
                                <h4 className={classes.title}>
                                  {goal.goalName}
                                </h4>
                                <p>{`$${timeline[i] || 0}`}</p>
                              </Paper>
                            </TimelineContent>
                          </TimelineItem>
                        );
                      })}
                    </Timeline>
                    {/* ---- END USER TIMELINE ---- */}
                  </Grid>
                  <Grid item xs={12} sm={12} md={5}>
                    <h3 className={classes.title}>Matches</h3>
                    {matches.map((match) => {
                      return (
                        <Card style={{ marginBottom: "0.5rem" }}>
                          <CardHeader
                            avatar={<Avatar>{match[0]}</Avatar>}
                            title={match}
                            subheader="(281)898-2332"
                          />
                        </Card>
                      );
                    })}
                  </Grid>
                </Grid>
                <div className={classes.description}>
                  <p>
                    Do not save what is left after spending, but spend what is
                    left after saving. – Warren Buffett
                  </p>
                </div>
                <br /> <br />
              </div>
            </div>
          </div>
        </div>
      ) : (
        <Redirect to="/signin" />
      )}
    </div>
  );
}
