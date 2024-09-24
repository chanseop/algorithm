function solution(s){
    var answer = true;
    let arr = s.split("");
    let queue = []
    // console.log(arr)
    arr.map((e)=>{
        if (e === '('){
            queue.push(e);
        }else{
            if (queue.length !== 0){
                const shiftString = queue.shift();
            }else{
                // 배열에 아무것도 없을때
                answer = false;
            }
        }
    })
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if (queue.length>0){
        answer = false;
    }

    return answer;
}