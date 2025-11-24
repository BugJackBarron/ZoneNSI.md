window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.typesetPromise()
})

var slider = document.getElementById('slider')
var sliderItem = slider.getElementsByTagName('div');
var dots = document.getElementById('dots');
var dotsChild = document.getElementById('dots').getElementsByTagName('li');
for (i = 0; i < sliderItem.length; i++) {
  dots.appendChild(document.createElement('li'));
  dotsChild[i].classList.add('list-inline-item');
  dotsChild[i].setAttribute("id", i);
  dotsChild[i].innerHTML = i;
  dotsChild[0].classList.add('active');
  dotsChild[i].addEventListener("click", runSlider);
}
function runSlider(){
  var dnum = this.getAttribute("id");
  for (i = 0; i < sliderItem.length; i++) {
    sliderItem[i].classList.remove('active');
    sliderItem[dnum].classList.add('active');
    dotsChild[i].classList.remove('active');
    dotsChild[dnum].classList.add('active');
  }
}