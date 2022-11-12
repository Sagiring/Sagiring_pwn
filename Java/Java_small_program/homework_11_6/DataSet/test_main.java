package DataSet;
import Human.*;

public class test_main {
    public static void main(String[] args) {
        human p1 = new human("f",1.70);
        human p2 = new human("s",1.75);
        student s1 = new student("m", 1.80, 2021212041);
        student s2 = new student("fsy", 2.0, 2021212036);
        DataSet d1 = new DataSet();
        d1.add(p1);
        d1.add(p2);
        d1.add(s1);
        d1.add(s2);
        System.out.println(d1.getAverage());
        System.out.println(d1.getMaximum());
       
    }
}
