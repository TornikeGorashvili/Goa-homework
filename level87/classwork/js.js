let word = 'hallo';
let user_input = prompt('Enter word: ');
let tries = 0;

while (user_input != word) {
  tries++;
  user_input = prompt('Try again, Enter word: ');
}

alert('success! you did it in ' + tries + ' tries')