var today = new Date();

var day = today.getDate();
var months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
];
var now = new Date();
var thisMonth = months[now.getMonth()]; // getMonth method returns the month of the date (0-January :: 11-December)
var year = today.getFullYear();
var out = document.getElementById("output");

out.innerHTML = thisMonth + " " + day + ", " + year;