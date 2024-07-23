// package LAB10;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class CopyData {

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Please provide source and destination file names as command line arguments.");
            return;
        }

        String sourceFileName = args[0];
        String destFileName = args[1];
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Select stream type:");
        System.out.println("1. Character Stream");
        System.out.println("2. Byte Stream");
        System.out.println("3. Buffered Character Stream");
        int choice = scanner.nextInt();
        
        switch (choice) {
            case 1:
                CharacterStream(sourceFileName, destFileName);
                break;
            case 2:
                ByteStream(sourceFileName, destFileName);
                break;
            case 3:
                BufferedStream(sourceFileName, destFileName);
                break;
            default:
                System.out.println("Invalid choice");
        }
        
        scanner.close();
    }

    private static void CharacterStream(String sourceFileName, String destFileName) {
        try (FileReader reader = new FileReader(sourceFileName);
             FileWriter writer = new FileWriter(destFileName)) {
            
            char[] buffer = new char[1024]; 
            int bytesRead;
            
            while ((bytesRead = reader.read(buffer)) != -1) {
                writer.write(buffer, 0, bytesRead);
            }
            
            System.out.println("File copied successfully using character stream.");
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void ByteStream(String sourceFileName, String destFileName) {
        try (FileInputStream reader = new FileInputStream(sourceFileName);
             FileOutputStream writer = new FileOutputStream(destFileName)) {
            
            byte[] buffer = new byte[1024]; 
            int bytesRead;
            
            while ((bytesRead = reader.read(buffer)) != -1) {
                writer.write(buffer, 0, bytesRead);
            }
            
            System.out.println("File copied successfully using byte stream.");
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void BufferedStream(String sourceFileName, String destFileName) {
        try (BufferedReader reader = new BufferedReader(new FileReader(sourceFileName));
             BufferedWriter writer = new BufferedWriter(new FileWriter(destFileName))) {
            String line;
            
            while ((line = reader.readLine()) != null) {
                writer.write(line);
                writer.newLine();
            }
            
            System.out.println("File copied successfully using buffered character stream.");
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
