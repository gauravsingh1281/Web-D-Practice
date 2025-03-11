import express from "express";
import axios from "axios";
import bodyParser from "body-parser";

const app = express();
const port = 3000;
const API_URL = "https://secrets-api.appbrewery.com";

const yourBearerToken = "d7244f2d-9195-4b45-8987-9caa99097373";
const config = {
  headers: { Authorization: `Bearer ${yourBearerToken}` },
};

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index.ejs", { content: "Waiting for data..." });
});

app.post("/get-secret", async (req, res) => {
  const searchId = req.body.id;
  try {
    const result = await axios.get(API_URL + "/secrets/" + searchId, config);
    res.render("index.ejs", { content: JSON.stringify(result.data) });
  } catch (error) {
    res.render("index.ejs", { content: JSON.stringify(error.response.data) });
  }
});

app.post("/post-secret", async (req, res) => {
  const SECRET = req.body.secret;
  const SCORE = req.body.score;

  try {
    const result = await axios.post(
      API_URL + "/secrets/",
      {
        secret: SECRET,
        score: SCORE,
      },
      config
    );
    res.render("index.ejs", { content: JSON.stringify(result.data) });
  } catch (error) {
    res.render("index.ejs", { content: JSON.stringify(error.response.data) });
  }
});

app.post("/put-secret", async (req, res) => {
  const searchId = req.body.id;
  const SECRET = req.body.secret;
  const SCORE = req.body.score;
  try {
    const result = await axios.put(
      API_URL + "/secrets/" + searchId,
      {
        secret: SECRET,
        score: SCORE,
      },
      config
    );
    res.render("index.ejs", { content: JSON.stringify(result.data) });
  } catch (error) {
    res.render("index.ejs", {
      content: JSON.stringify(error.response.data),
    });
  }
});

app.post("/patch-secret", async (req, res) => {
  const searchId = req.body.id;
  const SECRET = req.body.secret;
  const SCORE = req.body.score;
  try {
    const result = await axios.patch(
      API_URL + "/secrets/" + searchId,
      {
        secret: SECRET,
        score: SCORE,
      },
      config
    );
    res.render("index.ejs", { content: JSON.stringify(result.data) });
  } catch (error) {
    res.render("index.ejs", {
      content: JSON.stringify(error.response.data),
    });
  }
});

app.post("/delete-secret", async (req, res) => {
  const searchId = req.body.id;
  // TODO 5: Use axios to DELETE the item with searchId from the secrets api servers.
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
