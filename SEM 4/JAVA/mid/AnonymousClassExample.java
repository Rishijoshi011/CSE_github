// public class AnonymousClassExample {

//     static class Dog {
//         void bark(){
//             System.out.println("Dog Barks");
//         }
//     }

//     public static void main(String[] args){

//         Dog d1 = new Dog(){
//             @Override
//             void bark(){ System.out.println("cat meows");}
//         };
//         d1.bark();
//     }
// }

// public class AnonymousClassExample {

//     interface Animal { void makeSound(); }

//     public static void main(String[] args) {

//         Animal dog = new Animal() {
//             @Override
//             public void makeSound(){ System.out.println("Dog barks");}
//         };
//         dog.makeSound();
//     }
// }

abstract class Animal {
    abstract void bark();
}

public class AnonymousClassExample{

    public static void main(String[] args) {
        Animal dog = new Animal(){
            @Override
            void bark(){
                System.out.println("Dog barks..");
            }
        };
        dog.bark();
    }
}