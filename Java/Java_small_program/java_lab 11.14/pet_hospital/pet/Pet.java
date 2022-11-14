package pet;

import java.text.DecimalFormat;

/**
 * This is a class to define Pet objects. Pets should be compared
 * according to their owner's names, ignoring capitalization. Ties
 * should be broken based on the pet's name, ignoring capitalization.
 * 
 * Your job is to add the necessary data and methods to support the
 * P3main program, as well as the related classes in this system. Some
 * required methods are noted below with comments, but these are not the
 * only things you will need.
 */
public class Pet implements Comparable<Pet>{

   /** Handy for formatting. */
   private static DecimalFormat money = new DecimalFormat("0.00");

   /* The access specifiers for these variables must not be changed! */

   private String name;
   private String owner;
   private double weight = 0;

   protected double sum_money = 0;
   private int cnt_visit = 0;

   /**
    * Create a Pet object, initializing data members.
    * 
    * @param pname the Pet's name
    * @param oname the owner's name
    * @param wt    the weight of the pet
    */
   public Pet(String pname, String oname, double wt) {
      name = pname;
      owner = oname;
      weight = wt;
   }

   @Override
   public String toString() {
      return this.name + " (owner " + this.owner + ") " + this.weight
            + " lbs, $" + money.format(this.avgCost()) + " avg cost/visit  ";
   }

   /**
    * The Pet is visiting the vet, and will be charged accordingly.
    * The base cost for a visit is $85.00, and $30/shot is added.
    * 
    * @param shots the number of shots the pet is getting
    * @return the entire cost for this particular visit
    */
   public double visit(int shots) {
      double sum = shots * 30.0 + 85.0;
      sum_money += sum;
      cnt_visit += 1;

      return sum;
   }

   /**
    * Determine the average cost per visit for this pet.
    * 
    * @return that cost, or 0 if no visits have occurred yet
    */
   public double avgCost() {
      if (cnt_visit == 0) {
         return 0;
      }
      return sum_money / cnt_visit ;
   }

   public int compareTo(Pet pet) {
      int owner_is = owner.compareToIgnoreCase(pet.owner);
      int name_is = name.compareToIgnoreCase(pet.name);
      if(owner_is == 0 && name_is == 0){
         return 0;
      }else if(owner_is > 0){
         return 1;
      }else if(owner_is < 0){
         return -1;
      }else{
         if (name_is > 0) {
            return 1;
         }else{
            return -1;
         }
       
      }
   };
   public double get_weight(){
      return weight;
   }


}
