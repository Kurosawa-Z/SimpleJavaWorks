import java.util.Scanner;

public class DivCalculator{
        public static void main(String [] args) {
        int num1;
        int num2;
        int ans;

        Scanner reader = new Scanner(System.in);
        System.out.println("Hello Fungo");
        System.out.print("Enter First Number; ");
        num1 = reader.nextInt();
        System.out.print("Enter Second; ");
        num2 = reader.nextInt();
        ans = num1 / num2;
        System.out.print("the Answer is: " + ans);

  }
}