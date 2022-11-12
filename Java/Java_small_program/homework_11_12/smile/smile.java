package smile;


import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;

public class smile extends JFrame {
    public smile(){
       
        setTitle("smile");
        setSize(500, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setBackground(Color.white);
    }
    public void paint(Graphics g){
        g.setColor(Color.yellow);
        g.fillRoundRect(100,120,300,300, 300, 300); 
        g.setColor(Color.black);
        g.fillRoundRect(180,210,30,30, 30, 30); 
        g.fillRoundRect(280,210,30,30, 30, 30); 
        g.drawLine(160, 320, 330, 320);
        g.drawArc(160, 245, 170, 150, 0, -180);
        g.fillArc(160, 245, 170, 150, 0, -180);
    }

 public static void main(String[] args) {
    smile g = new smile();
    g.setVisible(true);
 }
}
