// For fixed nav bar on scroll

let nav = document.getElementById("nav");
let minScrollPoint = document.getElementById("min-scroll-point");
let searchBar = document.getElementById("search-bar");
let scrollValue = minScrollPoint.offsetTop;

function navFixed() {
  if (window.scrollY > scrollValue) {
    nav.classList.add("fixed", "bg-white", "top-0", "z-10");
    searchBar.classList.remove("hidden");
  } else {
    searchBar.classList.add("hidden");
    nav.classList.remove("fixed", "bg-white", "top-0", "z-10");
  }
}

// For go to top button
let topBtn = document.getElementById("top-btn");

const showTopBtn = () => {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    topBtn.style.display = "block";
  } else {
    topBtn.style.display = "none";
  }
};

const goUp = () => {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
};
window.onscroll = () => {
  showTopBtn();
  navFixed();
};
