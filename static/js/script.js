const like = document.getElementById('like');

let index = 0;

const colors = ['', 'red'];

like.addEventListener('click', function onClick() {
    like.style.color = colors[index];
    like.style.color = 'white';

    index = index >= colors.length - 1 ? 0 : index + 1;
});