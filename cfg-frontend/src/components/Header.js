import { Button, Link, makeStyles } from "@material-ui/core";
import React from "react";
import { useRecoilState } from "recoil";
import { authState } from "../atoms";

const useStyles = makeStyles({
  // This is no longer necessary with new logo header, but won't touch
  navbar: {
    padding: "0 2rem",
  },

  logoImage: {
    height: "50px",
    paddingLeft: "10px",
    paddingTop: "10px",
  },
});

export default function (props) {
  const classes = useStyles();
  const [auth, setAuth] = useRecoilState(authState);

  const logout = () => {
    setAuth({
      loggedIn: false,
      name: "",
      user_id: null,
    });
  };

  return (
    <div className={classes.navbar}>
      <a href="/">
        <img
          className={classes.logoImage}
          src={require("../assets/img/logo.png")}
          alt="logo"
        />
      </a>
      {auth.loggedIn && (
        <div style={{ float: "right", marginTop: "0.75rem" }}>
          <Button href="/profile">My Profile</Button>
          <Button onClick={logout}>Log out</Button>
        </div>
      )}
    </div>
  );
}
