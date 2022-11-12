package time_class;

import java.util.Calendar;

public class time {
    Calendar c1 = Calendar.getInstance();
    public int hour;
    public int minute;
    boolean is24 = true;

    public void show_is24(boolean is24) {
        this.is24 = is24;
    }

    public void record_time(int hour, int minute) {
        this.hour = hour;
        this.minute = minute;

    }

    public time() {

        hour = c1.get(Calendar.HOUR_OF_DAY);
        minute = c1.get(Calendar.MINUTE);

    }

    public time(int hour, int minute) {
        this.hour = hour;
        this.minute = minute;
    }

    public void add_hour() {
        if (hour == 23) {
            hour = 0;
        } else {
            hour++;
        }
    }

    public void add_hour(int n) {
        while (n > 24) {
            n -= 24;
        }
        if (hour + n >= 23) {
            hour = hour + n - 24;
        } else {
            hour += n;
            ;
        }
    }

    public void add_minute() {
        if (minute == 59) {
            minute = 0;
        } else {
            minute++;
        }
    }

    public void add_minute(int n) {
        while (n > 60) {
            n -= 60;
        }
        if (minute + n >= 59) {
            minute = minute + n - 60;
        } else {
            minute += n;
            ;
        }
    }

    public void to_string() {
        int is12 = 0;
        String[] time_is12 = { "AM", "PM" };
        if (!is24) {
            if(hour>12){
                is12 = 1;
                hour -= 12;
            }
        }
            if (hour < 10) {
                System.out.print("0" + hour);
            }else{
                System.out.print(hour);
            }
            System.out.print(":");
            if (minute < 10) {
                System.out.print("0" + minute);
            }else{
                System.out.print(minute);
            }
            if (!is24) {
                System.out.print(time_is12[is12]);
            }
            System.out.println();
    }

    public static void main(String[] args) {
        
        time t1 = new time();
        t1.to_string();
        t1.record_time(13, 14);
        t1.to_string();
        time t2 = new time(13, 14);
        t2.show_is24(false);
        t2.to_string();
        t2.add_hour();
        t2.add_minute();
        t2.to_string();
        t2.add_hour(50);
        t2.add_minute(50);
        t2.to_string();
    }
}
