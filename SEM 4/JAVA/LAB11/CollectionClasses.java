// package LAB11;

import java.util.ArrayList;
import java.util.Stack;
import java.util.Vector;

public class CollectionClasses {

    public static void main(String[] args) {

        // *Stack

        Stack<Integer> stack = new Stack<>();
        System.out.println("Demonstrating Stack:");
        stack.push(11);
        stack.push(12);
        stack.push(13);
        System.out.println("Stack: " + stack);

        System.out.println("Top element (peek): " + stack.peek());

        System.out.println("Popped element: " + stack.pop());
        System.out.println("Stack after pop: " + stack);
        System.out.println();

        // * Vector

        Vector<Integer> vector = new Vector<>();
        System.out.println("Demonstrating Vector:");
        vector.add(11);
        vector.add(12);
        vector.add(13);
        System.out.println("Vector: " + vector);

        System.out.println("Element at index 1: " + vector.get(1));

        vector.remove(1);
        System.out.println("Vector after removing element at index 1: " + vector);
        System.out.println();

        // * ArrayList

        ArrayList<Integer> arrayList = new ArrayList<>();
        System.out.println("Demonstrating ArrayList:");
        arrayList.add(11);
        arrayList.add(12);
        arrayList.add(13);
        System.out.println("ArrayList: " + arrayList);

        System.out.println("Element at index 0: " + arrayList.get(0));

        arrayList.remove(0);
        System.out.println("ArrayList after removing element at index 0: " + arrayList);
    }
}
