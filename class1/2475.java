package baekjoon;
import java.util.*;
public class no_2475 {
	public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		int a,b,c,d,e,sum;
		a=sc.nextInt();
		b=sc.nextInt();
		c=sc.nextInt();
		d=sc.nextInt();
		e=sc.nextInt();
		sum=((a*a)+(b*b)+(c*c)+(d*d+(e*e)));
		System.out.println(sum%10);
		
		sc.close();
	}
}
