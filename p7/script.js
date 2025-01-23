let exploreBtn = document.getElementById("explore");
let showExSublinks = document.getElementById("explore-sublinks");
let hireBtn = document.getElementById("hire-btn");
let showHireSublinks = document.getElementById("hire-sublinks");

// for explore btn sublinks

exploreBtn.addEventListener("mouseover", (e) => {
  showExSublinks.classList.remove("hidden");
  showExSublinks.classList.add("block");
});

exploreBtn.addEventListener("mouseout", (e) => {
  showExSublinks.classList.remove("block");
  showExSublinks.classList.add("hidden");
});
// showExSublinks.addEventListener("mouseout", (e) => {
//   showExSublinks.classList.remove("block");
//   showExSublinks.classList.add("hidden");
// });

// for Hire btn sublinks
hireBtn.addEventListener("mouseover", (e) => {
  showHireSublinks.classList.remove("hidden");
  showHireSublinks.classList.add("block");
});

hireBtn.addEventListener("mouseout", (e) => {
  showHireSublinks.classList.remove("block");
  showHireSublinks.classList.add("hidden");
});
// showHireSublinks.addEventListener("mouseout", (e) => {
//   showHireSublinks.classList.remove("block");
//   showHireSublinks.classList.add("hidden");
// });

// For category btn
let categoryBtn = document.getElementById("category-btn");
let arrowIcon = document.getElementById("arrow-icon");
let showCatSublinks = document.getElementById("category-sublinks");
categoryBtn.addEventListener("click", () => {
  showCatSublinks.classList.toggle("hidden");
  showCatSublinks.classList.toggle("block");
  arrowIcon.classList.toggle("rotate-180");
});
// for fitler btn
let fitlerBtn = document.getElementById("filter-btn");
let showFilterOption = document.getElementById("filter-option");
fitlerBtn.addEventListener("click", () => {
  showFilterOption.classList.toggle("hidden");
  showFilterOption.classList.toggle("block");
});
// For fixed nav bar on scroll

let nav = document.getElementById("nav");
let minScrollPoint = document.getElementById("min-scroll-point");
let searchBar = document.getElementById("search-bar");
let scrollValue = minScrollPoint.offsetTop;

function navFixed() {
  if (window.scrollY > scrollValue) {
    nav.classList.add("fixed", "bg-white", "top-0", "z-20");
    searchBar.classList.remove("hidden");
  } else {
    searchBar.classList.add("hidden");
    nav.classList.remove("fixed", "bg-white", "top-0", "z-20");
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
