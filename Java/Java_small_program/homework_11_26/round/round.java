package round;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class round extends JFrame {
    private JFrame frame1 =  new JFrame();
    private JPanel panel1 = new JPanel(){
        @Override
        public void paint(Graphics g) {
            super.paint(g);
            g.drawRoundRect(100, 100, 300, 300, 300, 300);
        }
    };
    private JButton b1 = new JButton("Red");
    private JButton b2 = new JButton("Green");
    private JButton b3 = new JButton("Blue");
    
    public round() {
      
        frame1.setTitle("ColorTest ");
        frame1.setSize(500, 500);
        frame1.setDefaultCloseOperation(EXIT_ON_CLOSE);
        frame1.setLocationRelativeTo(null);
        frame1.setBackground(Color.white);
   
        panel1.add(b1);
        panel1.add(b2);
        panel1.add(b3);
        frame1.setContentPane(panel1);
        frame1.setVisible(true);
        
        
        b1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                paint_color(panel1.getGraphics(), Color.red);
            }
        });

        b2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                paint_color(panel1.getGraphics(), Color.green);
            }
        });

        b3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                paint_color(panel1.getGraphics(), Color.blue);
            }
        });
    }
   

    public void paint_color(Graphics g, Color c) {
        if (g != null) {
            g.setColor(c);
            g.fillRoundRect(100, 100, 300, 300, 300, 300);
        } else {
            System.out.println("Error");
        }

    }

    public static void main(String[] args) {
        round g = new round();
        System.out.println(g);
    }

}
