package NetworkProgramming;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class DemoClient {
    public static void main(String[] args) {
        try {
            Socket soc = new Socket("localhost",5000);
            BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

            System.out.println("Enter two numbers");
            int a = Integer.parseInt(input.readLine());
            int b = Integer.parseInt(input.readLine());
            
            PrintWriter writer = new PrintWriter(soc.getOutputStream(), true);
            writer.println(a);
            writer.println(b);
            
            System.out.println("Sending Data to server: " + a + " and " + b);

            soc.close();
        } catch(IOException ex) {
            ex.printStackTrace();
        }
    }
}