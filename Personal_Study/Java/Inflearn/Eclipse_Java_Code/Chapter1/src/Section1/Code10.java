package Section1;

public class Code10 {

	public static void main(String[] args) {
		for (int n = 2; n <= 100; n++) {
			// 2, 3, .... , sqrt(n)
			boolean isPrime = true;
			for (int i = 2; i*i <= n && isPrime; i++)
				if (n % i == 0)
					isPrime = false;
//					System.out.println(n + "�� �Ҽ��� �ƴմϴ�.");
					
			if (isPrime)
				System.out.println(n+ "�� �Ҽ��Դϴ�.");
		}
	}

}
