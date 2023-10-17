class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int[] count= new int[1001];
        for(int a : array) count[a]+=1;
        
        System.out.print(count[1]);
        
        int top=0;
        
        for (int i=0; i<count.length; i++){
            if (top<count[i]){
                top=count[i];
                answer=i;
            }else if(top==count[i]){
                answer=-1;
            }
        }
        
        return answer;
    }
}

// class Solution {
//     public int solution(int[] array) {
//         int answer = 0;
//         int[] index = new int[1001];
//         int max = Integer.MIN_VALUE;
        
//         for(int i = 0; i < array.length; i++) {
//             index[array[i]]++;
//         }
        
//         for(int i = 0; i < index.length; i++) {
//             if (index[i] > max) {
//                 max = index[i];
//                 answer = i;
//             } else if (max == index[i]) {
//                 answer = -1;
//             }
//         }
//         return answer;
//     }
// }