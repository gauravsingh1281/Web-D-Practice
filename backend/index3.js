import express from "express";
const app = express();
const port = 3000;

function logger(req, res, next) {
  console.log(`Request method:${req.method} and Request Url :${req.url}`);
  next();
}
app.use(logger);
app.get("/", (req, res) => {
  res.send("hello wrold");
});
app.listen(port, () => {
  console.log("app started");
});
