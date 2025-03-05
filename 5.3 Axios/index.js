import express from "express";
import bodyParser from "body-parser";
import axios from "axios";

const app = express();
const port = 3000;

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", async (req, res) => {
  try {
    const response = await axios.get(
      "http://bored.api.lewagon.com/api/activity"
    );
    const result = response.data;
    res.render("index.ejs", { data: result });
  } catch (error) {
    console.error("Failed to make request:", error.message);
    res.render("index.ejs", {
      error: error.message,
    });
  }
});

app.post("/", async (req, res) => {
  const type = req.body.type;
  const participants = req.body.participants;
  try {
    const response = await axios.get(
      `http://bored.api.lewagon.com/api/activity?type=${type}&participants=${participants}`
    );
    const result = response.data;
    res.render("index.ejs", {
      data: result,
    });
  } catch (error) {
    console.error("Failed to make request:", error.message);
    res.render("index.ejs", {
      error: "No activities that match your criteria.",
    });
    console.log(error);
  }
});

app.listen(port, () => {
  console.log(`Server running on port: ${port}`);
});
