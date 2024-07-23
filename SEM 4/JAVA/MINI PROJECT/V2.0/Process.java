import java.util.Scanner;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class AccountNumber {
    private int accountNumber;
    private Users user = new Users();
    private FileManipulation dataManipulation = new FileManipulation();
    @SuppressWarnings("unused")
    private double balance;

    public int getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    boolean isAccountNumberExist(int accountNumber) {
        if (user.checkFile(accountNumber)) {
            return true;
        } else {
            return false;
        }
    }

    public int getValid6digitPIN() {
        @SuppressWarnings("resource")
        Scanner sc = new Scanner(System.in);
        int PIN = 0;
        boolean validatePIN = false;

        while (!validatePIN) {
            System.out.println("Set a 6-digit PIN:");

            if (sc.hasNextInt()) {
                PIN = sc.nextInt();

                if (PIN >= 100000 && PIN <= 999999) {
                    validatePIN = true;
                } else {
                    System.out.println("Invalid PIN. Please enter a positive 6-digit PIN.");
                }
            } else {
                System.out.println("Invalid input. Please enter a positive 6-digit PIN.");
                sc.next();
            }
        }
        // sc.close();
        return PIN;
    }

    public boolean verifyAmount(double amount) {
        boolean verifiedAmount = false;

        if (amount <= 0) {
            System.out.println("Enter valid Amount!!");
            verifiedAmount = false;
        } else {
            verifiedAmount = true;
        }

        return verifiedAmount;
    }

    public boolean changePIN(int currentPIN, int newPIN) {
        if (currentPIN != dataManipulation.readPinFromFile(this)) {
            System.out.println("Current PIN is incorrect. PIN change aborted.");
            return false;
        }
    
        String fileName = "users/" + getAccountNumber() + ".txt";
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            StringBuilder content = new StringBuilder();
            String line;
    
            while ((line = reader.readLine()) != null) {
                if (line.startsWith(String.valueOf(currentPIN))) {
                    line = String.valueOf(newPIN);
                }
                content.append(line).append("\n");
            }
    
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
                writer.write(content.toString());
            }
    
            System.out.println("PIN changed successfully.");
            dataManipulation.updatePINChangeLog(this, currentPIN, newPIN);
            return true;

        } catch (IOException e) {
            System.out.println("Error updating PIN: " + e.getMessage());
            return false;
        }
    }

}

class Users {
    final static String USER__DATA = "allUserAccountNumber.txt";
    final static String USER__DIR = "users/";

    public String getUSER__DATA() {
        return USER__DATA;
    }

