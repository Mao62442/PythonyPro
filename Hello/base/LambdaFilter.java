import java.util.List;
import java.util.Arrays;
import java.util.stream.Collectors;

public class LambdaFilter {
    public static void main(String[] args) {
        
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve", "Frank");

        // Using lambda expression to filter names that start with 'A'
        List<String> filteredNames = names.stream()
                .filter(name -> name.startsWith("A"))
                .collect(Collectors.toList());

        // Print the filtered names
        System.out.println(filteredNames); // Output: [Alice]

        Animal dog = new Dog();
        Animal cat = new Cat();
        dog.makeSound(); // Output: Bark
        cat.makeSound(); // Output: Meow
        printClassName(cat);
        printClassName(dog);
        
    }

    public static void printClassName(Animal animal) {
        System.out.println("The class name is " + animal.getClass().getSimpleName() + ".");
    }
}