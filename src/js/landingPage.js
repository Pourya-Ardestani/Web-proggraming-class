"use strict";

// function openWindow(event) {
//   event.stopPropagation();
//   const overlay = document.getElementById('overlay-container');
//   overlay.style.display = (overlay.style.display === 'flex') ? 'none' : 'flex';
// }

// document.addEventListener('click', function(event) {
//   const overlay = document.getElementById('overlay-container');
//   const button = document.getElementById('mobile-frame');

//   if (
//     overlay.style.display === 'flex' &&
//     !overlay.contains(event.target) &&
//     !button.contains(event.target)
//   ) {
//     overlay.style.display = 'none';
//   }
// });


const button = document.getElementById('mobile-frame');
const overlay = document.getElementById('overlay-container');

button.addEventListener('click', function (e) {
  e.stopPropagation();
  if (overlay.style.display === 'flex') {
    overlay.style.display = 'none';
  } else {
    overlay.style.display = 'flex';
  }
});

overlay.addEventListener('click', function (e) {
  e.stopPropagation();
});

document.addEventListener('click', function () {
  overlay.style.display = 'none';
});
