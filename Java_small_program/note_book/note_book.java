package note_book;

import java.util.ArrayList;

public class note_book {
    private ArrayList<String> notes = new ArrayList<String>();

    public void add(String s) {
        notes.add(s);
    }

    public int get_size() {
        return notes.size();
    }

    public String get_note(int index) {
        return notes.get(index);
    }

    public void remove_note(int index) {
        notes.remove(index);
    }

    public String[] show_list() {
        String[] a = new String[notes.size()];
        // for (int i = 0; i < notes.size(); i++) {
        //     a[i] = notes.get(i);
        // }
        notes.toArray(a);
        // 好函数 像list
        return a;
    }

    public static void main(String[] args) {
        note_book nb = new note_book();
        nb.add("first");
        nb.add("second");
        System.out.println(nb.notes);
        // List来咯
        //set是元组？
        
    }
}
