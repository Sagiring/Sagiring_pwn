package java_any;

import java.util.Calendar;

public class Java_any {
    public static void main(String[] args) {
        String[] date = {"2020","3","12"};
        Calendar c1 = Calendar.getInstance();

        c1.set(Integer.parseInt(date[0]), Integer.parseInt(date[1]) - 1, 1);
        System.out.println(c1.get(Calendar.DAY_OF_WEEK));
        
    }

}
