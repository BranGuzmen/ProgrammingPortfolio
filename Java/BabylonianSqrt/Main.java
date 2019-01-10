/**
 * User inputs a value and it finds an aproximation of the sqrt
 * 
 * Bryan Guzman
 * Lab Monday 2:45-3:40
 * Version 1.0
 */

import java.util.Scanner;
public class Main
{
    public static void main(String[] args)
    {  
       babSqrt();//keeps the main method simple 
    }
    
    public static void babSqrt()
    {
        double input;//the number the user wants to sqrt
        double accurate = 0.001;//how accurate we want our answer
        double diff = Double.MAX_VALUE;//holds the maxiumum value of the (guess - lastGuess)/lastGuess
        
        Scanner kb = new Scanner(System.in);
        System.out.println("Enter a number you wish to find the square root of");
        input = kb.nextInt();//stores user input in the variable input        
        
        double guess = input/2;//find an approximation of the sqrt
        double lastGuess = guess;//stores our guess value from above in a new variable
        
        if(input < 0)//a check to make sure the user does not enter a negative
        {
            System.out.println("You've entered a negative number");
            babSqrt();//runs this method again so that the user can enter a new number
        }
        if(input == 0)//a second check for if the user enters a 0
        {
            System.out.println("Your answer is: 0");
            System.exit(0);//closes and ends the program once the if statement is done
        }
        
        while(Math.abs(diff) > accurate)//while diff is greater than 0.001 it will stay in this loop
        {
            double r = input/guess;//math is being done here
            guess = (guess + r) / 2; 
            diff = ((guess - lastGuess)/lastGuess);
            lastGuess = guess;//resets the value of lastGuess so that it can find a more accurate answer
        }
        
        System.out.printf("Your answer is: %.4f", lastGuess);//formats the answer to 4 decimal places
        System.exit(0);//closes the terminal window once the method is completed 
    }
}