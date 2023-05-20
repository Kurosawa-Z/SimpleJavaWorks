import java.util.Scanner;

public class Main5 {
      public static void main (String[] args){
      Scanner input = new Scanner (System.in);
      System.out.print("What is your Name? ");
      String name = input.next();
      System.out.print("What your Age? ");
      String age = input.next();
      System.out.print("What Grade and Section are you? "); 
      String grade = input.next();
      System.out.print("Why did you choose programming? "); 
      String reason = input.next();
      System.out.print("Name of your school: "); 
      String school = input.next();
      System.out.print("What is your Teacher name? "); 
      String teacher = input.next();
 
      System.out.println();
      System.out.println();
      System.out.println("hello " + "\n" + "Your name is " + name + "\n" + "then you are " + age + "\n" + "your are " + grade + "\n" + "you choose programming because " + reason + "\n" + "your school name is " + school + "\n" + "your teacher is " + teacher);
     }
}