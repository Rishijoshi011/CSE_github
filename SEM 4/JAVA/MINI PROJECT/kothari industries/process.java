import java.util.Scanner;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.Console;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.text.ParseException;
import java.text.SimpleDateFormat;

class admin {

    private static final String DATABASE_PATH = "database";
    private static final String DATABASE_FILE = "database/employeeid.txt";

    private static final String ADMIN_USERNAME = "admin";
    private static final String ADMIN_PASSWORD = "admin@123";

    private int currentEmployeeCount = 0;

    private int flagdeleteemp = 0;

    // private String id;
    private String name;
    private String dob;
    private String gender;
    private String address;
    private String designation;
    private String personalEmail;
    private String phone;
    private double salaryBase;
    private String empPassword;


    public admin(String name, String dob, String gender, String address, String designation, String personalEmail,
            String phone, double salaryBase) {

        this.name = name;
        this.dob = dob;
        this.gender = gender;
        this.address = address;
        this.designation = designation;
        this.personalEmail = personalEmail;
        this.phone = phone;
        this.salaryBase = salaryBase;
    }

    public admin() {
    }

    public void AdminLogin() {
        Console console = System.console();
        if (console == null) {
            System.out.println("Console not available. Exiting...");
            return;
        }
        System.out.println("Please Enter your Login Credentials:");

        String adminUserName = console.readLine("Username: ");

        System.out.print("Password: ");
        char[] adminPassChars = console.readPassword();

        String adminPass = new String(adminPassChars);

        if (ADMIN_USERNAME.equals(adminUserName) && ADMIN_PASSWORD.equals(adminPass)) {
            System.out.println("\nHello Admin!");

            while (true) {
                System.out.println();
                System.out.println("+--------+-------------------------+");
                System.out.println("| Choice |         Action          |");
                System.out.println("+--------+-------------------------+");
                System.out.println("|   1    | List of Employees       |");
                System.out.println("|   2    | Add Employee            |");
                System.out.println("|   3    | Logout and Exit         |");
                System.out.println("+--------+-------------------------+");

                System.out.print("Enter Choice : ");
                int choice = Integer.parseInt(console.readLine());

                switch (choice) {
                    case 1:
                        listEmployees();
                        break;
                    case 2:
                        addEmployee();
                        break;
                    case 3:
                        System.out.println("Logging Out...");
                        System.out.println("Exiting...");
                        return;
                    default:
                        System.out.println("Invalid Choice!");
                        break;
                }
            }
        } else {
            System.out.println("Invalid Username or Password!");
            return;
        }
    }

    // public void AdminLogin() {

    //     @SuppressWarnings("resource")
    //     Scanner sc = new Scanner(System.in);

    //     System.out.println ("Please Enter your Login Credentials: ");

    //     System.out.print ("Username: ");
    //     String adminUserName = sc.next();

    //     System.out.print ("Password: ");
    //     String adminPass = sc.next();

    //     if (adminUserName.equals("admin") && adminPass.equals("admin@123")) {
    //         System.out.println();
    //         System.out.println("\nHello Admin!");

    //         while (true) {

    //             System.out.println();

    //             System.out.println("+--------+-------------------------+");
    //             System.out.println("| Choice |         Action          |");
    //             System.out.println("+--------+-------------------------+");
    //             System.out.println("|   1    | List of Employees       |");
    //             System.out.println("|   2    | Add Employee            |");
    //             System.out.println("|   3    | Logout and Exit         |");
    //             System.out.println("+--------+-------------------------+");

    //             System.out.print("Enter Choice : ");
    //             int choice = sc.nextInt();

    //             switch (choice) {

    //                 case 1:

    //                     listEmployees();
    //                     break;

    //                 case 2:

    //                     addEmployee();
    //                     break;

    //                 case 3:

    //                     System.out.println("Logging Out...");
    //                     System.out.println("Exiting...");
    //                     return;

    //                 default:

    //                 System.out.println("Invalid Choice!");
    //                 break;
    //             }

    //         }

    //     }

    //     else {
    //         System.out.println ("Invalid Username or Password!");
    //         return;
    //     }
    // }


