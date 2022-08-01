/* 백준 4948번
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.  */


// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });
// const resultAll = [];
// rl.on("line", line => {
//   let N = parseInt(line);
//   let result = 0;
//   if(N===0){
//     rl.close();
//     }
//     rl.on('close', () => {
//         resultAll.forEach(el => {
//             console.log(el);
//         })
//     process.exit();
//     })
//   for(i=N+1; i<=2*N; i++){
//     let boolean = true;
//     for(j=2; j<=i; j++){
//         if(boolean===true && i===j){
//             result++;
//             break;
//         }
//         if(i%j===0){
//             boolean = false;
//             break;
//         }
//     }
//   }
//   resultAll.push(result);
// });

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
const resultAll = [];
rl.on("line", line => {
  let N = parseInt(line);
  if(N===0){
    rl.close();
    }
    rl.on('close', () => {
        resultAll.forEach(el => {
            console.log(el);
        })
    process.exit();
    })
  
  let arr = Array((2*N)+1).fill(true)
  for (let i = 2; i * i <= 2*N; i += 1) {
    if (arr[i]) {
        for (let j = i * i; j <= 2*N; j += i) {
            arr[j] = false;
            }
        }
    }
  arr.fill(false,0,N+1)
  resultAll.push(arr.filter(e => e).length);
});