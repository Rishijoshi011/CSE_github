import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;

public class clientCode {
    public static void main(String[] args) {
        
        try {
            Socket socket = new Socket("localhost", 5000);
            OutputStream output = socket.getOutputStream();

            System.out.println("connection established...");

            PrintWriter writer = new PrintWriter(output, true);
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            BufferedReader consolReader = new BufferedReader(new InputStreamReader(System.in));

            System.out.println("Enter any two number");
            int num = Integer.parseInt(consolReader.readLine());
            int num2 = Integer.parseInt(consolReader.readLine());

            writer.println(num);
            writer.println(num2);

            int result = Integer.parseInt(reader.readLine());
            System.out.println("unpacking recived data...");
            System.out.println("Result is: " + result);

            consolReader.close();
            reader.close();
            writer.close();
            output.close();
            socket.close();

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