    @SuppressWarnings("resource")
    public void listEmployees() {

        try {

            BufferedReader reader = new BufferedReader(new FileReader(DATABASE_FILE));

            String line = reader.readLine();
            Scanner sc = new Scanner(System.in);

            if (line != null && !line.isEmpty()) {

                currentEmployeeCount = Integer.parseInt(line);

                if (currentEmployeeCount > 0) {
                    System.out.println("+------------+----------------------+----------------------+");
                    System.out.println("| EmployeeID |         Name         |      Designation     |");
                    System.out.println("+------------+----------------------+----------------------+");

                    for (int i = 1; i <= currentEmployeeCount; i++) {
                        String fileName = "database/employeeData" + i + ".txt";
                        BufferedReader dataReader = new BufferedReader(new FileReader(fileName));
                        String employeeID = dataReader.readLine().split(":")[1].trim();
                        String employeeName = dataReader.readLine().split(":")[1].trim();
                        String employeeDesignation = dataReader.readLine().split(":")[1].trim();
                        dataReader.close();
                        System.out.printf("| %-10s | %-20s | %-20s |%n", employeeID, employeeName, employeeDesignation);
                    }

                    System.out.println("+------------+----------------------+----------------------+");

                    do {

                        System.out.println("\nOptions Menu : ");
                        System.out.println("+--------+-------------------------+");
                        System.out.println("| Choice | Action                  |");
                        System.out.println("+--------+-------------------------+");
                        System.out.println("|   1    | Fetch Details           |");
                        System.out.println("|   2    | Return To Admin Menu    |");
                        System.out.println("+--------+-------------------------+");

                        System.out.print("Enter Choice : ");

                        int choice = sc.nextInt();
                        sc.nextLine();

                        switch (choice) {

                            case 1:

                                System.out.print("Enter EmployeeID to fetch details: ");

                                String employeeIDInput = sc.nextLine();
                                String temp = employeeIDInput;
                           
                                if (!employeeIDInput.contains("KT00")) {
                                    employeeIDInput = "KT00" + temp;
                                }
                                
                                fetchEmployeeDetails(employeeIDInput);
                                break;

                            case 2:

                                return;

                            default:

                                System.out.println("Enter Valid Choice !");
                                break;
                        }
                    } while (true);
                } else {

                    System.out.println(" \n No employees enrolled.");

                }
            } else {

                System.out.println("\n No employees enrolled.");

            }

            reader.close();

        } catch (IOException e) {

            System.out.println("Error listing employees: " + e.getMessage());

        }
    }

    @SuppressWarnings("resource")
    public void fetchEmployeeDetails(String employeeID) {
        try {

            Scanner sc = new Scanner(System.in);

            String fileName = "database/employeeData" + employeeID.substring(4) + ".txt";
            String fileId = employeeID.substring(4);

            BufferedReader dataReader = new BufferedReader(new FileReader(fileName));
            String line;

            while ((line = dataReader.readLine()) != null) {

                if (line.startsWith("Password:")) {
                    continue;                    
                }

                System.out.println(line);
            }


            dataReader.close();

            System.out.println("+--------+-----------------+");
            System.out.println("| Choice |     Action      |");
            System.out.println("+--------+-----------------+");
            System.out.println("|   1    | Update Employee |");
            System.out.println("|   2    | Remove Employee |");
            System.out.println("|   3    | Return to Menu  |");
            System.out.println("+--------+-----------------+");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch (choice) {

                case 1:

                    updateEmployeedetails(fileName, fileId);
                    return;

                case 2:

                    deleteEmployee(fileName, fileId);
                    break;

                case 3:

                    return;

                default:

                    System.out.println("Enter Valid Choice !");
                    break;

            }

        } catch (IOException e) {

            System.out.println("Error fetching employee details: " + e.getMessage());

        }

    }

