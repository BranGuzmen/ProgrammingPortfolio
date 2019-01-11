/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ssd1.wk02;

/**
 *
 * @author Bryan Guzman
 * @version 1.0
 */
public class Ellipse {
    private int semiMajorRadius;
    private int semiMinorRadius;
    private String color;
    
    /*
    *constructor for ellipse class
    *takes in the three variable semiMinor, semiMajor and color
    *sets those three variables equal to their corresponding variables
    */
    public Ellipse(int semiMinor, int semiMajor, String color)
    {
        this.semiMajorRadius = semiMajor;
        this.semiMinorRadius = semiMinor;
        this.color = color;
    }
    
    /*
    *Series of get methods for semiMajorRadius, semiMinorRadius and color
    *Returns the values of each variable when called
    */
    public int getSemiMajorRadius()
    {
        return semiMajorRadius;
    }
    
    public int getSemiMinorRadius()
    {
        return semiMinorRadius;
    }
    
    public String getColor()
    {
        return color;
    }
    /*
    *Calculates the area of the ellipse
    *Uses semiMajorRadius, semiMinorRadius and Math.PI
    *Takes the int values and casts them to become a double and return a doble
    */
    public double getArea()
    {
        return (double)(Math.PI*semiMajorRadius*semiMinorRadius);
    }
    
    @Override
    public String toString()
    {
        return ("Semi Major Radius = " + semiMajorRadius + "\nSemi Minor Radius = " + semiMinorRadius + "\nArea = " + getArea() + "\nColor = " + color);
    }
}
