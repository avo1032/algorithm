/*
  문제 설명
호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

  제한사항
1 ≤ book_time의 길이 ≤ 1,000
book_time[i]는 ["HH:MM", "HH:MM"]의 형태로 이루어진 배열입니다
[대실 시작 시각, 대실 종료 시각] 형태입니다.
시각은 HH:MM 형태로 24시간 표기법을 따르며, "00:00" 부터 "23:59" 까지로 주어집니다.
예약 시각이 자정을 넘어가는 경우는 없습니다.
시작 시각은 항상 종료 시각보다 빠릅니다.
*/

function solution(book_time) {
  var answer = 1;
  for (let i = 0; i < book_time.length; i++) {
    const start = startToNumber(book_time[i][0]);
    let end = endToNumber(book_time[i][1]) % 100;
    for (let j = 1; j < book_time.length; j++) {
      if (
        startToNumber(book_time[j][0]) >= start &&
        start >= startToNumber(book_time[j][1])
      ) {
        continue;
      }
      if (
        startToNumber(book_time[j][0]) <= end &&
        end <= startToNumber(book_time[j][1])
      ) {
        continue;
      }
      if (
        startToNumber(book_time[j][0]) >= start &&
        end <= startToNumber(book_time[j][1])
      ) {
        continue;
      }
      answer++;
    }
  }
  return answer;
}

function startToNumber(time) {
  return Number(time.replace(":", ""));
}
function endToNumber(time) {
  let end = startToNumber(time);
  if (end / 100 == 50) {
    return end + 50;
  }
  return end;
}

const test = solution([
  ["15:00", "17:00"],
  ["16:40", "18:20"],
  ["14:20", "15:20"],
  ["14:10", "19:20"],
  ["18:20", "21:20"],
]);
console.log(test);
