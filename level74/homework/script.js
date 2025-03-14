// `let` ცვლადის გამოცხადებისთვის გამოიყენება
let title = document.getElementById("title");
let paragraph = document.getElementById("paragraph");

// `textContent` - გამოიყენება HTML ელემენტის ტექსტის შესაცვლელად.
title.textContent = "ახალი სათაური ჯავასკრიპტით!";
paragraph.textContent = "ეს პარაგრაფი შეცვლილია JavaScript-ის მეშვეობით.";

// `getElementById` - აბრუნებს იმ HTML ელემენტს, რომელსაც აქვს მითითებული ID.
console.log("სათაური: ", titleElement.textContent);
console.log("პარაგრაფი: ", paragraphElement.textContent);
