// package LAB10;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Random;

public class RandomIntegerFile {

    public static void main(String[] args) {
        String fileName = "rand.dat"; 
        int numberOfIntegers = 10; 

        generateRandomIntegersToFile(fileName, numberOfIntegers);

        readIntegersFromFileAndDisplay(fileName);
    }

    private static void generateRandomIntegersToFile(String fileName, int numberOfIntegers) {
        Random random = new Random();

        try (DataOutputStream dataOutputStream = new DataOutputStream(new FileOutputStream(fileName))) {
            for (int i = 0; i < numberOfIntegers; i++) {
                int randomInteger = random.nextInt(100); 
                dataOutputStream.writeInt(randomInteger);
            }
            System.out.println("Random integers written to file: " + fileName);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void readIntegersFromFileAndDisplay(String fileName) {
        try (DataInputStream dataInputStream = new DataInputStream(new FileInputStream(fileName))) {
            System.out.println("Integers read from file: " + fileName);
            
            while (dataInputStream.available() > 0) {
                int integer = dataInputStream.readInt();
                System.out.println(integer);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}