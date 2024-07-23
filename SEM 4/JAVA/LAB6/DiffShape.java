import java.util.Scanner;

abstract class Shape {
    abstract void area();
    Scanner sc = new Scanner(System.in);
}

class Circles extends Shape {
    private double radius;

    @Override
    void area() {
        System.out.println("Enter radius: ");    
        radius = sc.nextDouble();
        System.out.println("Area of Circle is: " + (Math.PI * radius * radius));
    }
}

class Triangles extends Shape {
    double height, base;
    
    @Override
    void area() {
        System.out.println("Enter height and Base: ");
        height = sc.nextDouble();
        base = sc.nextDouble();
        System.out.println("Area of Triangle is " + ((height * base)) / 2);
    }
}

class Square extends Shape {
    double side;

    @Override
    void area() {
        System.out.println("Enter side: ");
        side = sc.nextDouble();
        System.out.println("Area of Square is: " + side * side);
    }
}

public class DiffShape {
    public static void main(String[] args) {
        Shape sp = new Circles();
        sp.area();

        sp =  new Square();
        sp.area();

        sp = new Triangles();
        sp.area();

    }
}
