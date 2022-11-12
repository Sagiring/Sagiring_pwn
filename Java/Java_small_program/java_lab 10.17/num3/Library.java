package num3;

import java.util.ArrayList;

public class Library {
    ArrayList<Book> l = new ArrayList<Book>();
    String Address;

    // Add the missing implementation to this class
    public Library(String library_name) {
        Address = library_name;
    }

    public void addBook(Book add_book) {
        l.add(add_book);
    }

    public static void printOpeningHours() {
        System.out.println("Libraries are open daily from 9am to 5pm.");
    }

    public void printAddress() {
        System.out.println(Address);
    }

public void borrowBook(String book_title){
    boolean find_bool = false;
    for (Book book : l) {
        if(book.title == book_title){
            if(book.borrowed == false){
            book.borrowed = true;
            System.out.println("You successfully borrowed The Lord of the Rings");
            }else{
            System.out.println("Sorry, this book is already borrowed.");
            }
            find_bool = true;
            break;
        }
    }
    if(find_bool == false){
        System.out.println("Sorry, this book is not in our catalog.");
    }
}

    public void printAvailableBooks() {
        if(!l.isEmpty())
        for (Book book : l) {
            System.out.println(book.title);
        }else{
            System.out.println("No book in catalog");
        }
    }

    public void returnBook(String book_title) {
        for (Book book : l) {
            if (book.title == book_title) {
                book.borrowed = false;
                System.out.println("You successfully returned The Lord of the Rings");
            }
        }
    }

    public static void main(String[] args) {
        // Create two libraries
        Library firstLibrary = new Library("10 Main St.");
        Library secondLibrary = new Library("228 Liberty St.");

        // Add four books to the first library
        firstLibrary.addBook(new Book("The Da Vinci Code"));
        firstLibrary.addBook(new Book("Le Petit Prince"));
        firstLibrary.addBook(new Book("A Tale of Two Cities"));
        firstLibrary.addBook(new Book("The Lord of the Rings"));

        // Print opening hours and the addresses
        System.out.println("Library hours:");
        printOpeningHours();
        System.out.println();

        System.out.println("Library addresses:");
        firstLibrary.printAddress();
        secondLibrary.printAddress();
        System.out.println();

        // Try to borrow The Lords of the Rings from both libraries
        System.out.println("Borrowing The Lord of the Rings:");
        firstLibrary.borrowBook("The Lord of the Rings");
        firstLibrary.borrowBook("The Lord of the Rings");
        secondLibrary.borrowBook("The Lord of the Rings");
        System.out.println();

        // Print the titles of all available books from both libraries
        System.out.println("Books available in the first library:");
        firstLibrary.printAvailableBooks();
        System.out.println();
        System.out.println("Books available in the second library:");
        secondLibrary.printAvailableBooks();
        System.out.println();

        // Return The Lords of the Rings to the first library
        System.out.println("Returning The Lord of the Rings:");
        firstLibrary.returnBook("The Lord of the Rings");
        System.out.println();

        // Print the titles of available from the first library
        System.out.println("Books available in the first library:");
        firstLibrary.printAvailableBooks();
    }
}