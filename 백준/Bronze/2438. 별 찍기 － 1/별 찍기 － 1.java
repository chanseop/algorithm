
import java.util.Scanner;
public class Main{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n;
		n= sc.nextInt();
		for(int p=1; p<=n; p++) {
			for(int q=0; q<p; q++) {
			System.out.print("*");
			}
			System.out.println();
		}
		sc.close();
	}

}