    public void updateEmployeedetails(String fileName, String fileId) {

        try {

            BufferedReader dataReader = new BufferedReader(new FileReader(fileName));
            String line;

            while ((line = dataReader.readLine()) != null) {

                if (line.startsWith("Password:")) {
                    continue;                    
                }

                System.out.println(line);
            }
            dataReader.close();

            Scanner sc = new Scanner(System.in);

            do {

                System.out.println("\nSelect which detail to update:");
                System.out.println("+--------+-----------------+");
                System.out.println("| Choice |     Detail      |");
                System.out.println("+--------+-----------------+");
                System.out.println("|   1    |      Name       |");
                System.out.println("|   2    |   Designation   |");
                System.out.println("|   3    |       DOB       |");
                System.out.println("|   4    | Phone Number    |");
                System.out.println("|   5    | Personal Email  |");
                System.out.println("|   6    |     Address     |");
                System.out.println("|   7    |      Salary     |");
                System.out.println("|   8    |  Return to Menu |");
                System.out.println("+--------+-----------------+");
                System.out.print("Enter your choice: ");

                int choice = sc.nextInt();
                sc.nextLine();

                switch (choice) {
                    case 1:
                        System.out.print("\nEnter new name: ");
                        String newName = sc.nextLine().trim();
                        updateEmployeeName(fileName, newName);
                        break;
                    case 2:
                        System.out.print("\nEnter new designation: ");
                        String newDesignation = sc.nextLine().trim();
                        updateEmployeeDesignation(fileName, newDesignation);
                        break;
                    case 3:
                        boolean validDOB = false;
                        do {
                            System.out.print("\nEnter new DOB (dd-MM-yyyy): ");
                            String newDOB = sc.nextLine().trim();

                            if (isValidDateFormat(newDOB)) {
                                validDOB = true;
                                updateEmployeeDOB(fileName, newDOB);
                            } else {
                                System.out.println("Invalid date format.");
                            }
                        } while (!validDOB);
                        break;
                    case 4:

                        boolean isValidPhone = false;
                        do {
                            System.out.print("\nEnter new phone number: ");
                            String newPhoneNumber = sc.nextLine().trim();

                            if (isValidPhoneNumber(newPhoneNumber)) {
                                isValidPhone = true;
                                updateEmployeePhoneNumber(fileName, newPhoneNumber);
                            } else {
                                isValidPhone = false;
                            }

                        } while (!isValidPhone);
                        break;
                    case 5:
                        System.out.print("\nEnter new personal email: ");
                        String newPersonalEmail = sc.nextLine().trim();
                        updateEmployeePersonalEmail(fileName, newPersonalEmail);
                        break;
                    case 6:
                        System.out.print("\nEnter new address: ");
                        String newAddress = sc.nextLine().trim();
                        updateEmployeeAddress(fileName, newAddress);
                        break;
                    case 7:
                        boolean validSalary = false;
                        do {
                            System.out.print("\nEnter New Salary : ");
                            String newSalary = sc.nextLine();

                            try {
                                Double.parseDouble(newSalary);
                                // Validate salary
                                if (isValidSalary(Double.parseDouble(newSalary))) {
                                    validSalary = true;
                                    updateEmployeeSalary(fileName, newSalary);
                                }

                                else {
                                    System.out.println("Invalid salary amount. Please enter a positive value.");
                                }
                            } catch (NumberFormatException e) {
                                System.out.println("Invalid input. Please enter a valid salary amount.");
                            }
                        } while (!validSalary);
                        break;
                    case 8:
                        System.out.println("Returning to Menu.");
                        return;
                    default:
                        System.out.println("Invalid choice. Returning to menu.");
                        break;
                }
            } while (true);

        } catch (Exception e) {

        }

    }

    public void deleteEmployee(String fileName, String fileId) {

        try {

            String formattedFileName = "database/employeeData" + fileId.toLowerCase() + ".txt";

            Files.deleteIfExists(Paths.get(formattedFileName));

            List<String> idList = Files.readAllLines(Paths.get(DATABASE_FILE));

            idList.remove("Employee ID: KT00" + fileId);
            Files.write(Paths.get(DATABASE_FILE), idList);

            LocalDateTime transactionTime = LocalDateTime.now();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
            String Time = transactionTime.format(formatter);

            BufferedWriter writer = new BufferedWriter(new FileWriter("database/deletedEmployeeData.txt", true));

            writer.write(" [ " + Time + " ] " + " Deleted Employee: KT00" + fileId + "\n");
            writer.close();

            for (int i = Integer.parseInt(fileId) + 1; i <= currentEmployeeCount; i++) {

                String oldFileName = "database/employeeData" + i + ".txt";
                String newFileName = "database/employeeData" + (i - 1) + ".txt";

                Files.move(Paths.get(oldFileName), Paths.get(newFileName), StandardCopyOption.REPLACE_EXISTING);

                updateempdataId(newFileName, "KT00" + (i - 1));
            }

            flagdeleteemp = 1;

            updateEmployeeIDDatabase();

            System.out.println("Employee KT00" + fileId + " deleted successfully.");

        } catch (IOException e) {

            System.out.println("Error deleting employee: " + e.getMessage());

        } finally {

            flagdeleteemp = 0;

        }
    }

