import java.util.Scanner;

class NoMatchException extends Exception {
    NoMatchException(String str){
        super("It's a diffrent string");
    }
}

public class Demo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter an String");
        String str = sc.next();
        final String MATCH = "India"; 

        try {
            if (!str.equals(MATCH)) { throw new NoMatchException(str); }
        } catch (Exception ex) {
            System.err.println(ex);
        }

        sc.close();
    }
}
