package java_lab_one.num_1;
import java.util.Scanner;

public class num_1_StringChip {
    public static void main(String[] args) {
        String user_input = new String();
        String result = new String();
        Scanner in = new Scanner(System.in);
        user_input = in.nextLine();
        in.close();

        int cnt = 0;
        int loc = 0;
        for (char i : user_input.toCharArray()) {
            if (i == ' ') {
                cnt++;
                if (cnt == 2) {
                    loc++;
                    break;
                }
            }
            loc++;

        }
        result = user_input.substring(loc);
        result = result.substring(0, 1).toUpperCase() + result.substring(1, result.length() - 1) + ", ";
        user_input = user_input.substring(0, loc);
        user_input = user_input.substring(0, 1).toLowerCase() + user_input.substring(1);
        result += user_input + '?';
        System.out.println(result);
    }
}
