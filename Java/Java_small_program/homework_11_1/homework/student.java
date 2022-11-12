package homework;

public class student extends human{
    private String name;
    private String id;

    public student(String name,String id){
        super(name);
        this.name = name;
        this.id = id;
        System.out.println("student confirm");
    }
    @Override
    public boolean equals(Object obj) {
        if(this == obj){
            return true;
        }
        if(obj == null || obj.getClass() != getClass()){
        return false;
        }
        student obj1 = (student) obj;
        if(this.name == obj1.name && this.id == obj1.id ){
            return true;
        }
        return false;
    }
   @Override
   public String toString() {
       
       return name+" "+id;
   }
    @Override
    public int hashCode() {
        
        return super.hashCode();
    }
}
