package homework_9_21;

import java.util.Scanner;

public class binary_decimal {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int exit = 1;
        System.out.print("Enter a Binary string:");
        String a_binary = in.nextLine();
        in.close();
        for (int i : a_binary.toCharArray()) {
            if (i != '0' && i != '1') {
                System.out.println("Error: Invalid Binary String " + a_binary);
                exit = 0;
                break;
            }
        }
        if (exit == 1) {
            System.out.println(
                    "The equivalent decimal number for binary " + a_binary + " is " + Integer.parseInt(a_binary, 2));
                    // 十进制转2进制！！！
        }
    }
}
