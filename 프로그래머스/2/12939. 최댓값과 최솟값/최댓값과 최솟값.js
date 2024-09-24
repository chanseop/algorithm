function solution(s) {
    var answer = '';
    let numberArr = s.split(" ").map(e=>Number(e));
    numberArr.sort((a,b) => {
        return a-b
    });
    // console.log(numberArr);
    answer = numberArr[0]+" "+numberArr.pop();
    
    return answer;
}