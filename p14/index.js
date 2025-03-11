import express from "express";
import axios from "axios";
import bodyParser from "body-parser";
import "dotenv/config";
const app = express();
const port = 3000;
const apiUrl = "https://api.openuv.io/api/v1/uv";
const token = process.env.API_KEY_TOKEN;
const config = {
  headers: { "x-access-token": token },
};

app.use(bodyParser.urlencoded({ extended: true }));
app.get("/", async (req, res) => {
  res.render("index.ejs");
});

app.post("/", async (req, res) => {
  const latitude = req.body.lat;
  const longitude = req.body.lng;
  const date = new Date(`${req.body.date}T00:00:00.000Z`);
  try {
    const result = await axios.get(
      `${apiUrl}?lat=${latitude}&lng=${longitude}&dt=:${date}`,
      config
    );
    const sunInfo = result.data.result.sun_info.sun_times;
    function indianTimeZoneCon(time) {
      const dateTimeOptions = {
        timeZone: "Asia/Kolkata",
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: true,
      };
      const UtcTime = new Date(time);
      const istTime = UtcTime.toLocaleString("en-IN", dateTimeOptions);
      return istTime;
    }
    res.render("index.ejs", {
      sunrise: indianTimeZoneCon(sunInfo.sunrise),
      sunset: indianTimeZoneCon(sunInfo.sunset),
    });
  } catch (error) {
    console.log(error.response.data);
    res.status(500).send(error.response.data);
  }
});

app.listen(port, () => {
  console.log(`app started listening on port ${port}`);
});
