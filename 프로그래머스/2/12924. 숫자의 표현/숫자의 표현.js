function solution(n) {
    let cnt =0;
    let start =1;
    while(start !== n+1){
        let sum =0;
        for (let i=start; i<=n+1; i++){
            sum+=i
            if(sum===n){
                cnt+=1
                break
            }else if(sum>n){
                break
            }
        }
        start += 1
        
    }
    return cnt;
}