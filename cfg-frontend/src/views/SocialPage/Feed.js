import {
  Avatar,
  Card,
  CardActions,
  CardContent,
  CardHeader,
  IconButton,
  makeStyles,
} from "@material-ui/core";
import FavoriteIcon from "@material-ui/icons/Favorite";
import React from "react";

const useStyles = makeStyles({
  card: {
    maxWidth: "512px",
    margin: "auto",
  },
});

export default function (props) {
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardHeader
        avatar={<Avatar>{props.user.name}</Avatar>}
        title="NEW POST"
        subheader="September 26, 2020"
      />
      <CardContent>{props.content}</CardContent>
      <CardActions>
        <IconButton>
          <FavoriteIcon />
        </IconButton>
      </CardActions>
    </Card>
  );
}
