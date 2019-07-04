package Section2;

import java.util.Scanner;

public class Code18 {

	public static void main(String[] args) {
		System.out.print("Please enter one integer and Press Enter.");
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		int [] data = new int [a];
		for (int i = 0; i < a; i++)
			data[i] = keyboard.nextInt();
		keyboard.close();

		bubbleSort(a, data);

		System.out.println("Sorted data : ");
		for (int i = 0; i < a; i++)
			System.out.println(data[i]);
	}

	public static void bubbleSort(int a, int [] data) {	
		// bubbleSort�� �ƹ��͵� return �� �ʿ䰡 ����. �׷��� void�� ����Ѵ�.
		for (int i = a - 1; i > 0; i--) {
			for (int j = 0; j < i; j++) {
				if (data[j] > data[j + 1]) {
					int tmp = data[j];
					data[j] = data[j + 1];
					data[j + 1] = tmp;
				}
			}
		}
//		return; // return ���ε� � ���� �������� �ʴ°�. �� �Լ��� �����Ѵ�.
	}
}