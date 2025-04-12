let count = 0;

function counter1() {
    count += 5;
    document.getElementById('count').textContent = count;
}

function counter2() {
    count -= 5;
    document.getElementById('count').textContent = count;
}
