/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ssd1.wk02;

/**
 *@import Scanner
 * @author Bryan Guzman
 * @version 2.0
 */

public class EllipeseDemo {
    /**
     * 
     * All that is here for now is a main method that fills an
     * ArrayList of type Ellipse
     */
    public static void main(String[] args)
    { 
            Ellipse a = new Ellipse(7,5,"green");
            Ellipse b = new Ellipse(10,8,"blue");
            Ellipse c = new Ellipse(22,16,"yellow");
            Ellipse d = new Ellipse(44,22,"blue");
        
            EllipseSummary container = new EllipseSummary();
        
            container.addEllipse(a);
            container.addEllipse(b);
            container.addEllipse(c);
            container.addEllipse(d);
        
            System.out.println(container);
            
    
    }
    
    
}
