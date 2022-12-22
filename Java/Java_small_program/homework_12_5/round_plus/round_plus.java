package round_plus;
import java.awt.Color;
import java.awt.Cursor;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.event.MouseInputAdapter;

public class round_plus extends JFrame {
    private JFrame frame1 = new JFrame();
    private JPanel panel1 = new JPanel() {
        @Override
        public void paint(Graphics g) {
            super.paint(g);
            g.drawOval(100, 100, 300, 300);
        }
    };
    // private JPanel panel_round = new JPanel();

    private JButton b1 = new JButton("Red");
    private JButton b2 = new JButton("Green");
    private JButton b3 = new JButton("Blue");

    public round_plus() {

        set_frame();

        set_panel_button();
        set_Mouse_listener();

        panel1.setVisible(true);
        frame1.setContentPane(panel1);
        frame1.setVisible(true);

    }

    private void set_Mouse_listener() {
        panel1.addMouseMotionListener(new MouseInputAdapter() {
            @Override
            public void mouseMoved(MouseEvent e) {
                super.mouseMoved(e);
                if (e.getPoint().distance(250, 250) <= 153) {

                    panel1.setCursor(Cursor.getPredefinedCursor(Cursor.CROSSHAIR_CURSOR));
                } else {
                    panel1.setCursor(Cursor.getPredefinedCursor(Cursor.DEFAULT_CURSOR));
                }
            }

        });
        panel1.addMouseListener(new MouseInputAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                super.mouseClicked(e);
             
                if (e.getPoint().distance(250, 250) <= 153) {
                    new Thread(){
                        public void run() {
                            super.run();
                            while (true) {
                                paint_color(panel1.getGraphics(), panel1.getBackground());
                                time_sleep(1000);
                                paint_color(panel1.getGraphics(), Color.red);
                                time_sleep(1000);
                                paint_color(panel1.getGraphics(), Color.green);
                                time_sleep(1000);
                                paint_color(panel1.getGraphics(), Color.blue);
                                time_sleep(1000);
                            }
                        };
                    }.start();
                   
                }
            }
        });
    }

    private void set_panel_button() {
        panel1.add(b1);
        panel1.add(b2);
        panel1.add(b3);
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

    private void set_frame() {
        frame1.setTitle("ColorTest ");
        frame1.setSize(500, 500);
        frame1.setDefaultCloseOperation(EXIT_ON_CLOSE);
        frame1.setLocationRelativeTo(null);
        frame1.setBackground(Color.white);
    }

    public void paint_color(Graphics g, Color c) {
        if (g != null) {
            g.setColor(c);
            g.fillRoundRect(100, 100, 300, 300, 300, 300);
        } else {
            System.out.println("Error");
        }

    }

    public void time_sleep(int n) {
        try {
            Thread.sleep(n);
        } catch (InterruptedException ie) {
            System.exit(0);
        }
    }

    public static void main(String[] args) {
        round_plus g = new round_plus();
        System.out.println(g);
    }

}
