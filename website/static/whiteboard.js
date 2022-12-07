var paintcanvas = document.getElementById("canvas1");
var context = paintcanvas.getContext("2d");
var color = 'black';
var radius = 10;
var isPainting = false;

function setWidth (value) {
  var canvas=document.getElementById("canvas1");
  if (isNumeric(value)) {
    canvas.width=value;
  }
}

function setHeight(value) {
  var canvas=document.getElementById("canvas1");
  if(isNumeric(value)) {
    canvas.height=value;
  }
}

function startPaint() {
  isPainting=true;
}

function endPaint() {
  isPainting=false;
}

function doPaint(x,y) {
  if (isPainting) {
    paintCircle(x,y);
  }
}
function clearCanvas () {
  context.clearRect(0, 0, paintcanvas.width, paintcanvas.height);
}

function paintCircle (x, y) {
    context.beginPath();
    context.arc(x, y, radius, 0, Math.PI * 2, true);
    context.fillStyle = color;
    context.fill();
}

function isNumeric (value) {
  return !isNaN(value);
}

function changeColor(newColor) {
  color=newColor;
}

function resizeBrush(newSize) {
  radius=newSize;
  document.getElementById("sizeOutput").value=newSize
}