/**
 *
 * 당첨 번호	31	10	45	1	6	19	결과
 * 최고 순위 번호	31	0→10	44	1	0→6	25	4개 번호 일치, 3등
 * 최저 순위 번호	31	0→11	44	1	0→7	25	2개 번호 일치, 5등
 *
 * [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
 * [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
 * [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]
 *
 * 1	6개 번호가 모두 일치
 * 2	5개 번호가 일치
 * 3	4개 번호가 일치
 * 4	3개 번호가 일치
 * 5	2개 번호가 일치
 * 6(낙첨)	그 외
 */
function solution(lottos, win_nums) {
  var answer = [];
  let rightNum = 0;
  for (let i = 0; i < lottos.length; i++) {
    win_nums.includes(lottos[i]) ? rightNum++ : rightNum;
  }
  let zeroNum = 0;
  for (let i = 0; i < lottos.length; i++) {
    if (lottos[i] === 0) {
      zeroNum++;
    }
  }
  let bestRank;
  if (rightNum + zeroNum > 1) {
    bestRank = 7 - (rightNum + zeroNum);
  } else {
    bestRank = 6;
  }
  let worstRank;
  if (rightNum > 1) {
    worstRank = 7 - rightNum;
  } else {
    worstRank = 6;
  }

  answer = [bestRank, worstRank];
  return answer;
}