    void newUser(AccountNumber ac) {

        try {
            FileWriter writer = new FileWriter(USER__DATA, true);
            int accountNumber = ac.getAccountNumber();
            writer.write(Integer.toString(accountNumber) + "\n");

            writer.close();

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public void deleteUser(AccountNumber ac) {
        try {
            File originalFile = new File(USER__DATA);
            File tempFile = new File("temp_user_data.txt");

            BufferedReader reader = new BufferedReader(new FileReader(originalFile));
            BufferedWriter writer = new BufferedWriter(new FileWriter(tempFile));

            String acToBeDeleted = Integer.toString(ac.getAccountNumber());
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                if (currentLine.contains(acToBeDeleted))
                    continue;
                writer.write(currentLine + System.lineSeparator());
            }

            writer.close();
            reader.close();

            if (!originalFile.delete()) {
                System.out.println("Could not delete original user data file.");
                return;
            }

            if (!tempFile.renameTo(originalFile)) {
                System.out.println("Could not rename temporary user data file.");
            }

            File userFile = new File(USER__DIR + ac.getAccountNumber() + ".txt");
            if (userFile.exists()) {
                if (!userFile.delete()) {
                    System.out.println("Could not delete user file.");
                }
            } else {
                System.out.println("User file does not exist.");
            }

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public boolean checkFile(int accountNumberToCheck) {
        try (BufferedReader reader = new BufferedReader(new FileReader(USER__DATA))) {
            String line;
            while ((line = reader.readLine()) != null) {

                int accountNumber = Integer.parseInt(line.trim());
                if (accountNumber == accountNumberToCheck) {
                    return true;
                }
            }
        } catch (IOException | NumberFormatException ex) {
            System.err.println("Error reading the file: " + ex.getMessage());
            ex.printStackTrace();
        }
        return false;
    }

}

class FileManipulation {
    private static Users user = new Users();

    public void checkAndCreateFiles() {
        String usersDirectoryPath = "users";
        String allUserAccountNumberFilePath = "allUserAccountNumber.txt";
        String transferingFundsRecordsFilePath = "TransferingFundsRecords.txt";
        String PINChangeLogFilePath = "PINChangeLog.txt";

        File usersDirectory = new File(usersDirectoryPath);
        File allUserAccountNumberFile = new File(allUserAccountNumberFilePath);
        File transferingFundsRecordsFile = new File(transferingFundsRecordsFilePath);
        File PINChangeLogFile = new File(PINChangeLogFilePath);

        try {
            if (!usersDirectory.exists()) {
                boolean directoryCreated = usersDirectory.mkdir();
                if (!directoryCreated) {
                    System.out.println("Failed to create the users directory.");
                }
            }
    
            if (!allUserAccountNumberFile.exists()) {
                boolean created = allUserAccountNumberFile.createNewFile();
                if (!created) {
                    System.out.println("Failed to create " + allUserAccountNumberFilePath + ".");
                }
            }
    
            if (!transferingFundsRecordsFile.exists()) {
                boolean created = transferingFundsRecordsFile.createNewFile();
                if (!created) {
                    System.out.println("Failed to create " + transferingFundsRecordsFilePath + ".");
                }
            }
    
            if (!PINChangeLogFile.exists()) {
                boolean created = PINChangeLogFile.createNewFile();
                if (!created) {
                    System.out.println("Failed to create " + PINChangeLogFilePath + ".");
                }
            }

        } catch (IOException e) {
            System.out.println("An error occurred while creating files: " + e.getMessage());
        }
    }

    public void getFileContents(String fileName, AccountNumber ac) {
        String directory = "users";
        Path filePath = Paths.get(directory, fileName);

        if (!Files.exists(filePath)) {
            System.out.println("File not found: " + filePath);
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath.toFile()))) {
            String line;
            StringBuilder gathering = new StringBuilder();
            String pass = String.valueOf(readPinFromFile(ac));
            while ((line = reader.readLine()) != null) {
                if (line.equals(pass)) {
                    continue;
                } else {
                    gathering.append(line).append("\n");
                }
            }
            String fileContents = gathering.toString();
            System.out.println("File contents:");
            System.out.println(fileContents);
        } catch (IOException e) {
            System.out.println("Error reading the file: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public void createNewFile(AccountNumber ac, int PIN) {
        String fileName = "users/" + ac.getAccountNumber() + ".txt";

        try {
            FileWriter writer = new FileWriter(fileName, true);
            writer.write(Integer.toString(PIN) + "\n");
            writer.close();
        } catch (IOException ex) {
            System.out.println("Error creating file: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

    public boolean creditAmount(AccountNumber ac, int PIN, double amount) {
        if(PIN == -1 || amount == -1.00){
            return false;
        } else {
            int storedPin = readPinFromFile(ac);

            if (PIN == storedPin) {
                // System.out.println("PIN verified.");
                LocalDateTime transactionTime = LocalDateTime.now();
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
                String formattedTransactionTime = transactionTime.format(formatter);

                try {
                    String fileName = "users/" + ac.getAccountNumber() + ".txt";
                    FileWriter writer = new FileWriter(fileName, true);

                    double balance = getLastBalance(ac, fileName);
                    balance += amount;
                    writer.write(formattedTransactionTime + " = " + amount + " is credited\n");
                    writer.write(formattedTransactionTime + " Total balance is: " + balance + "\n\n");
                    writer.close();

                    return true; // * successfully credited
                } catch (IOException ex) {
                    ex.printStackTrace();
                    return false;
                }
            } else {
                System.out.println("Incorrect PIN. Unable to credit amount.");
                return false;
            }
        }
    }

    public int readPinFromFile(AccountNumber ac) {
        String fileName = "users/" + ac.getAccountNumber() + ".txt";
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            return Integer.parseInt(reader.readLine());
        } catch (IOException | NumberFormatException ex) {
            System.out.println("Error reading PIN from file: " + ex.getMessage());
            return -1;
        }
    }

    public boolean debitAmount(AccountNumber ac, int PIN, double amount) {
        int storedPIN = readPinFromFile(ac);

        if (PIN == storedPIN) {
            // System.out.println("PIN verified.");

            LocalDateTime transactionTime = LocalDateTime.now();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            String formattedTransactionTime = transactionTime.format(formatter);

            try {
                String fileName = "users/" + ac.getAccountNumber() + ".txt";
                FileWriter writer = new FileWriter(fileName, true);

                double balance = getLastBalance(ac, fileName);
                if (balance >= amount) {
                    balance -= amount;
                    writer.write(formattedTransactionTime + " = " + amount + " is debited\n");
                    writer.write(formattedTransactionTime + " Total balance is: " + balance + "\n\n");
                    writer.close();
                    return true;
                } else {
                    System.out.println("Insufficient balance. Unable to debit amount.");
                    writer.close();
                    return false; // * will be exited due to insuff bal
                }

            } catch (IOException ex) {
                ex.printStackTrace();
                return false; // * due to io execption
            }

        } else {
            System.out.println("Incorrect PIN. Unable to debit amount.");
            return false; // * due to Incorrect pin
        }
    }

    public double getLastBalance(AccountNumber ac, String fileName) {
        double lastBalance = 0;
        String line;
        fileName = "users/" + ac.getAccountNumber() + ".txt";
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            while ((line = reader.readLine()) != null) {
                if (line.contains("Total balance is:")) {
                    String[] parts = line.split(": ");
                    lastBalance = Double.parseDouble(parts[1].trim());
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return lastBalance;
    }

    public void transferingAmount(AccountNumber sender, int senderPIN, int receiver, double amount) {
        if (senderPIN == -1 && receiver == -1 && amount == -1.00) {
            System.out.println("Something went wrong, May inputs are invalid");
            return;
        } else {
            if (!user.checkFile(receiver)) {
                System.out.println("Reciver not authenticated. Transfering of amount is aborted!!!");
            } else {
                if (!authenticateUser(sender, senderPIN)) {
                    System.out.println("Sender authentication failed. Transfer aborted.");
                    return;
                }
    
                if (!deductAmount(sender, senderPIN, amount)) {
                    System.out.println("Insufficient funds in sender's account. Transfer aborted.");
                    return;
                }
    
                if (!depositAmount(receiver, amount)) {
                    System.out.println("Error transferring amount to recipient. Transfer aborted.");
                    return;
                }
    
                updateTransactionRecords(sender, receiver, amount);
                System.out.println("Transfer successful.");
            }
        } 
    }

    private boolean authenticateUser(AccountNumber ac, int PIN) {
        if (!user.checkFile(ac.getAccountNumber())) {
            return false;
        }
        return true;
    }

    private boolean deductAmount(AccountNumber ac, int PIN, double amount) {
        return debitAmount(ac, PIN, amount);
    }

    private boolean depositAmount(int recipientAc, double amount) {
        LocalDateTime transactionTime = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String formattedTransactionTime = transactionTime.format(formatter);

        try {
            String fileName = "users/" + recipientAc + ".txt";
            FileWriter writer = new FileWriter(fileName, true);

            double lastBalance = 0;
            String line;
            fileName = "users/" + recipientAc + ".txt";
            try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
                while ((line = reader.readLine()) != null) {
                    if (line.contains("Total balance is:")) {
                        String[] parts = line.split(": ");
                        lastBalance = Double.parseDouble(parts[1].trim());
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }

            lastBalance += amount;
            writer.write(formattedTransactionTime + " = " + amount + " is credited\n");
            writer.write(formattedTransactionTime + " Total balance is: " + lastBalance + "\n\n");

            writer.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return true;
    }

    private void updateTransactionRecords(AccountNumber sender, int receiver, double amount) {
        // System.out.println("inside function");
        LocalDateTime transactionTime = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String formattedTransactionTime = transactionTime.format(formatter);

        try {
            // System.out.println("inside try");
            String fileName = "TransferingFundsRecords.txt";
            FileWriter writer = new FileWriter(fileName, true);

            writer.write(formattedTransactionTime + " Sender Account Number: " + sender.getAccountNumber() + "\n");
            writer.write(formattedTransactionTime + " Receiver Account Number: " + receiver + "\n");
            writer.write(formattedTransactionTime + " Transfered Amount: " + amount + "\n\n");

            // System.out.println("before close");
            writer.close();

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public void updatePINChangeLog(AccountNumber ac, int currentPIN, int newPIN) {
        String fileName = "PINChangeLog.txt";

        try (FileWriter writer = new FileWriter(fileName, true)) {
            LocalDateTime transactionTime = LocalDateTime.now();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            
            writer.write("Account No: " + ac.getAccountNumber() + "\n");
            writer.write("PIN changed on " + transactionTime.format(formatter) + " from: " + newPIN + " to: " + currentPIN + "\n\n");

            // System.out.println("PIN change log updated successfully.");
        } catch (IOException e) {
            System.out.println("Error updating PIN change log: " + e.getMessage());
        }
    }

}

public class Process {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        AccountNumber ac = new AccountNumber();
        Users user = new Users();
        FileManipulation dataManipulation = new FileManipulation();
        dataManipulation.checkAndCreateFiles();

        int accountNumber = 0;
        boolean validateAccountNumber = false;

        while (!validateAccountNumber) {
            System.out.println("Enter Account number:");

            if (sc.hasNextInt()) {
                accountNumber = sc.nextInt();

                if (accountNumber > 0) {
                    validateAccountNumber = true;
                } else {
                    System.out.println("Invalid account number. Please enter a positive account number.");
                }
            } else {
                System.out.println("Invalid input. Please enter a positive account number.");
                sc.next();
            }
        }

        if (ac.isAccountNumberExist(accountNumber)) {
            int PIN = ac.getValid6digitPIN();
            ac.setAccountNumber(accountNumber);
            int storedPin = dataManipulation.readPinFromFile(ac);

            if (PIN != storedPin) {
                System.out.println("PIN IS INVALID. COLLECT YOUR CARD FROM THE CARD-TRAY!!");
                System.exit(0);
            }
        } else {
            System.out.println("Welcome Your account is created");

            ac.setAccountNumber(accountNumber);

            int PIN = ac.getValid6digitPIN();
            user.newUser(ac);
            dataManipulation.createNewFile(ac, PIN);

        }

        int choice = -1;
        boolean validateChoice = false;

        do {
            System.out.println("\n1.Credit Amount");
            System.out.println("2.Debit Amount");
            System.out.println("3.show Tansactions");
            System.out.println("4.Exit");
            System.out.println("5.View Balance");
            System.out.println("6.Delete Account");
            System.out.println("7.Transfer Funds");
            System.out.println("8.Change PIN");

            System.out.println("\nEnter choice: ");
            choice = sc.nextInt();

            // while (!validateChoice) {
            //     System.out.print("\nEnter Choice:");
            //     if (sc.hasNextInt()) {
            //         choice = sc.nextInt();
            //         if (choice > 0) {
            //             validateChoice = true;
            //         } else {
            //             System.out.println("Enter valid choice");
            //         }
            //     } else {
            //         System.out.println("Enter valid choice");
            //         sc.next();
            //     }
            // }a
            // sc.nextLine();

            switch (choice) {
                case 1:
                    int PIN = -1;
                    Double amount = -1.00;

                    boolean validatePIN = false, validateAmount = false;
                    while (!validatePIN) {
                        System.out.println("Enter PIN: ");

                        if (sc.hasNextInt()) {
                            PIN = sc.nextInt();
                            if (PIN > 0) {
                                validatePIN = true;
                            } else {
                                System.out.println("Invalid PIN. Please enter a positive PIN number.");
                            }
                        } else {
                            System.out.println("Invalid input. Please enter a positive PIN number.");
                            sc.next();
                        }
                    }

                    while(!validateAmount) {
                        System.out.println("Enter Amount: ");

                        if (sc.hasNextDouble()) {
                            amount = sc.nextDouble();
                            if (PIN > 0) {
                                validateAmount = true;
                            } else {
                                System.out.println("Invalid Amount. Please enter a positive amount.");
                            }
                        } else {
                            System.out.println("Invalid input. Please enter a positive amount.");
                            sc.next();
                        }
                    }

                    if (ac.verifyAmount(amount)) {
                        dataManipulation.creditAmount(ac, PIN, amount);
                    }

                    break;

                case 2:
                    PIN = -1;
                    amount = -1.00;

                    validatePIN = false;
                    validateAmount = false;
                    
                    while (!validatePIN) {
                        System.out.println("Enter PIN: ");

                        if (sc.hasNextInt()) {
                            PIN = sc.nextInt();
                            if (PIN > 0) {
                                validatePIN = true;
                            } else {
                                System.out.println("Invalid PIN. Please enter a positive PIN number.");
                            }
                        } else {
                            System.out.println("Invalid input. Please enter a positive PIN number.");
                            sc.next();
                        }
                    }

                    while(!validateAmount) {
                        System.out.println("Enter Amount: ");

                        if (sc.hasNextDouble()) {
                            amount = sc.nextDouble();
                            if (amount > 0) {
                                validateAmount = true;
                            } else {
                                System.out.println("Invalid Amount. Please enter a positive amount.");
                            }
                        } else {
                            System.out.println("Invalid input. Please enter a positive amount.");
                            sc.next();
                        }
                    }

                    if (ac.verifyAmount(amount)) {
                        dataManipulation.debitAmount(ac, PIN, amount);
                    }

                    break;

                case 3:
                    String file_name = Integer.toString(ac.getAccountNumber()) + ".txt";
                    dataManipulation.getFileContents(file_name, ac);
                    break;

                case 4:
                    System.exit(0);
                    break;

                case 5:
                    file_name = Integer.toString(ac.getAccountNumber()) + ".txt";
                    System.out.println("Your Balane is: " + dataManipulation.getLastBalance(ac, file_name));

                    break;

                case 6:
                    file_name = Integer.toString(ac.getAccountNumber()) + ".txt";
                    System.out.println("ARE YOU SURE TO DELETE YOUR ACCOUNT? THEN TYPE yes");

                    String confirm = sc.next();
                    confirm = confirm.toLowerCase();

                    if (confirm.equals("yes") || confirm.equals("y")) {
                        user.deleteUser(ac);
                        System.out.println("YOUR ACCOUNT HAS BEEN DELETED");
                        System.exit(0);
                    }
                    break;

                case 7:
                    int reciverAc = -1;
                    PIN = -1;
                    amount = -1.00;

                    validatePIN = false;
                    validateAmount = false;
                    boolean validateReciverAc = false;

                    while (!validateReciverAc) {
                        System.out.println("Enter Account Number of Reciver: ");

                        if (sc.hasNextInt()) {
                            reciverAc = sc.nextInt();
                            if (reciverAc > 0) {
                                validateReciverAc = true;
                            } else {
                                System.out.println("Invalid Receiver account number. Please enter a positive account number.");
                            }
                        } else {
                            System.out.println("Invalid input. Please enter a positive receiver number.");
                            sc.next();
                        }
                    }

                    while (!validatePIN) {
                        System.out.println("Enter PIN: ");

                        if (sc.hasNextInt()) {
                            PIN = sc.nextInt();
                            if (PIN > 0) {
                                validatePIN = true;
                            } else {
                                System.out.println("Invalid PIN. Please enter a positive PIN number.");
                            }
                        } else {
                            System.out.println("Invalid input. Please enter a positive PIN number.");
                            sc.next();
                        }
                    }

                    while(!validateAmount) {
                        System.out.println("Enter Amount: ");

                        if (sc.hasNextDouble()) {
                            amount = sc.nextDouble();
                            if (amount > 0) {
                                validateAmount = true;
                            } else {
                                System.out.println("Invalid Amount. Please enter a positive amount.");
                            }
                        } else {
                            System.out.println("Invalid input. Please enter a positive amount.");
                            sc.next();
                        }
                    }
                    if (ac.getAccountNumber() == reciverAc) {
                        System.out.println("YOU CAN'T TRANSFER INTO YOUR OWN account");
                    } else {
                        if (ac.verifyAmount(amount)) {
                            dataManipulation.transferingAmount(ac, PIN, reciverAc, amount);
                        }
                    }

                    break;
                
                case 8:
                    validatePIN = false;
                    int newPIN = -1;
                    PIN = -1;

                    while (!validatePIN) {
                        System.out.println("Enter PIN: ");

                        if (sc.hasNextInt()) {
                            PIN = sc.nextInt();
                            if (PIN > 0) {
                                validatePIN = true;
                            } else {
                                System.out.println("Invalid PIN. Please enter a positive PIN number.");
                            }
                        } else {
                            System.out.println("Invalid input. Please enter a positive PIN number.");
                            sc.next();
                        }
                    }

                    newPIN = ac.getValid6digitPIN();
                        
                    ac.changePIN(PIN, newPIN);
                    break;

                default:
                    System.out.println("INVALID CHOICE!!");
                    break;
            }
        } while (choice != 4);

        sc.close();
    }
}