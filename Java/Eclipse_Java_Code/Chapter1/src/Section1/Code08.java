package Section1;
import java.util.Scanner;

public class Code08 {

	public static void main(String[] args) {

		Scanner keyboard = new Scanner(System.in);
		System.out.print("�� ���� ���ڸ� �Է��Ͻðڽ��ϱ�? :");
		int n = keyboard.nextInt();
		System.out.println("���ڸ� �Է��ϼ���.");
		int [] data = new int [n];
		for (int i = 0; i < n; i++)
			data[i] = keyboard.nextInt();
		keyboard.close();

		int sum = 0;
        // int max = 0; ���� �Է¹޴� ���ڰ� ��� ������ �̷��� �ᵵ ������ ������ 
		int max = data[0];	// �Է¹��� ���ڰ� ������� ������ �ֱ� ������ �̷��� ����.
		for ( int i = 0; i < n; i++) {
			sum += data[i];	// sum = sum + data[i];
			if (data[i] > max)
				max = data[i];
		}
		System.out.println("The sum is " + sum);
		System.out.println("The max is " + max);

	}

}