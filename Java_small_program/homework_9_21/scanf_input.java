package homework_9_21;

import java.util.Scanner;

public class scanf_input {
    public static void main(String[] args) {
        int a;
        double b;
        String c = new String();
        Scanner in = new Scanner(System.in);
        System.out.print("Enter an integer:");
        a = in.nextInt();
        System.out.print("Enter a floating point number:");
        b = in.nextDouble();
        System.out.print("Enter your name:");
        c = in.next();
        System.out.println("Hi! "+c+", the sum of "+a+" and "+b+" is "+(a+b));
        in.close();

    }
}
