//week 1 Example
package ssd1.wk01;

import javax.swing.JOptionPane;

/**
 *
 * @author peterrosner
 */
public class Example {
    private static int age;

    public static void main(String[] args) {
        int myvar;
        myvar = 10;
        System.out.println("1 - myvar = " + myvar);
        myvar = 5;
        System.out.println("2 - myvar = " + myvar);
        myvar = myvar * 3;
        myvar -= 4;
        System.out.println("3 - myvar = " + myvar);
        askAges();
    }
        
       public static void askAges()
       {
        String myVarString = JOptionPane.showInputDialog("Enter an age");
        age = Integer.parseInt(myVarString);
        if(age > 7)
        {
            age = 7;
        }
        
        for(int c = 0; c < age; c++)
        {
           String askAge = JOptionPane.showInputDialog("Enter an age");
           age = Integer.parseInt(askAge);
           if(age < 13)
           {
               System.out.println("Child");
           }
           if(age > 13 && age < 18)
           {
               System.out.println("Youth");
           }
           if(age > 18)
           {
               System.out.println("Adult");
           }
        }
     }   
}       
 

