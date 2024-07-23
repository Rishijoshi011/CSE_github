import java.util.Scanner;


interface Shape2D {
    void getArea();
}

abstract class Shape {
    abstract void display();
}

class Circle extends Shape implements Shape2D {
    double area;

    @Override
    public void getArea() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter radius: ");
        double radius = sc.nextDouble(); 

        area = (Math.PI * radius * radius);
        sc.close();
    }
    
    @Override
    void display() {
        System.out.println("Area of Circle is: " + area);
    }
}

public class Dimentional {
    public static void main(String[] args) {
        Circle cir = new Circle();
        cir.getArea();
        cir.display();
    }
}
