function solution(s) {
    let change =0,zCount=0;
    
    while(s !== "1"){
        change++;
        zCount+=(s.match(/0/g)||"").length;
        s = (s.match(/1/g)).length.toString(2);
    }
    
    return [change,zCount]
}

