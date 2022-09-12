package Clock;

public class Display {
    private int value = 0;
    private int limit = 0;

    public Display(int limit) {
        this.limit = limit;
    }

    public void increase(){
        value ++;
        if (value == limit){
            value = 0;
        }
    }
    public int get_value(){
        return value;
    }
    public static void main(String[] args) {
        Display d = new Display(24);
        while(true){
          d.increase();
          System.out.println(d.get_value());
        }
    }
}
