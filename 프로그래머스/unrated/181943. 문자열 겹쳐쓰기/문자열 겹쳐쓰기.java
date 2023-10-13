class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        
        char[] my_arr= my_string.toCharArray();
        char[] overwrite_arr= overwrite_string.toCharArray();
        
        // System.out.println(my_arr);
        // System.out.println(overwrite_arr);
        
        for (int i=0; i<my_arr.length; i++){
            if (s<=i && i<s+overwrite_arr.length){
                my_arr[i]=overwrite_arr[i-s];
                answer+=my_arr[i];
                // System.out.println("@@"+i);
            }else{
                answer+=my_arr[i];
                // System.out.println("!!!"+i);
            }
            
        }
        
        return answer;
    }
}