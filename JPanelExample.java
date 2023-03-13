import javax.swing.*;
import java.awt.*;

public class JPanelExample {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JPanel Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setPreferredSize(new Dimension(400, 300));
        panel.setBackground(Color.WHITE);

        JLabel label = new JLabel("Hello, JPanel!");
        label.setFont(new Font("Arial", Font.BOLD, 24));
        panel.add(label);

        frame.getContentPane().add(panel);
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
