import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class MedicalBillingSystem extends JFrame {
    private ArrayList<Patient> patients;
    private ArrayList<MedicalService> services;

    private JTextField patientNameField;
    private JComboBox<String> serviceComboBox;
    private JTextArea billTextArea;

    public MedicalBillingSystem() {
        patients = new ArrayList<>();
        services = new ArrayList<>();
        
        // Sample medical services
        services.add(new MedicalService("Consultation", 50));
        services.add(new MedicalService("X-ray", 100));
        services.add(new MedicalService("Blood Test", 80));

        setTitle("Medical Billing System");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 2));

        panel.add(new JLabel("Patient Name:"));
        patientNameField = new JTextField();
        panel.add(patientNameField);

        panel.add(new JLabel("Select Service:"));
        serviceComboBox = new JComboBox<>();
        for (MedicalService service : services) {
            serviceComboBox.addItem(service.getName());
        }
        panel.add(serviceComboBox);

        JButton addButton = new JButton("Add Service");
        addButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                addService();
            }
        });
        panel.add(addButton);

        JButton generateBillButton = new JButton("Generate Bill");
        generateBillButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                generateBill();
            }
        });
        panel.add(generateBillButton);

        billTextArea = new JTextArea();
        panel.add(billTextArea);

        add(panel);
        setVisible(true);
    }

    private void addService() {
        String patientName = patientNameField.getText();
        String selectedService = (String) serviceComboBox.getSelectedItem();
        for (Patient patient : patients) {
            if (patient.getName().equals(patientName)) {
                for (MedicalService service : services) {
                    if (service.getName().equals(selectedService)) {
                        patient.addService(service);
                        break;
                    }
                }
                return;
            }
        }
        // If patient doesn't exist, create a new one
        Patient newPatient = new Patient(patientName);
        patients.add(newPatient);
        for (MedicalService service : services) {
            if (service.getName().equals(selectedService)) {
                newPatient.addService(service);
                break;
            }
        }
    }

    private void generateBill() {
        StringBuilder bill = new StringBuilder();
        for (Patient patient : patients) {
            bill.append("Patient: ").append(patient.getName()).append("\n");
            double totalCost = 0;
            for (MedicalService service : patient.getServices()) {
                bill.append("- ").append(service.getName()).append(": $").append(service.getCost()).append("\n");
                totalCost += service.getCost();
            }
            bill.append("Total: $").append(totalCost).append("\n\n");
        }
        billTextArea.setText(bill.toString());
    }

    // Method to add a new medical service
    private void addMedicalService(String name, double cost) {
        services.add(new MedicalService(name, cost));
        serviceComboBox.addItem(name);
    }

    // Method to add a new patient
    private void addPatient(String name) {
        patients.add(new Patient(name));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new MedicalBillingSystem();
            }
        });
    }
}

class Patient {
    private String name;
    private ArrayList<MedicalService> services;

    public Patient(String name) {
        this.name = name;
        services = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public void addService(MedicalService service) {
        services.add(service);
    }

    public ArrayList<MedicalService> getServices() {
        return services;
    }
}

class MedicalService {
    private String name;
    private double cost;

    public MedicalService(String name, double cost) {
        this.name = name;
        this.cost = cost;
    }

    public String getName() {
        return name;
    }

    public double getCost() {
        return cost;
    }
}