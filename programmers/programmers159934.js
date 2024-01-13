/**
 * 카드 뭉치
 *
 * 문제설명
 * 코니는 영어 단어가 적힌 카드 뭉치 두 개를 선물로 받았습니다. 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶습니다.
 * 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
 * 한 번 사용한 카드는 다시 사용할 수 없습니다.
 * 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
 * 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.
 * 예를 들어 첫 번째 카드 뭉치에 순서대로 ["i", "drink", "water"], 두 번째 카드 뭉치에 순서대로 ["want", "to"]가 적혀있을 때 ["i", "want", "to", "drink", "water"] 순서의 단어 배열을 만들려고 한다면
 * 첫 번째 카드 뭉치에서 "i"를 사용한 후 두 번째 카드 뭉치에서 "want"와 "to"를 사용하고 첫 번째 카드뭉치에 "drink"와 "water"를 차례대로 사용하면 원하는 순서의 단어 배열을 만들 수 있습니다.
 * 문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal이 매개변수로 주어질 때, cards1과 cards2에 적힌 단어들로 goal를 만들 있다면 "Yes"를, 만들 수 없다면 "No"를 return하는 solution 함수를 완성해주세요.
 *
 * 1 ≤ cards1의 길이, cards2의 길이 ≤ 10
 * 1 ≤ cards1[i]의 길이, cards2[i]의 길이 ≤ 10
 * cards1과 cards2에는 서로 다른 단어만 존재합니다.
 * 2 ≤ goal의 길이 ≤ cards1의 길이 + cards2의 길이
 * 1 ≤ goal[i]의 길이 ≤ 10
 * goal의 원소는 cards1과 cards2의 원소들로만 이루어져 있습니다.
 * cards1, cards2, goal의 문자열들은 모두 알파벳 소문자로만 이루어져 있습니다.
 * 
 * 제한사항
1 ≤ keymap의 길이 ≤ 100
1 ≤ keymap의 원소의 길이 ≤ 100
keymap[i]는 i + 1번 키를 눌렀을 때 순서대로 바뀌는 문자를 의미합니다.
예를 들어 keymap[0] = "ABACD" 인 경우 1번 키를 한 번 누르면 A, 두 번 누르면 B, 세 번 누르면 A 가 됩니다.
keymap의 원소의 길이는 서로 다를 수 있습니다.
keymap의 원소는 알파벳 대문자로만 이루어져 있습니다.
1 ≤ targets의 길이 ≤ 100
1 ≤ targets의 원소의 길이 ≤ 100
targets의 원소는 알파벳 대문자로만 이루어져 있습니다.
 * 
 */

function solution(keymap, targets) {
  const answer = [];
  const keymapJson = {};
  for (let key of keymap) {
    const keyArr = key.split("");
    addKeymap(keymapJson, keyArr);
  }
  for (let target of targets) {
    const targetArr = target.split("");
    let result = 0;
    for (let i = 0; i < targetArr.length; i++) {
      if (!keymapJson[targetArr[i]]) {
        answer.push(-1);
        break;
      }
      result += keymapJson[targetArr[i]];
      if (i === targetArr.length - 1) {
        answer.push(result);
      }
    }
  }
  return answer;
}

function addKeymap(keymapJson, keymap) {
  for (let i = 0; i < keymap.length; i++) {
    if (!!keymapJson[keymap[i]] && keymapJson[keymap[i]] <= i + 1) continue;
    keymapJson[`${keymap[i]}`] = i + 1;
  }
}
