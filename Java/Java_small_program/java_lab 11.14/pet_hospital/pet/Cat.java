package pet;

public class Cat extends Pet {
    private String live_state = "inside";

    public Cat(String pname, String oname, double wt) {
        super(pname, oname, wt);
    }

    public void goOutside() {
        live_state = "outside";
    }

    @Override
    public double visit(int shots) {
        double money = 0;
        money += 20;
        super.sum_money += money;

        if (live_state == "outside") {
            shots++;
        }
        money += super.visit(shots);

        return money;
    }
    @Override
    public String toString() {
        
        return live_state+" cat "+super.toString();
    }
}
