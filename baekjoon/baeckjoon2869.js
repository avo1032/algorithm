/* 백준 2869번
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오. */


const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on("line", line => {
  input = line.split(' ').map((el) => parseInt(el));
  const A = parseInt(input[0]);
  const B = parseInt(input[1]);
  const V = parseInt(input[2]);

  const X = Math.floor(V/(A-B))
  const Y = A - B;

  days = ((X - 1) * Y) + A >= V ? X-1 : X+1
  console.log(X);
  console.log(V);


  console.log(days);
  rl.close();
  rl.on('close', () => {
    process.exit();
  })
});