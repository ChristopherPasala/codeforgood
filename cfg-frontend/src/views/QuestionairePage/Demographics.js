import {
  Button,
  FormControl,
  Grid,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@material-ui/core";
import Axios from "axios";
import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { useRecoilState } from "recoil";
import { authState } from "../../atoms";

export default function () {
  const [gender, setGender] = useState("");
  const [ethnicity, setEthnicity] = useState("");
  const [age, setAge] = useState("");
  const [auth, setAuth] = useRecoilState(authState);
  const history = useHistory();

  const onSubmit = (event) => {
    event.preventDefault();
    const data = { gender, ethnicity, age };
    Axios.post(`/api/user/${auth.user_id}`, data).then((res) => {
      if (res.data.status === "ok") {
        history.push("/questionaire");
      }
    });
  };

  return (
    <div>
      <div
        style={{
          margin: "5rem auto",
          padding: "3rem",
          width: "85%",
          borderRadius: "6px",
          boxShadow:
            "0 16px 24px 2px rgba(0, 0, 0, 0.14), 0 6px 30px 5px rgba(0, 0, 0, 0.12), 0 8px 10px -5px rgba(0, 0, 0, 0.2)",
        }}
      >
        <h1>Demographic Info</h1>
        <Grid container justify="space-around" alignItems="center">
          <Grid item xs={5}>
            <FormControl fullWidth>
              <InputLabel id="gender">Gender</InputLabel>
              <Select
                labelId="gender"
                value={gender}
                onChange={(event) => setGender(event.target.value)}
              >
                <MenuItem value="male">Male</MenuItem>
                <MenuItem value="female">Female</MenuItem>
                <MenuItem value="other">Other</MenuItem>
              </Select>
            </FormControl>
            <br /> <br />
            <FormControl fullWidth>
              <InputLabel id="ethnicity">Ethnicity</InputLabel>
              <Select
                labelId="ethnicity"
                value={ethnicity}
                onChange={(event) => setEthnicity(event.target.value)}
              >
                <MenuItem value="black">Black</MenuItem>
                <MenuItem value="white">White</MenuItem>
                <MenuItem value="hispanic">Hispanic / Latino</MenuItem>
                <MenuItem value="asian">Asian</MenuItem>
                <MenuItem value="native">Native American</MenuItem>
                <MenuItem value="multi">Multi-Racial</MenuItem>
              </Select>
            </FormControl>
            <br />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="age"
              label="Age"
              type="number"
              id="age"
              onChange={(event) => setAge(event.target.value)}
            />
            <br />
            <br />
            <Button
              fullWidth
              variant="contained"
              color="primary"
              onClick={onSubmit}
            >
              Submit
            </Button>
          </Grid>
          <Grid item xs={5}>
            <img
              src={require("../../assets/img/man.png")}
              style={{ width: "50%", height: "50%" }}
            />
          </Grid>
        </Grid>
      </div>
    </div>
  );
}
