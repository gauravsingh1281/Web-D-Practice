import express from "express";
import bodyParser from "body-parser";
import pg from "pg";

const app = express();
const port = 3000;

const db = new pg.Client({
  user: "postgres",
  host: "localhost",
  database: "World",
  password: "1281gaurav",
  port: 5432,
});

db.connect();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", async (req, res) => {
  const result = await db.query("select country_code from visited_countries");
  const response = result.rows;
  let visited_countries = [];
  response.forEach((country) => {
    visited_countries.push(country.country_code);
  });
  res.render("index.ejs", {
    countries: visited_countries,
    total: visited_countries.length,
  });
  db.end();
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
