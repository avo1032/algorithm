function solution(survey, choices) {
  var answer = "";
  let R = 0;
  let T = 0;
  let C = 0;
  let F = 0;
  let J = 0;
  let M = 0;
  let A = 0;
  let N = 0;

  for (let i = 0; i < survey.length; i++) {
    const score = choices[i];
    const surveyArr = survey[i].split("");
    let addScore = 0;
    let target = "ABC";
    if (score < 4) {
      target = surveyArr[0];
      addScore = 4 - score;
    } else if (score > 4) {
      target = surveyArr[1];
      addScore = score - 4;
    }
    switch (target) {
      case "R":
        R = R + addScore;
        break;
      case "T":
        T = T + addScore;
        break;
      case "C":
        C = C + addScore;
        break;
      case "F":
        F = F + addScore;
        break;
      case "J":
        J = J + addScore;
        break;
      case "M":
        M = M + addScore;
        break;
      case "N":
        N = N + addScore;
        break;
      case "A":
        A = A + addScore;
        break;
    }
  }
  T > R ? (answer += "T") : (answer += "R");
  F > C ? (answer += "F") : (answer += "C");
  M > J ? (answer += "M") : (answer += "J");
  N > A ? (answer += "N") : (answer += "A");

  return answer;
}
const result = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]);
console.log(result);
// 입출력 예
// survey	choices	result
// ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
// ["TR", "RT", "TR"]	[7, 1, 3]	"RCJA"

// choices	뜻
// 1	매우 비동의
// 2	비동의
// 3	약간 비동의
// 4	모르겠음
// 5	약간 동의
// 6	동의
// 7	매우 동의

// 지표 번호	성격 유형
// 1번 지표	라이언형(R), 튜브형(T)
// 2번 지표	콘형(C), 프로도형(F)
// 3번 지표	제이지형(J), 무지형(M)
// 4번 지표	어피치형(A), 네오형(N)

// 선택지	성격 유형 점수
// 매우 비동의	네오형 3점
// 비동의	네오형 2점
// 약간 비동의	네오형 1점
// 모르겠음	어떤 성격 유형도 점수를 얻지 않습니다
// 약간 동의	어피치형 1점
// 동의	어피치형 2점
// 매우 동의	어피치형 3점