    public void addEmployee() {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Name : ");
        this.name = scanner.nextLine();

        System.out.print("Enter Position / Designation : ");
        this.designation = scanner.nextLine();

        boolean validDOB = false;
        do {
            System.out.print("Enter DOB (dd-MM-yyyy) : ");
            this.dob = scanner.nextLine();

            if (isValidDateFormat(this.dob)) {
                validDOB = true;
            } else {
                System.out.println("Invalid date format.");
            }
        } while (!validDOB);


        boolean isValidGender = false;
        do {
            System.out.print("Enter Gender : ");
            this.gender = scanner.nextLine();

            String g = this.gender.toLowerCase();

            if (g.equals("male") || g.equals("female")) {
                isValidGender = true;
            } else {
                System.out.println("Invalid gender. Please enter 'male' or 'female'.");
            }
        } while (!isValidGender);


        boolean isValidPhone = false;
        do {
            System.out.print("Enter Phone Number : ");
            this.phone = scanner.nextLine();

            if (isValidPhoneNumber(this.phone)) {
                isValidPhone = true;
            }

            else {
                isValidPhone = false;
            }

        } while (!isValidPhone);


        System.out.print("Enter Personal Email : ");
        this.personalEmail = scanner.nextLine();

        System.out.print("Enter Address : ");
        this.address = scanner.nextLine();

        
        boolean validSalary = false;
        do {
            System.out.print("Enter Salary : ");
            String salaryInput = scanner.nextLine();

            try {
                this.salaryBase = Double.parseDouble(salaryInput);
                // Validate salary
                if (isValidSalary(this.salaryBase)) {
                    validSalary = true;
                }

                else {
                    System.out.println("Invalid salary amount. Please enter a positive value.");
                }

            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid salary amount.");
            }
        } while (!validSalary);

        
        boolean isValidPass = false;
        do {
            System.out.print("Enter a Password: ");
            this.empPassword = scanner.nextLine();

            if (isValidPassword(this.empPassword)) {
                isValidPass = true;
            }

            else {
                isValidPass = false;
            }

        } while (!isValidPass);


        System.out.println("Employee added Successfully!");

        updateEmployeeIDDatabase();

        createEmployeeDataFile();

    }

    public boolean isValidPassword (String empINPass) {

        if (empINPass.length() < 6 || empINPass.length() > 14) {
            
            System.out.println("Password should be atleast 6 character long and must not exceed 14!");
            return false;
        }

        else {
            return true;
        }
    }

    public boolean isValidDateFormat(String dateStr) {
        SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy");
        sdf.setLenient(false);

        try {

            Date date = sdf.parse(dateStr);
            Calendar cal = Calendar.getInstance();
            cal.setTime(date);
            int day = cal.get(Calendar.DAY_OF_MONTH);
            int month = cal.get(Calendar.MONTH);
            int year = cal.get(Calendar.YEAR);

            if (calculateAge(dob) < 18) {
                System.out.println(" Employee must be an adult. We do not condone child labour.");
                return false;
            }

            if (day < 1 || day > getDaysInMonth(month, year)) {
                return false;
            }

            return true;
        } catch (ParseException e) {
            return false;
        }

    }

    public static int getDaysInMonth(int month, int year) {
        switch (month) {
            case Calendar.JANUARY:
            case Calendar.MARCH:
            case Calendar.MAY:
            case Calendar.JULY:
            case Calendar.AUGUST:
            case Calendar.OCTOBER:
            case Calendar.DECEMBER:
                return 31;
            case Calendar.APRIL:
            case Calendar.JUNE:
            case Calendar.SEPTEMBER:
            case Calendar.NOVEMBER:
                return 30;
            case Calendar.FEBRUARY:
                return (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) ? 29 : 28; // Leap year handling
            default:
                return -1; // Invalid month
        }
    }

