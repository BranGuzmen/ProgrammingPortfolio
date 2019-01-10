package csi403;
/**
* NUMBER OF POINTS WITHIN A POLYGON
*
*
* This program will calculate the number of points within a set of coordinates forming a polygon. If the set of coordinates do not form
* a polygon, then the program will not output the correct answer. The size of the polygon is limited to a 19x19 grid; this can be changed 
* by altering a nested for-loop found within the pointsWithin function. 
*
* @author Bryan Guzmen
* @version 1.0
* ID 001265918
* CSI403-Project04
**/


// Import required Java libraries
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.json.*;
import java.util.*;

//Will be used to represent coordinate points on a grid
class Point {
    public int x;
    public int y;

    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}

// Extend HttpServlet class
public class JsonService extends HttpServlet {

    // Standard servlet method
    public void init() throws ServletException {
        // Do any required initialization here - likely none
    }

    // Standard servlet method - we will handle a POST operation
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doService(request, response);
    }

    // Standard servlet method - we will not respond to GET
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Set response content type and return an error message
        response.setContentType("application/json");
        PrintWriter out = response.getWriter();
        out.println("{ 'message' : 'Use POST!'}");
    }

    // Our main worker method
    private void doService(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Get received JSON data from HTTP request
        BufferedReader br = new BufferedReader(new InputStreamReader(request.getInputStream()));
        String jsonStr = "";
        String test = "";
        JsonArray inArray;

        // Set response content type to be JSON
        response.setContentType("application/json");
        PrintWriter out = response.getWriter();

        //Continue reading json string until it reaches the end
        while((test = br.readLine()) != null){
            //Make sure null is not added on to jsonStr
            if(test != null){
                jsonStr += test;
            }
        }
        try {
            //Create a JsonArray from jsonStr
            StringReader strReader = new StringReader(jsonStr);
            JsonReader reader = Json.createReader(strReader);
            JsonObject obj = reader.readObject();
            inArray = obj.getJsonArray("inList");
        }
        catch (Exception e){
            out.print("{\"Error\" : \"Malformed JSON\"}");
            return;
        }

        // Adds all JsonObjects to the LinkedList
        LinkedList<JsonObject> list = new LinkedList<JsonObject>();

        if(inArray == null){
            out.print("{\"Error\" : \"Empty JSON message sent\"}");
            return;
        }
        else if(inArray.size() < 3){
            out.print("{\"Error\" : \"Not enough coordinates provided\"}");
            return;
        }
        else{
            int len = inArray.size();
            Point[] points = new Point[len];
            try{
                //Iterate over inArray and store in a linked list of Json Objects
                for(int i = 0; i < inArray.size(); i++) {
                    list.add(inArray.getJsonObject(i));
                }
            }
            catch(Exception e){
                out.print("{\"Error\" : \"Failed to add to list\"}");
                return;
            }

            try{
                //Takes list and converts them to individual points in an array stored in points array
                for (int i = 0; i < inArray.size(); i++) {
                    points[i] = new Point(list.get(i).getInt("x"), list.get(i).getInt("y"));
                }
            }
            catch(Exception e){
                out.print("{\"Error\" : \"Failed to add to points\"}");
                return;
            }

            //Print what pointsWithin returns in JSON format
            out.println("{ \"count\" : " + pointsWithin(points) + "}");

        }
    }

    // Standard Servlet method
    public void destroy() {
        // Do any required tear-down here, likely nothing.
    }
    

    public static int pointsWithin(Point[] points) {
        Point tempPoint;
        int count = 0;

        //Run through each point on a 19x19 grid
        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                tempPoint = new Point(i, j);

                //If the point generated is contained in the boundary
                if (isContained(tempPoint, points) == true) {
                    //Add it to the linked list
                    //list.add(tempPoint);
                    count++;
                }
            }
        }
        return count;
    }


    public static boolean isContained(Point test, Point[] points) {
        int i, j;
        boolean result = false;

        //Check for intersections
        for (i = 0, j = points.length - 1; i < points.length; j = i++) {
            if ((points[i].y > test.y) != (points[j].y > test.y)
                    && (test.x < (points[j].x - points[i].x) * (test.y - points[i].y) / (points[j].y - points[i].y) + points[i].x)) {
                result = !result;
            }
        }

        //If the point is on the line flag true
        if (isPointOnLine(test, points) == true) {
            //Otherwise it is false
            result = false;
        }
        return result;
    }

    public static boolean isPointOnLine(Point test, Point[] points) {
        Point point1, point2;
        int dX, dY, x, y, cross;

        //Iterate over all the points and assign them
        for (int i = 0; i < points.length; i++) {
            //Assign pointA to the index of i
            point1 = points[i];
            //If i is equal to the length - 1
            if (i == points.length - 1) {
                //Then assign pointB to the first index
                point2 = points[0];
                //otherwise
            } else {
                //Assign point b
                point2 = points[i + 1];
            }

            //Get the difference between points
            dX = test.x - point1.x;
            dY = test.y - point1.y;

            //Difference between x & y
            x = point2.x - point1.x;
            //Get the difference between the value of y for pointB and the value of y for pointA
            y = point2.y - point1.y;

            //Calculate the cross
            cross = dX * y - dY * x;

            //If it is zero than the point is on the line
            if (cross == 0) {
                //Flag the point as true and return the result
                return true;
            }
        }
//Otherwise return that is is not on the line
        return false;
    }
}