/*
 * Code01.java 
 * Defining and assigning values to fields and local variables.
 */

public class Code01 {

	static int num;

	public static void main(String[] args) {

		int anotherNum = 5;
		num = 2;

		System.out.println(num + anotherNum);

		System.out.println("Num: " + num);

		System.out.println("anotherNum: " + anotherNum);

		System.out.println("Sum: " + num + anotherNum);	// left associativity

		System.out.println("Sum: " + (num + anotherNum));
	}

}