    public static boolean isValidPhoneNumber(String phoneNum) {
        if (phoneNum.length() < 10 || phoneNum.length() > 10) {
            System.out.println("Please enter a valid 10 Digit Phone Number!");
            return false;
        } else {
            return true;
        }
    }

    public static boolean isValidSalary(double salary) {
        return salary >= 0;
    }

    public void updateEmployeeIDDatabase() {

        try {

            BufferedReader reader = new BufferedReader(new FileReader(DATABASE_FILE));
            String line = reader.readLine();

            if (line != null && !line.isEmpty()) {

                currentEmployeeCount = Integer.parseInt(line);

            }

            if (flagdeleteemp == 1) {

                currentEmployeeCount--;

            } else {

                currentEmployeeCount++;

            }

            BufferedWriter writer = new BufferedWriter(new FileWriter(DATABASE_FILE));

            writer.write(String.valueOf(currentEmployeeCount));

            writer.close();
            reader.close();

        } catch (IOException e) {

            System.out.println("Error updating employee database: " + e.getMessage());

        }

    }

    private void updateempdataId(String fileName, String newEmployeeId) {

        try {

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Employee ID:")) {

                    line = "Employee ID: " + newEmployeeId;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }
    }

    private void updateEmployeeName(String fileName, String newName) {

        try {

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Name:")) {

                    line = "Name: " + newName;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println("Employee Name Updated!");
    }

    private void updateEmployeeDesignation(String fileName, String newDesignation) {
        try {

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Designation:")) {

                    line = "Designation: " + newDesignation;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println("Employee Designation Updated!");
    }

    private void updateEmployeeDOB(String fileName, String newDOB) {
        try {

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("DOB:")) {

                    line = "DOB: " + newDOB;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println("Employee DOB Updated!");
    }

    private void updateEmployeePhoneNumber(String fileName, String newPhone) {
        try {

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Phone:")) {

                    line = "Phone: " + newPhone;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println("Employee Phone number Updated!");
    }

    private void updateEmployeePersonalEmail(String fileName, String personalEmail) {
        try {

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Personal Email:")) {

                    line = "Personal Email: " + personalEmail;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println("Employee Personal Email Updated!");
    }

    private void updateEmployeeAddress(String fileName, String newAddress) {
        try {

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Address:")) {

                    line = "Address: " + newAddress;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println("Employee Address Updated!");
    }

    private void updateEmployeeSalary(String fileName, String newSalary) {
        try {

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Salary:")) {

                    line = "Salary: " + newSalary;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println("Employee Salary Updated!");
    }

    public void createEmployeeDataFile() {

        String filename = "database/employeeData" + (currentEmployeeCount) + ".txt";

        try {

            BufferedWriter writer = new BufferedWriter(new FileWriter(filename));

            writer.write("Employee ID: KT00" + (currentEmployeeCount) + "\n");
            writer.write("Name: " + name + "\n");
            writer.write("Designation: " + designation + "\n");
            writer.write("DOB: " + dob + "\n");
            writer.write("Gender: " + gender + "\n");
            writer.write("Age: " + calculateAge(dob) + "\n");
            writer.write("Phone: " + phone + "\n");
            writer.write("Personal Email: " + personalEmail + "\n");
            writer.write("Address: " + address + "\n");
            writer.write("Salary: " + salaryBase + "\n");
            writer.write("Password: " + empPassword + "\n");
            writer.close();

        } catch (IOException e) {

            System.out.println("Error creating employee data file: " + e.getMessage());

        }

    }

    public int calculateAge(String dob) {
        int age = -1;

        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy");

            LocalDate birthDate = LocalDate.parse(dob, formatter);

            age = Period.between(birthDate, LocalDate.now()).getYears();
        } catch (DateTimeParseException e) {
            System.out.println("Error parsing date of birth: " + e.getMessage());
        }

        return age;
    }

}

class Employee {

    private static String empName;
    private static String empId;
    private static String empPass;


    public Employee(String empName, String empId, String empPass) {

        this.empName = empName;
        this.empId = empId;
        this.empPass = empPass;
    }


    public void employeeLogin() {

        Scanner sc = new Scanner(System.in);
        System.out.println();
        System.out.println("Please enter your Login Details!");
        System.out.println();
        System.out.print("Enter Employee ID: ");
        empId = sc.nextLine();
        System.out.print("Enter Password: ");
        empPass = sc.nextLine();

        String filePath = "database/employeeData" + empId.substring(4) + ".txt";

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.startsWith("Name:")) {
                    empName = line.substring(line.indexOf(':') + 1).trim();
                }
            }
        }

        catch (IOException e) {
            System.out.println(e);
        }

        if (login(empId, empPass)) {
            System.out.println();
            System.out.println("Login successful. Welcome, " + empName);
            System.out.println();

            promptEmp();
        }

        else {
            System.out.println();
            System.out.println("Invalid Employee ID or Password. Please try again.");
            System.out.println();
        }
    }

    public static boolean login(String empId, String empPass) {

        String filePath = "database/employeeData" + empId.substring(4) + ".txt";
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {

                if (line.contains("Password:")) {
                    String storedPassword = line.substring(line.indexOf(':') + 1).trim();
                    return empPass.equals(storedPassword);
                }
            }
        }

        catch (IOException e) {
            System.out.println("Error reading employee data: " + e.getMessage());
        }

        return false;

    }

    public static void promptEmp () {

        Scanner sc = new Scanner (System.in);

        while (true) {

            System.out.println();

            System.out.println("+--------+-------------------------+");
            System.out.println("| Choice |         Action          |");
            System.out.println("+--------+-------------------------+");
            System.out.println("|   1    | Fetch Details           |");
            System.out.println("|   2    | Update Details          |");
            System.out.println("|   3    | Logout and Exit         |");
            System.out.println("+--------+-------------------------+");

            System.out.print("Enter Choice : ");
            int choice = sc.nextInt();

            switch (choice) {

                case 1:

                    fetchEmpDetails();
                    break;

                case 2:

                    promptUpdate();
                    break;

                case 3:

                    System.out.println("Logging Out...");
                    System.out.println("Exiting...");
                    return;

                default:

                System.out.println("Invalid Choice!");
                break;
            }
        }
    }


    public static void fetchEmpDetails() {
        String fileName = "database/employeeData" + empId.substring(4) + ".txt";

        System.out.println ("+----------------------------------------+");

        BufferedReader dataReader;
        try {
            dataReader = new BufferedReader(new FileReader(fileName));
            String line;

            while ((line = dataReader.readLine()) != null) {

                System.out.println(line);

            }
        } 
        
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
            
         catch (IOException ioe) {
            ioe.printStackTrace();
        }

        System.out.println ("+----------------------------------------+");
    }

    public static void promptUpdate() {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nSelect which detail to update:");
        System.out.println("+--------+-----------------+");
        System.out.println("| Choice |     Detail      |");
        System.out.println("+--------+-----------------+");
        System.out.println("|   1    | Phone Number    |");
        System.out.println("|   2    | Personal Email  |");
        System.out.println("|   3    | Password        |");
        System.out.println("|   4    | Address         |");
        System.out.println("|   5    | Return to Menu  |");
        System.out.println("+--------+-----------------+");
        System.out.print("Enter your choice: ");

        int choice = sc.nextInt();
        sc.nextLine();

        switch (choice) {

            case 1:

                    boolean isValidPhone = false;
                        do {
                            System.out.print("\nEnter new phone number: ");
                            String newPhoneNumber = sc.nextLine().trim();

                            if (isValidPhoneNumber(newPhoneNumber)) {
                                isValidPhone = true;
                                updateEmployeePNum(newPhoneNumber);
                            } else {
                                isValidPhone = false;
                            }

                        } while (!isValidPhone);       
                    break;

            case 2:

                System.out.print("\nEnter a new Personal Email: ");
                String pEmail = sc.nextLine().trim();

                updateEmpPersonalEmail(pEmail);
                break;

            case 3:
                         
                boolean isValidPass = false;
                do {
                    System.out.print("\nEnter a new Password: ");
                    String empPassword = sc.nextLine().trim();
                    
                    if (isValidPassword(empPassword)) {
                        isValidPass = true;
                        if (isValidPass) {
                            updateEmpPass(empPassword);
                        }
                    }
                    
                    else {
                        isValidPass = false;
                    }
                    
                } while (!isValidPass);
                
                
                break;
                
                case 4:
                
                System.out.print("\nEnter a new Address: ");
                String newAddr = sc.nextLine().trim();
                
                updateEmpAddress(newAddr);
                break;

            case 5:

                System.out.println ("Returning to the Main Menu.");
                return;

            default:

                System.out.println ("Invalid Choice!");
                break;
        }
    }

    private static void updateEmployeePNum(String newPhone) {
        try {
            
            String fileName = "database/employeeData" + empId.substring(4) + ".txt";

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Phone:")) {

                    line = "Phone: " + newPhone;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println(empName  + " your Phone number is Updated");
    }

    private static void updateEmpPersonalEmail(String pEmail) {
        try {

            String fileName = "database/employeeData" + empId.substring(4) + ".txt";

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Personal Email:")) {

                    line = "Personal Email: " + pEmail;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println("Employee Personal Email Updated!");
    }


    private static void updateEmpPass(String empPassword) {
        try {

            String fileName = "database/employeeData" + empId.substring(4) + ".txt";

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Password:")) {

                    line = "Password: " + empPassword;

                }
                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println(empName + " your Password has been Updated!");
    }

    private static void updateEmpAddress(String newAddr) {
        try {

            String fileName = "database/employeeData" + empId.substring(4) + ".txt";

            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            StringBuilder content = new StringBuilder();

            String line;

            while ((line = reader.readLine()) != null) {

                if (line.startsWith("Address:")) {

                    line = "Address: " + newAddr;

                }

                content.append(line).append("\n");

            }

            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content.toString());
            writer.close();

        } catch (IOException e) {

            System.out.println("Error updating employee data inside file: " + e.getMessage());

        }

        System.out.println();
        System.out.println("Employee Address Updated!");
    }

    public static boolean isValidPhoneNumber(String phoneNum) {
        if (phoneNum.length() < 10 || phoneNum.length() > 10) {
            System.out.println("Please enter a valid 10 Digit Phone Number!");
            return false;
        } else {
            return true;
        }
    }

    public static boolean isValidPassword (String empINPass) {

        if (empINPass.length() < 6 || empINPass.length() > 14) {
            
            System.out.println("Password should be atleast 6 character long and must not exceed 14!");
            return false;
        }

        else {
            return true;
        }
    }
}

public class process {
    public static void main(String[] args) {

        checkAndCreateFiles();
        Scanner sc = new Scanner(System.in);

        admin A = new admin();
        Employee E = new Employee(null, null, null);

        int choice = 0;

        System.out.println("Welcome to Employee Management System");

        while (true) {

            System.out.println("Please select your role:");
            System.out.println("+--------+-----------------+");
            System.out.println("| Choice |      Role       |");
            System.out.println("+--------+-----------------+");
            System.out.println("|   1    |     Admin       |");
            System.out.println("|   2    |     Employee    |");
            System.out.println("|   3    |     Exit        |");
            System.out.println("+--------+-----------------+");

            System.out.print("Enter Choice : ");
            choice = sc.nextInt();

            switch (choice) {

                case 1:

                    A.AdminLogin();
                    break;

                case 2:

                    E.employeeLogin();
                    break;

                case 3:

                    System.out.println("Exiting...");
                    System.exit(0);
                    break;

                default:

                    System.out.println("Invalid Choice!");
                    break;
            }

        }
    }

    public static void checkAndCreateFiles() {
        
        String DATABASE_PATH = "database";
       String DATABASE_FILE = "database/employeeid.txt";

        File db = new File(DATABASE_PATH);
        File emptxt = new File(DATABASE_FILE);
        
        try {
            if (!db.exists()) {
                boolean created = db.mkdir();
                if (!created) {
                    System.out.println("Failed to create " + db + ".");
                }
            }

            if (!emptxt.exists()) {
                boolean created = emptxt.createNewFile();
                if (!created) {
                    System.out.println("Failed to create " + emptxt + ".");
                }
            }

        } catch (IOException e) {
            System.out.println("An error occurred while creating files: " + e.getMessage());
        }
    }
}