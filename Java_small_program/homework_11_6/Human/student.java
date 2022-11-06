package Human;

public class student extends human {
    private int id;

    public student(String name, double height, int id) {
        super(name, height);
        this.id = id;
    }

    public int get_id() {
        return id;
    }
}
