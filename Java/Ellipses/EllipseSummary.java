/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ssd1.wk02;
import java.util.ArrayList;
/**
 *
 * @author Bryan Guzmsn
 * @version 1.0
 */
public class EllipseSummary {

    /**
     * Global variables that will be used throughout the class
     */
    private int count;
    private Ellipse newEllipse;
    private double totalArea = 0;
    ArrayList<Ellipse> ellipseContainer = new ArrayList();
    
    /**
     * Constructor creates an ArrayList of type Ellipse
     * The ArrayList is used to hold all of the Ellipse Objects
     */
    public EllipseSummary()
    {
    }

    /**
     *
     *
     * @param a Takes an Ellipse object as a parameter puts that object into an
     * array Updates count by 1 Updates totalArea by the area of the ellipse
     * added
     */
    public void addEllipse(Ellipse a) {
        ellipseContainer.add(a);
        count++;
        totalArea += a.getArea();
    }

    /**
     * Count was updated each time an ellipse was added using the addEllipse
     * method
     *
     * @return count
     */
    public int totalEllipses() {
        return count;
    }

    /**
     * TotalArea was updated in the for loop each time an ellipse was added
     * using addEllipse
     *
     * @return totalArea
     */
    public double totalArea() {
        return totalArea;
    }

    /**
     * Finds the largest Ellipse and returns its area
     *
     * @return largest area
     */
    public double largestArea() {
        double largest = Double.MIN_VALUE;
        double temp;

        for (Ellipse ellipse : ellipseContainer) {
            temp = ellipse.getArea();
            if (temp > largest) {
                largest = temp;
            }
        }
        return largest;
    }

    /**
     * finds the largest ellipse and returns its color
     *
     * @return largest ellipse's color
     */
    public String largestColor() {
        double largest = Double.MIN_VALUE;
        double temp;
        int hold = Integer.MIN_VALUE;

        for(int c = 0; c < ellipseContainer.size(); c++)
        {
            temp = ellipseContainer.get(c).getArea();
            if(temp > largest)
            {
                largest = temp;
                hold = c; 
            }
        }
        return ellipseContainer.get(hold).getColor();
    }

    /**
     * Returns the number of blue ellipses
     *
     * @return #of blue ellipses
     */
    public int blueEllipses() {
        int bCount = 0;

        for (Ellipse color : ellipseContainer) {
            if (color.getColor().equals("blue")) {
                bCount++;
            }
        }
        return bCount;
    }

    @Override
    public String toString() {
        return ("Number of Ellipses: " + totalEllipses() + 
                "\nTotal Area of Ellipses: " + totalArea() + 
                "\nArea of the Largest Ellipse " + largestArea() + 
                "\nColor of the largest Ellipse " + largestColor() 
                + "\nNumber of Blue Ellipses " + blueEllipses());
    }
}
