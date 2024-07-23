import java.applet.Applet;
import java.awt.Color;
import java.awt.Graphics;

public class appletLifecycle extends Applet {

    @Override
    public void init() {
        System.out.println("init method");
    }

    @Override
    public void start() {
        System.out.println("start method");
    }

    @Override
    public void paint(Graphics g) {
        g.setColor(Color.CYAN);
        g.drawRect(25, 25, 100, 100);
        setSize(500, 500);
        setVisible(true);
    }

    @Override   
    public void stop() {
        System.out.println("stop method");
    }

    @Override
    public void destroy() {
        System.out.println("destroy method");
    }
    public static void main(String[] args) {
        
    }
}
