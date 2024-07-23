// package LAB12;

import java.io.*;
import java.net.*;

public class CircleServer {

    public static void main(String[] args) {
        final int port = 5000;

        try {
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server is listening on port " + port);

            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected.");

            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

            double radius = Double.parseDouble(in.readLine());
            System.out.println("Received radius: " + radius);

            double area = Math.PI * radius * radius;

            out.println(area);
            System.out.println("Sent area: " + area);

            clientSocket.close();
            serverSocket.close();
            System.out.println("Server closed.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
