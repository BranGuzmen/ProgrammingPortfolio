package csi403;
/**
* PRIORITY QUEUE
*
*
* Program will receive a POST of an array containing a series of commands along with integers representing the priority. Commands will determine 
* the action taken with each object and the integer is used to place an object into the list. As each command is ran the program will send a 
* response detailing the command and actions taken. The only time the integer value is needed is when the "enqueue" command is requested; otherwise
* the integer value will be disregarded. Once at the end of the POSTed array, the program will out put what remains in the priority queue. 
*
* @author Bryan Guzman
* @version 1.0
* ID 001265918
* CSI403-Project02
**/

// Import required java libraries
import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.json.*;

// Extend HttpServlet class
public class Project02 extends HttpServlet {

  // Standard servlet method 
  public void init() throws ServletException
  {
      // Do any required initialization here - likely none
  }

  // Standard servlet method - we will handle a POST operation
  public void doPost(HttpServletRequest request,
                    HttpServletResponse response)
            throws ServletException, IOException
  {
      // Catch exceptions
      try
      {
          doService(request, response);
      }
      catch(Exception e)
      {
          response.setContentType("application/json");
          PrintWriter out = response.getWriter();
          out.println("{ \"message\" : \"Malformed JSON\"}");
      }
  }

  // Standard servlet method - we will not respond to GET
  public void doGet(HttpServletRequest request,
                    HttpServletResponse response)
            throws ServletException, IOException
  {
      // Set response content type and return an error message
      response.setContentType("application/json");
      PrintWriter out = response.getWriter();
      out.println("{ 'message' : 'Use POST!'}");
  }


  private void doService(HttpServletRequest request,
                    HttpServletResponse response)
            throws ServletException, IOException
  {
      // Set response content type to be JSON
      response.setContentType("application/json");
      // Send back the response JSON message
      PrintWriter out = response.getWriter();

      // Get received JSON data from HTTP request
      BufferedReader br = new BufferedReader(new InputStreamReader(request.getInputStream()));
      String jsonStr = "";
      /*if(br != null){
          jsonStr = br.readLine();
      }
      
      // Create JsonReader object
      StringReader strReader = new StringReader(jsonStr);
      JsonReader reader = Json.createReader(strReader);

      // Get the singular JSON object (name:value pair) in this message.    
      JsonObject obj = reader.readObject();
      // From the object get the array named "inList"
      JsonArray inArray = obj.getJsonArray("inList");*/

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

      Comparator<Job> comparator = new JobComparator();
      PriorityQueue<Job> pQueue = new PriorityQueue<>(inArray.size(),comparator);
      String name;
      int pri;

      for(int i=0; i < inArray.size(); i++){
          if(inArray.getJsonObject(i).getString("cmd").equals("enqueue")) {
              name = inArray.getJsonObject(i).getString("name");
              pri = inArray.getJsonObject(i).getInt("pri");
              if(pri < 0){
                  out.println("{ \"message\" : \"Priority < zero\"}");
                  return;
              }
              pQueue.add(new Job(name, pri));
          }
          else if(inArray.getJsonObject(i).getString("cmd").equals("dequeue")){
              if(pQueue.poll() == null){
                  out.println("{ \"message\" : \"Dequeued empty priority queue\"}");
                  return;
              }
          }
          else {
              out.println("{ \"message\" : \"Malformed JSON\"}");
              return;
          }
      }

      // Build array for printing
      JsonArrayBuilder outArrayBuilder = Json.createArrayBuilder();
      int size = pQueue.size();
      for (int i = 0; i < size; i++) {
          outArrayBuilder.add(pQueue.poll().getJobName());
      }

      //Print results
      out.println("{ \"outList\" : " + outArrayBuilder.build().toString() + "}");

  }
    
  // Standard Servlet method
  public void destroy()
  {
      // Do any required tear-down here, likely nothing.
  }
}

