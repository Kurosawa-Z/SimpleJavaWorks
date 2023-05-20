import java.util.Scanner;

public class Main2 {
      public static void main (String[] args){
      Scanner input = new Scanner (System.in);
      System.out.print("What is your Name? " + "");
      String name = input.next();
      System.out.print("What your Age? " + "");
      String age = input.next();
      System.out.print("What is your Grade and Section" + ""); 
      String grade = input.next();
      System.out.print("What is your School Name: " + ""); 
      String school = input.next();
      System.out.print("What your Teacher Name: " + ""); 
      String teacher = input.next();

      System.out.println(); 
      System.out.println(name + "/n" + age + "/n" + grade + "/n" + school + "/n" + teacher + "/n");
    }
}
      
      
