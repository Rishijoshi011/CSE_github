import java.util.LinkedList;
import java.util.Scanner;


class A {
    int a = 11;

    public void display(){
        System.out.println(a);
    }
}


class B extends A{
     int a = 7;

    public void display(){
        System.out.println(a);
    }

}

public class ArrayListCollectionClass {
    public static void main(String[] args) {
        A a = new B();
        System.out.println(a.a);

        Scanner sc = new Scanner(System.in);
    //     LinkedList<String> al = new LinkedList<>();        

    //     System.out.println("Enter -1 to stop: ");
    //     while (true) {
    //         System.out.println("Enter Element: ");
    //         String element = sc.nextLine();
    //         if (element.equals("exit")) { break; } else { al.add(element); }
    //     }
    //     System.out.println("size of an Array: " + al.size());
        
    //     System.out.println("Elements are: ");
    //     for(int i = 0; i != al.size(); i++) {
    //         System.out.print(al.get(i) + " ");
    //     }

    //     sc.close();
    }
}