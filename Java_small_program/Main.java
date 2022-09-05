import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int money_amount = 0;
        Scanner in = new Scanner(System.in);
        System.out.print("请投币>");
        money_amount = in.nextInt();
        if (money_amount >= 10) {
            System.out.println("找零>" + (money_amount - 10));
        } else {
            System.out.println("这些钱无法购买一张票");
        }
        in.close();
    }
}