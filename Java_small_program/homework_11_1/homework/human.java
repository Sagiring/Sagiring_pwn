package homework_11_1.homework;

public class human {
    private String name;
    public human(String name){
        this.name = name;
    }
    @Override
    public boolean equals(Object obj) {
        if(this == obj){
            return true;
        }
        if(obj == null || obj.getClass() != getClass()){
        return false;
        }
        human obj1 = (human) obj;
        if(this.name == obj1.name ){
            return true;
        }
        return false;
    }
    
    @Override
    public String toString() {
       
        return name;
    }
    @Override
    public int hashCode() {
      
        return super.hashCode();
    }
    public void happybirthday(){
        System.out.println(toString()+" happy birthday!");
    }
    public static void happybirthday(human person){
        System.out.println(person.toString()+" happy birthday!");
    }
    public static void main(String[] args) {
        student st1 = new student("zxy","2021212036");
        student st2 = new student("fsy","2021212024");
        System.out.println(st1.equals(st2));
        System.out.println(st1.toString());
        System.out.println(st2.toString());
        System.out.println(st1.hashCode());
        System.out.println(st2.hashCode());

        happybirthday(st1);
        happybirthday(st2);

        human st3 = new student("zjm", "2021212041");
        human st4 = new human("am");
        System.out.println(st3.toString());
        human human1 = (human) st2;
        student human2 = (student) st3;
        // student human3 = (student) st4; 父不能变儿
        System.out.println(human1.toString());
        System.out.println(human2.toString());
        // System.out.println(human3.toString());
        System.out.println(st4.toString());
        System.out.println(st2.equals(human2));
        System.out.println(st2.equals(human1));

        student st5 = new student("zjm", "2021212041");
        student st6 = new student("zjm", "2021212041");
        System.out.println(st5.equals(st6));
        
    }
}
