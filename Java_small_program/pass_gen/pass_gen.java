package pass_gen;

import java.util.Scanner;

public class pass_gen {
    public Boolean evaluate_password(String password, Boolean show_info) {
        Boolean result = false;
        int password_state = 0b00000;
        // TODO:password_judge
        for (char i : password.toCharArray()) {
            // String 转 char[]\
            // 判断各种字符
            if (Character.isUpperCase(i)) {
                password_state |= 0b10000;
            } else if (Character.isLowerCase(i)) {
                password_state |= 0b01000;
            } else if (Character.isDigit(i)) {
                password_state |= 0b00100;
            } else {
                password_state |= 0b00010;
            }
        }
        if (password.toString().length() >= 8) {
            password_state |= 0b00001;
        }
        if (password_state == 0b11111) {
            if (show_info) {
                System.out.println("Password is in rule");
            }
        } else {
            if (show_info) {
                String prompt = new String();
                prompt = "Password is not in rule,";
                // 打括号保证运算？Java特性
                if ((password_state & 0b00001) == 0) {
                    prompt += "len is not enough,";
                }
                if ((password_state & 0b10000) == 0) {
                    prompt += "no upper char,";
                }
                if ((password_state & 0b01000) == 0) {
                    prompt += "no digit,";
                }
                if ((password_state & 0b00010) == 0) {
                    prompt += "no puctuation,";
                }
                prompt = prompt.substring(0, prompt.length()-1);
                // 
                // 字符串切片！！！！！
                // 
                prompt += ".";
                System.out.println(prompt);
            }
        }
        return result;
    }

    public int generate_password() {
        int result = 0;
        return result;
    }

    public int creat_password() {
        int result = 0;
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String user_input = new String();
        System.out.print("请输入密码>");
        user_input = in.nextLine();
        pass_gen password = new pass_gen();
        password.evaluate_password(user_input, true);
        in.close();
    }
}
