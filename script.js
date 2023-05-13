var swiper = new Swiper(".mySwiper", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 0,
    depth: 100,
    modifier: 2.5,
    slideShadows: false,
  },

  initialSlide: 1,
  spaceBetween: 50.5,
});
var map = L.map("map", {
  center: [-6.9714715,107.6438126, 12],
  zoom: 15,
});

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

L.marker([-6.9714715,107.6438126]).addTo(map)
    .bindPopup('Tempat RW')
    .openPopup();


AOS.init({
  duration: 400,
});