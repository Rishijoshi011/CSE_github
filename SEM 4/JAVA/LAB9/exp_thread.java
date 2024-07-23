import java.lang.Runnable;

class TestThread2 implements Runnable {

    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.print("a" + " ");
        }  
    }
}

public class exp_thread {
    public static void main(String[] args) {
        TestThread2 t = new TestThread2();
        Thread thread = new Thread(t); 
        thread.start(); 
    }
}
