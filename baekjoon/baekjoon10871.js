/* 백준 10871번
문제 : 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

입력 : 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
      둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

출력 : X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
 */

// const readline = require("readline");

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// let input = [];
// let result;

// rl.on("line", (line) => {
//   input.push(line);

//   const firstLine = input[0];
//   let X;
//   function lessThanX(value) {
//     return parseInt(value) < X;
//   }
//   if (firstLine) {
//     X = parseInt(firstLine.split(" ")[1]);
//   }
//   const num = input[1];
//   let numArr = [];
//   if (num) {
//     numArr = num.split(" ");
//     // result = (numArr.filter(lessThanX)).map(Number);
//     result = numArr.filter(lessThanX)
//     rl.on("close", () => {
//       console.log(result);
//     });
//   }
// });

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let result = [];
let A = [];
let X;
let N;
rl.on("line", (line) => {
  input.push(line);

  if (input[0]) {
    N = Math.floor(input[0].split(" ")[0]);
    X = Math.floor(input[0].split(" ")[1]);
  }

  if (input[1]) {
    A = input[1].split(" ").map(Number);

    for (let i = 0; i < N; i++) {
      if (A[i] < X) {
        result.push(A[i]);
      }
    }

    console.log(result)
    rl.close();

  }

  rl.on("close", () => {
    process.exit();
  });
});

// rl.on("close", () => {
//   console.log(input);
//   console.log(result.length);
//   process.exit();
// });
