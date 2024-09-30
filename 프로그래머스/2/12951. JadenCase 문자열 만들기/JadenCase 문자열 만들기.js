function solution(s) {
    var answer = '';
    s = s.toLowerCase();  // 먼저 소문자로 변환

    // 문자열을 공백 기준으로 split 하고, 각 단어별로 처리
    const stringArr = s.split(' ');

    // 각 단어를 순차적으로 처리
    for (let i = 0; i < stringArr.length; ++i) {
        let word = stringArr[i];
        if (word.length > 0) {
            // 첫 문자가 알파벳인 경우에만 대문자로 변환
            word = word[0].toUpperCase() + word.slice(1);
        }
        // 결과에 단어 추가
        answer += word;

        // 마지막 단어가 아닌 경우에는 공백 추가
        if (i !== stringArr.length - 1) {
            answer += ' ';
        }
    }

    return answer;
}
