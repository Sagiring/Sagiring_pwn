package pass_gen;

import java.util.Random;
import java.util.Scanner;

public class pass_gen {

    public String string_type_out(String type) {
        String result = "";
        if(type == "digits"){
        String digits = new String();
        for (int i = 49; i <= 57; i++) {
            digits += (char) i;
        }
        result = digits;
    }else if(type == "uppercase"){
        String uppercase = new String();
        for (int i = 65; i <= 90; i++) {
            uppercase += (char) i;
        }
        result = uppercase;
    }else if(type == "lowercase"){
        String lowercase = new String();
        for (int i = 97; i <= 122; i++) {
            lowercase += (char) i;
        }

        result = lowercase;
    }else if(type == "punctuation"){
        String punctuation = new String();

        for (int i = 33; i <= 47; i++) {
            punctuation += (char) i;
        }
        for (int i = 58; i <= 64; i++) {
            punctuation += (char) i;
        }
        for (int i = 91; i <= 96; i++) {
            punctuation += (char) i;
        }
        for (int i = 123; i <= 126; i++) {
            punctuation += (char) i;
        }
        result = punctuation;
    }
    return result;
    }

    public Boolean evaluate_password(String password, Boolean show_info) {
        Boolean result = false;
        int password_state = 0b00000;
        // finish:password_judge
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
            result = true;
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
                prompt = prompt.substring(0, prompt.length() - 1);
                //
                // 字符串切片！！！！！
                //
                prompt += ".";
                System.out.println(prompt);
            }
        }
        return result;
    }

    public String generate_password(int length) {
        String result = "";
        String all_char_set = new String();
        for (int i = 33; i < 127; i++) {
            all_char_set += (char) i;
        }
        Random r = new Random();
        for (int i = 0; i < length; i++) {
            result += all_char_set.toCharArray()[r.nextInt(94)];
        }
        return result;
    }

    public String creat_password() {
        String result = "";
        pass_gen string = new pass_gen();
        result += string.string_type_out("uppercase");
        Random r = new Random();
        r.nextInt(result.length());
        return result;
        
    }

    public static void main(String[] args) {
        main_userinput();
        main_auto_password();
    }

    private static void main_auto_password() {
        Scanner in = new Scanner(System.in);
        pass_gen password = new pass_gen();
        while (true) {
            System.out.print("请输入length>");
            int length = in.nextInt();
            String user_password = password.generate_password(length);
            if (password.evaluate_password(user_password, false)) {
                System.out.println("New created pw:" + user_password);
                break;
            }
        }
        in.close();
    }

    private static void main_userinput() {
        Scanner in = new Scanner(System.in);
        String user_input = new String();
        while (true) {
            System.out.print("请输入>");
            user_input = in.nextLine();
            pass_gen password = new pass_gen();
            if (password.evaluate_password(user_input, true)) {
                break;
            }
        }
        in.close();
    }
}
