package homework;

import java.util.Scanner;

public class Hexadecimal_binary {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] hexBits = {"0000", "0001", "0010", "0011",
                            "0100", "0101", "0110", "0111",
                            "1000", "1001", "1010", "1011",
                            "1100", "1101", "1110", "1111"};
        System.out.print("Enter a Hexadecimal string:");
        String user_in = in.nextLine();
        in.close();
        System.out.print("The equivalent binary for hexadecimal"+"\""+user_in+"\""+" is");
        for(char i:user_in.toCharArray()){
            
            System.out.print(" "+hexBits[Integer.parseInt(i+"", 16)]);
        }

    }
}
