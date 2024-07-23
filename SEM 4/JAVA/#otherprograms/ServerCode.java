import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class ServerCode {
    public static void main(String[] args) {
       
        try {
            System.out.println("Wating for Client...");
            ServerSocket serverSocket = new ServerSocket(5000);
            Socket socket = serverSocket.accept();

            System.out.println("connection established...");

            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            OutputStream output = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(output, true);

            int num = Integer.parseInt(reader.readLine());
            int num2 = Integer.parseInt(reader.readLine());
            System.out.println("Working on recived data...");

            int result = num + num2;

            System.out.println("Sending data...");

            writer.println(result);
            
            writer.close();
            output.close();
            reader.close();
            socket.close();
            serverSocket.close();

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}