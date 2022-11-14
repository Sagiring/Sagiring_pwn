package vet;

import java.util.Arrays;
import pet.*;

/**
 * Class to keep track of client (Pet) information for a Veterinary
 * practice. Some methods are sketched for you, but others will need
 * to be added in order to implement the Database interface and
 * support the P3main program and expected output. You'll also need
 * to add the data members.
 */
public class Vet implements Database {

  private String vet_name;
  private Pet[] clients;
  private int client_num = 0;

  /**
   * Create a veterinary practice.
   * 
   * @param startSize the capacity for how
   *                  many clients they can handle
   * @param who       the name of the vet practice
   */
  public Vet(int startSize, String who) {
    vet_name = who;
    clients = new Pet[startSize];
  }

  public int size() {
    return client_num;
  }

  public Object find(Object o) {
    if (o instanceof Pet) {
      for (int i = 0; i < client_num; i++) {
        if (clients[i].compareTo((Pet) o) == 0) {
          return clients[i];
        }
      }
    }
    return null;
  }

  /**
   * Display the name of the Vet and all the clients, one per line,
   * on the screen. (See sample output for exact format.)
   */
  public void display() {
    System.out.println("Vet "+vet_name+" clients list:");
    for (int i = 0; i < client_num; i++) {
      System.out.println(clients[i]);
    }

  }

  /**
   * Add an item to the database, if there is room.
   * You are limited by the initial capacity.
   * 
   * @param o the object to add (must be a Pet)
   * @return true if added, false otherwise
   */
  public boolean add(Object o) {
    if (o instanceof Pet) {
      client_num++;
      clients[client_num - 1] = (Pet) o;
      sort();
      return true;
    }
    return false;
  }

  /**
   * Delete an item from the database, if it is there,
   * maintaining the current ordering of the list.
   * 
   * @param o the object to delete
   * @return the item if one is deleted, null otherwise
   */
  public Object delete(Object o) {
    if (o instanceof Pet) {
      for (int i = 0; i < client_num; i++) {
        if (clients[i].compareTo((Pet) o) == 0) {
          Pet to_delete = clients[i];
          for (int j = i;j+1 != client_num; j++) {
            clients[j] =clients[j+1];
          }
          clients[client_num-1] = null;
          client_num--;
          sort();
          return to_delete;
        }
      }
    }
    return null;
  }

  /**
   * Compute the average weight over all clients.
   * 
   * @return the average
   */
  public double averageWeight() {
    double weight = 0;
    for (int i = 0; i < client_num; i++) {
      weight += clients[i].get_weight();
    }
    return weight / client_num;
  }

  /**
   * Sort the clients. (This is complete.)
   */
  public void sort() {
    Arrays.sort(this.clients, 0, this.size());
  }

}
