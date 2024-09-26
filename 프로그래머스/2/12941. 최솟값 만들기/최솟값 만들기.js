function solution(A,B){
    var answer = 0;
    A.sort((a,b) =>{return a-b;});
    B.sort((a,b) =>{return a-b;});
    
    // console.log(A,B)
    
    let sum =0;
    
    for (let i=0; i<A.length; i++){
        answer += A[i]*B[B.length-i-1]
    }

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    // console.log('Hello Javascript')

    return answer;
}