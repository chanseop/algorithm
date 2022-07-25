package baekjoon;
import java.util.*;
public class no_2739 {
	public static void main(String args[]) {
		Scanner sc= new Scanner(System.in);
		int n;
		int i=1;
		n=sc.nextInt();
		for(i=1; i<10; i++) {
			System.out.println(n+" * "+i+ " = "+n*i);
		}
		sc.close();
	}

}
