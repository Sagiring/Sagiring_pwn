
import java.util.Calendar;
import java.util.Scanner;
public class birthday_calendar {
    private String[] week = { "周日", "周一", "周二", "周三", "周四", "周五", "周六" };

    public void print_week(String[] date) {
        System.out.println(date[0]);
        birthday_calendar bir = new birthday_calendar();
        for (String i : bir.week) {
            System.out.print(" " + i);
        }
        System.out.println();
    }

    public void print_date(String[] date) {

        int max_day;
        Calendar c1 = Calendar.getInstance();
        c1.set(Integer.parseInt(date[0]), Integer.parseInt(date[1]) - 1, 1);

        int week_fin = c1.get(Calendar.DAY_OF_WEEK);
        max_day = c1.getActualMaximum(Calendar.DATE);
        int is_first = 1;
        for (int j = 1; j < week_fin; j++) {
            System.out.print("     ");
        }
        for (int i = 1; i <= max_day; i++) {

            if (is_first == 0) {
                if (i < 10) {
                    System.out.print("    ");
                } else {
                    System.out.print("   ");
                }
            } else {
                is_first = 0;
                System.out.print("  ");
            }
            if (i == Integer.parseInt(date[2])) {
                System.out.print(i + "*");
            } else {
                System.out.print(i);
            }
            if (week_fin == 7) {
                System.out.println();
                week_fin = 0;
                is_first = 1;
            }
            week_fin++;
        }
        System.out.println();

    }

    public void print_all_rate(String[] rate_date) {
        String week[] = { "一", "二", "三", "四", "五", "六", "日" };
        Calendar c1 = Calendar.getInstance();
        c1.set(Integer.parseInt(rate_date[0]), Integer.parseInt(rate_date[1]) - 1,Integer.parseInt(rate_date[2]) );
        float sum = 0;
        int[] week_num_sum = new int[7];

        for (int i = 0; Integer.parseInt(rate_date[0]) + i < 2022; i++) {
            c1.set(Integer.parseInt(rate_date[0]) + i, Integer.parseInt(rate_date[1]) - 1, Integer.parseInt(rate_date[2]) );
            int week_fin = c1.get(Calendar.DAY_OF_WEEK) - 1;
            week_num_sum[week_fin] += 1;
            sum++;
        }
        for (int i = 0; i < 7; i++) {
            System.out.println("星期" + week[i] + ":" + String.format("%.3f",week_num_sum[i] / sum));
        }
    }

    public static void main(String[] args) {
        birthday_calendar bir = new birthday_calendar();
        String user_input = "2019 3 12";
        System.out.println("请输入年月日(格式:2007 12 3)");
        Scanner in = new Scanner(System.in);
        user_input = in.nextLine();
        in.close();
        String[] date = user_input.split(" ");
        // split!!
        String[] rate_date = user_input.split(" ");
        Calendar c1 = Calendar.getInstance();
        while (Integer.parseInt(date[0]) < 2022) {
            
            c1.set(Integer.parseInt(date[0]), Integer.parseInt(date[1]) - 1, 1);
            bir.print_week(date);
            bir.print_date(date);
            date[0] = (Integer.parseInt(date[0]) + 1) + "";
        }
        // System.out.println(week[c1.get(Calendar.DAY_OF_WEEK)-1]);
        bir.print_all_rate(rate_date);
    }
}
