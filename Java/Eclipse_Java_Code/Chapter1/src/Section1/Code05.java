package Section1;

public class Code05 {

	public static void main(String[] args) {
		// declare the array
		int [] grades;		// 배열을 사용하기 위해서는 먼저 이렇게 배열을 선언

		// allocate memory for 5 indices
		grades = new int[5];	// 배열의 크기를 지정하면서 생성한다.
        						// 실제 배열이 만들어지는 시점은 여기
        						// 이 두 라인은 한 라인으로 만들 수 있다.
        						// int[] grades = new int [5];
				
		// assign some values to the array
		grades[0] = 100;	// 배열의 각 칸에 데이터를 저장하고,
		grades[1] = 76;		// 저장된 데이터를 읽기 위해서 []를 사용
		grades[2] = 92;		// 배열이 인덱스는 0부터 시작한다.
		grades[3] = 95;
		grades[4] = 14;

		// print out each value
		System.out.println(grades[0]);
		System.out.println(grades[1]);
		System.out.println(grades[2]);
		System.out.println(grades[3]);
		System.out.println(grades[4]);

	}

}
