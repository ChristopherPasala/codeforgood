import {
  Button,
  Card,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@material-ui/core";
import Axios from "axios";
import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useRecoilState } from "recoil";
import { authState } from "../../atoms";

export default function () {
  const [goals, setGoals] = useState([]);
  const [auth, setAuth] = useRecoilState(authState);
  const history = useHistory();
  const { register, handleSubmit, reset } = useForm();

  const addGoal = (data) => {
    setGoals([...goals, data]);
    reset();
  };

  const submitGoals = async () => {
    if (goals.length > 0) {
      for (let goal of goals) {
        await Axios.post(`/api/goals/${auth.user_id}`, goal);
      }
      history.push("/profile");
    }
  };

  return (
    <div
      style={{
        margin: "3rem auto",
        padding: "3rem",
        width: "85%",
        borderRadius: "6px",
        boxShadow:
          "0 16px 24px 2px rgba(0, 0, 0, 0.14), 0 6px 30px 5px rgba(0, 0, 0, 0.12), 0 8px 10px -5px rgba(0, 0, 0, 0.2)",
      }}
    >
      <h1>Goals Creation</h1>
      <Grid container justify="space-around">
        <Grid item xs={5}>
          <form onSubmit={handleSubmit(addGoal)}>
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="goal"
              label="Goal Name"
              name="goalName"
              autoFocus
              inputRef={register}
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="goalAmount"
              label="Amount $"
              type="number"
              id="amount"
              inputRef={register}
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="goalAge"
              label="Target Age"
              type="number"
              id="age"
              inputRef={register}
            />
            <Button type="submit" fullWidth variant="contained" color="primary">
              Add Goal +
            </Button>
          </form>
        </Grid>
        <Grid item xs={5}>
          <div
            style={{
              background: "#EEEEEE",
              overflow: "auto",
              maxHeight: "58vh",
              minHeight: "58vh",
            }}
          >
            {goals.map((goal, i) => {
              return (
                <React.Fragment key={i}>
                  <br />
                  <Card style={{ width: "85%", margin: "auto" }}>
                    <CardContent>
                      <Typography color="textSecondary" gutterBottom>
                        Goal
                      </Typography>
                      <Typography variant="h5" component="h2">
                        {goal.goalName}
                      </Typography>
                      <Typography color="secondary">
                        {`$${goal.goalAmount}`}
                      </Typography>
                      <Typography variant="body2" component="p">
                        {`By age ${goal.goalAge}`}
                      </Typography>
                    </CardContent>
                  </Card>
                  <br />
                </React.Fragment>
              );
            })}
          </div>
        </Grid>
      </Grid>
      <br /> <br />
      <Button
        fullWidth
        variant="contained"
        color="primary"
        onClick={submitGoals}
      >
        Finish
      </Button>
      <div></div>
    </div>
  );
}
