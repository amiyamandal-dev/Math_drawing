import  { draw } from "../pkg/game_of_life";

const height = 600;
const width = 600;


const canvas = document.getElementById("juliaset");
canvas.height = height;
canvas.width = width;
var ctx = canvas.getContext("2d");
const realInput = document.getElementById('real');
const imaginaryInput = document.getElementById('imaginary');
const renderBtn = document.getElementById('render');


const renderLoop = () =>{
    const real = parseFloat(realInput.value) || 0;
    const imaginary = parseFloat(imaginaryInput.value) || 0;
    draw(ctx, height, width, real, imaginary);
}

renderBtn.addEventListener('click', () => {
    renderLoop();
});

