import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "./App.css";
import useMediaQuery from "@material-ui/core/useMediaQuery";
import { createMuiTheme, ThemeProvider } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";

import Header from "./components/Header";
import Home from "./views/Home";
import SignIn from "./views/SignIn";
import SignUp from "./views/SignUp";
import ProfilePage from "./views/ProfilePage/ProfilePage";
import SocialPage from "./views/SocialPage/SocialPage";
import Goals from "./views/QuestionairePage/Goals";
import Demographics from "./views/QuestionairePage/Demographics";
import useScript from "./components/chatbot";
import { RecoilRoot } from "recoil";
import recoilPersist from "recoil-persist";

function App() {
  const prefersDarkMode = useMediaQuery("(prefers-color-scheme: dark)");

  useScript("http://cdn.chatbot.com/widget/plugin.js%27");

  const theme = React.useMemo(
    () =>
      createMuiTheme({
        palette: {
          type: "light",
        },
      }),
    [prefersDarkMode]
  );

  const { RecoilPersist, updateState } = recoilPersist();

  return (
    <RecoilRoot initializeState={updateState}>
      <RecoilPersist />
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Header />
        <Router>
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/signin" exact component={SignIn} />
            <Route path="/signup" exact component={SignUp} />
            <Route path="/profile" exact component={ProfilePage} />
            <Route path="/social" exact component={SocialPage} />
            <Route path="/questionaire" exact component={Goals} />
            <Route path="/demographics" exact component={Demographics} />
          </Switch>
        </Router>
      </ThemeProvider>
    </RecoilRoot>
  );
}

export default App;
