// class Solution {
//     public int[] solution(int[] numbers) {
//         int[] answer = {};
//         for(int i=0; i<numbers.length; i++){
//             numbers[i]=2*numbers[i];
//         }
//         return numbers;
//     }
// }

import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers){
        return Arrays.stream(numbers).map(i -> i*2).toArray();
    }
}



