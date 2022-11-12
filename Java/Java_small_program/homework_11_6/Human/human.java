package Human;

import high_data.height;
public class human implements height {
    private double height;
    private String name;

   public double getdata() {
       return height;
   }
   public human(String name,double height){
    this.name = name;
    this.height= height;
   }
    public String get_name(){
        return name;
    }
}
