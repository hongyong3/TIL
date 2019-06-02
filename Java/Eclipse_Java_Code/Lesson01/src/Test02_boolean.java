
public class Test02_boolean {

	public static void main(String[] args) {
		int n = 10110;
		// 2, 3, .... , sqrt(n)

		boolean isPrime = true;
		for (int i = 2; i*i <= n && isPrime; i++)
			if (n % i == 0)
				isPrime = false;
				System.out.println(n + "은 소수가 아닙니다.");

		if (isPrime)
			System.out.println(n+ "은 소수입니다.");

	}

}
