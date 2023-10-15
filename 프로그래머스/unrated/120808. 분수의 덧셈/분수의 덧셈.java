class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {0,0};
        int a= 0;
        int b= 0;
        int max=0;
        a=(denom1*numer2)+(numer1*denom2);
        b=(denom1*denom2);
        
        for (int i=1; i<=a && i<=b; i++){
            if(a%i==0 && b%i==0){
                max=i;
            }
        }
        
        answer[0]=a/max;
        answer[1]=b/max;
        
        return answer;
    }
}