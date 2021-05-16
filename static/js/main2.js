const animateCSS = (element, animation, prefix = 'animate__') =>
  // We create a Promise and return it
  new Promise((resolve, reject) => {
    const animationName = `${prefix}${animation}`;
    const node = document.querySelector(element);

    node.classList.add(`${prefix}animated`, animationName,"animate__repeat-2");

    // When the animation ends, we clean the classes and resolve the Promise
    function handleAnimationEnd(event) {
      event.stopPropagation();
      node.classList.remove(`${prefix}animated`, animationName,"animate__repeat-2");
      resolve('Animation ended');
    }

    node.addEventListener('animationend', handleAnimationEnd, {once: true});
  });
document.querySelector(".button1").onclick = function () {
    animateCSS('.button1', 'pulse');
    window.location.href = "/18";


};
document.querySelector(".button2").onclick = function () {
    animateCSS('.button2', 'pulse');
    window.location.href = "/45+";


};
document.querySelector(".button3").onclick = function () {
  animateCSS('.button3', 'pulse');
  window.location.href = "https://short.smittal.tech/wabot";


};
document.querySelector(".button4").onclick = function () {
  animateCSS('.button4', 'pulse');
  window.location.href = "https://covid19-twitter.in";


};
console.log("Made by Shubh Mittal")