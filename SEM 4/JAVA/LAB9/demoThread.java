import java.lang.Thread;

class TestThread extends Thread {
    
    TestThread(String name) {
        super(name);
    }
    
    public void run() {
        if (Thread.currentThread().getName().equals("first")) {
            for (int i = 0; i < 100; i++) {
                System.out.print("a" + " ");
            }
        } else if (Thread.currentThread().getName().equals("second")) {
            for (int i = 0; i < 100; i++) {
                System.out.print("b" + " ");
            }
        } else if (Thread.currentThread().getName().equals("third")) {
            for (int i = 1; i <= 100; i++) {
                System.out.print(i + " ");
            }
        } 
    }
}

public class demoThread {
    public static void main(String[] args) {
        TestThread t = new TestThread("first");
        TestThread t2 = new TestThread("second");
        TestThread t3 = new TestThread("third");
        t3.start();
        t.start();
        t2.start();
    }    
}
