// package LAB12;

import java.io.*;
import java.net.*;

public class CircleClient {

    public static void main(String[] args) {
        final String serverAddress = "localhost"; 
        final int port = 5000; 

        try {
            Socket socket = new Socket(serverAddress, port);
            System.out.println("Connected to server.");

            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            double radius = 5.0; 

            out.println(radius);
            System.out.println("Sent radius: " + radius);

            double area = Double.parseDouble(in.readLine());
            System.out.println("Received area of the circle: " + area);

            socket.close();
            System.out.println("Connection closed.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
