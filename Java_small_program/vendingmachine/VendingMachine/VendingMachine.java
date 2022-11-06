package VendingMachine;

public class VendingMachine {
    int price = 80;
    int balance;
    int total;

    void setPrice(int price){
        this.price = price;
    }

    void showPrompt() {
        System.out.println("welcome");
    }

    void insertMoney(int amount) {
        balance = balance + amount;
    }

    void showBalance() {
        System.out.println(balance);
    }

    void getFood() {
        if (balance >= price) {
            System.out.println("here you are.");
            balance = balance - price;
            total = total + price;
        }
    }
public static void main(String[] args){
    VendingMachine vm = new VendingMachine();
    vm.showPrompt();
    vm.showBalance();
    vm.insertMoney(100);
    vm.getFood();
    vm.showBalance();
}
}
