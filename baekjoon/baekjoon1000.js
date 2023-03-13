/* 백준 1000번
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. */

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  input = line.split(" ").map((el) => parseInt(el));
  const A = parseInt(input[0]);
  const B = parseInt(input[1]);

  console.log(A + B);
  rl.close();
  rl.on("close", () => {
    process.exit();
  });
});

// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

// ["1", "2"]
let line = input[0].split(" ");

let a = parseInt(line[0]); // 1
let b = parseInt(line[1]); // 2

console.log(a + b);
