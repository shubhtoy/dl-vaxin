var date=new Date();
var hours=date.getHours();
var greet;
console.log(hours)
window.onload=function(){
if(hours>-1 && hours<=3){
    greet="evening";
  }
else if (hours<12 && hours!=0){
    greet="morning";
}
else if(hours>=12 && hours <=17){
    greet ="afternoon";
}
else if(hours>17 && hours<=24){
    greet="evening";
}
document.querySelector(".greet").innerHTML="Good "+greet;
document.querySelector(".sun").src=greet+'.png';

};
fetch("https://type.fit/api/quotes")
.then(function (response) {
return response.json();
})
.then(function (myJson) {
var quote=myJson[Math.floor(Math.random() * myJson.length)];
document.querySelector(".actual_quote").innerHTML =quote.text;
document.querySelector(".author").innerHTML = "- "+quote.author;

})
.catch(function (error) {
console.log("Error: " + error);
});
const animateCSS = (element, animation, prefix = 'animate__') =>
  // We create a Promise and return it
  new Promise((resolve, reject) => {
    const animationName = `${prefix}${animation}`;
    const node = document.querySelector(element);

    node.classList.add(`${prefix}animated`, animationName);

    // When the animation ends, we clean the classes and resolve the Promise
    function handleAnimationEnd(event) {
      event.stopPropagation();
      node.classList.remove(`${prefix}animated`, animationName);
      resolve('Animation ended');
    //   node.style.animation=;

    }
    node.addEventListener('animationend', handleAnimationEnd, {once: true});
  });
  document.querySelector(".part1").onclick=function() {
    animateCSS('.part1', 'pulse');
    window.location.href = "/18";

  };
  document.querySelector(".sun").onclick=function() {
    animateCSS('.sun', 'fadeOutDown');
    
  };
  document.querySelector(".part2").onclick=function() {
    animateCSS('.part2', 'pulse');
    window.location.href = "/45+";

  };
  document.querySelector(".part3").onclick=function() {
    animateCSS('.part3', 'pulse');
    window.location.href = "https://coronabeds.jantasamvad.org/";

  };
  document.querySelector(".part4").onclick=function() {
    animateCSS('.part4', 'pulse');
    window.location.href = "https://short.smittal.tech/wabot";

  };
  document.querySelector(".part5").onclick=function() {
    animateCSS('.part5', 'pulse');
    window.location.href = "https://covid19-twitter.in";

  };
  document.querySelector(".name_title").onclick=function() {
    animateCSS('.name_title', 'headShake');
  };
//   document.querySelector(".part3").onclick=function() {
//     document.querySelector('.part3').classList.add('animate__animated','animate__infinite', 'animate__pulse');
// //     ;
//   };
//   document.querySelector(".part4").onclick=function() {
//     document.querySelector('.part4').classList.add('animate__animated','animate__infinite', 'animate__pulse');
// //     ;
//   };
//   document.querySelector(".part5").onclick=function() {
//     document.querySelector('.part5').classList.add('animate__animated','animate__infinite', 'animate__pulse');
// //     ;
//   };
//   document.querySelector(".name_title").onclick=function() {
//     document.querySelector('.name_title').classList.add('animate__animated', 'animate__headShake');
// //     ;
//   };

