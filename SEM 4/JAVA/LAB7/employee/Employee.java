// package LAB_7.employee;

import java.util.Scanner;

public class Employee {
    String empName, empGender;

    void inputData(String name, String gender) {
        this.empName = name;
        this.empGender = gender.toLowerCase();
    }

    void showData(){
        System.out.println("Name: " + empName);
        System.out.println("Gender: " + empGender);
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Employee name: ");
        String empName = sc.nextLine();
        System.out.println("Enter Employee Gender: ");
        String empGender = sc.nextLine();
        System.out.println("Enter Employee salary: ");
        double empSalary = sc.nextDouble();
        
        SalariedEmployee emp = new SalariedEmployee();
        emp.inputData(empName, empGender);
        emp.setSalary(empSalary);
        emp.grossSalary();

        sc.close();
    }
}

class SalariedEmployee extends Employee {
    double empSalary, HRA, DA, finalPay;
    
    void setSalary(double empSalary) { this.empSalary = empSalary; }

    void allownce() {
        if (empGender.equals("female")) {
            HRA = 0.1 * empSalary;
            DA = 0.05 * empSalary;
        } else {
            HRA = 0.09 * empSalary;
            DA = 0.05 * empSalary;
        }
        finalPay = HRA + DA + empSalary;
    }

    void grossSalary() {
        allownce();
        System.out.println("Employee salary: " + finalPay);
    }
}

