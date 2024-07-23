package NetworkProgramming;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;


public class DemoServer {
    public static void main(String[] args) {
        try {
            System.out.println("Waiting for a Client...");

            ServerSocket sSoc = new ServerSocket(5000);
            Socket soc = sSoc.accept();

            System.out.println("Connection Established!!");

            BufferedReader reader = new BufferedReader(new InputStreamReader(soc.getInputStream()));
            int a = Integer.parseInt(reader.readLine());
            int b = Integer.parseInt(reader.readLine());
            
            System.out.println("Recived Data are: " + a + " and " + b);
            System.out.println("Sum: " + (a + b));

            sSoc.close();
            soc.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
