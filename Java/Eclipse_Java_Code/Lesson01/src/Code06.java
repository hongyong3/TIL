
public class Code06 {

	public static void main(String[] args) {
		int [] grades;

		grades = new int[5];	// # define MAX 5

		grades[0] = 100;
		grades[1] = 76;
		grades[2] = 92;
		grades[3] = 95;
		grades[4] = 14;

		for(int i = 0; i < grades.length; i++) {	// 이 위치에 선언된 변수 i의 적용범위 (scope)는 이 for 문에 한정된다.
			System.out.println("Grade " + (i+1) +": "+grades[i]);
		}

	}

}
