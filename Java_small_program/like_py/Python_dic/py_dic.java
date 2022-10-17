package python_dic;

import java.util.HashMap;
import java.util.Scanner;

public class py_dic {
    private HashMap<Integer, String> coin_name = new HashMap<Integer, String>();

    public py_dic() {
        coin_name.put(1, "penny");
        coin_name.put(10, "dime");
        coin_name.put(15, "quarter");
        coin_name.put(50, "half-dolar");
        System.out.println(coin_name.keySet().size());
        // Key的所有值 keyset() for int k:keyset()
        System.out.println(coin_name);
    }

    public String getName(int amount) {
        if (coin_name.containsKey(amount)) {
            return coin_name.get(amount);
        } else {
            return "Not Found";
        }

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int amount = in.nextInt();
        py_dic coin = new py_dic();
        String name = coin.getName(amount);
        System.out.println(name);
        in.close();

    }
}
