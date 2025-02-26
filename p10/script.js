import express from "express";
import ejs from "ejs";
const app = express();
const port = 3000;

let date = new Date();
let dayType = "";
let advice = "";
let weekday = date.getDay();
if (weekday === 0 || weekday === 6) {
  dayType = "the weekend";
  advice = "it's time to have fun!";
} else {
  dayType = "a weekday";
  advice = "it's time to work hard!";
}

app.get("/", (req, res) => {
  res.render("index.ejs", {
    DayType: dayType,
    Advice: advice,
  });
});
app.listen(port, () => {
  console.log(`Server started listening on port ${port}`);
});
