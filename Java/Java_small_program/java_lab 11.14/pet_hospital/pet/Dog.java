package pet;

public class Dog extends Pet{
    private String figure;
    public Dog(String pname, String oname, double wt,String figure){
        super(pname, oname, wt);
        this.figure = figure;
    }
    @Override
    public double visit(int shots) {
        double money = 0;
        money += 15;
        if(figure == "medium"){
            money += 2.5*shots;
        }else if(figure == "large"){
            money += 5.0*shots;
        }
        super.sum_money += money;
        money += super.visit(shots);
        
        return money;
    }
    @Override
    public String toString() {
        
        return figure+" dog "+ super.toString();
    }
}
