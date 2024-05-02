import java.util.Scanner;

public class BasicCalculator {
    public static void main(String[] args) {
        double num1;
        double num2;
        double ans;
        char op;
        Scanner reader = new Scanner(System.in);
        System.out.print("enter two number:");
        num1 = reader.nextDouble();
        num2 = reader.nextDouble();
        System.out.print("\nenter an opertor(+,-,*,/):");
        op = reader.next().charAt(0);
        switch (op) {
            case '+':
                ans = num1 + num2;
                break;
            case '-':
                ans = num1 - num2;
                break;
            case '*':
                ans = num1 * num2;
                break;
            case '/':
                ans = num1 / num2;
                break;
            default:
                System.out.printf("error! enter correct opertor");
                return;
        }
        System.out.print("\n the result is given as follows:\n");
        System.out.printf(num1 + " " + op + " " + num2 + "=" + ans);
    }
}
