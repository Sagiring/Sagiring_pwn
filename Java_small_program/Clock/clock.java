package Clock;

public class clock {
    private Display hour = new Display(24);
    private Display minute = new Display(60);

    public void start() {
        while (true) {
            minute.increase();
            if (minute.get_value() == 0) {
                hour.increase();
            }
            System.out.printf("%02d:%02d\n", hour.get_value(), minute.get_value());
        }
    }

    public static void main(String[] args) {
        clock Clock_test = new clock();
        Clock_test.start();
    }
}
