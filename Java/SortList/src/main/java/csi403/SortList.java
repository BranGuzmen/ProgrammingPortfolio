package csi403;
/**
* SORT LIST
*
*
* Sorts a POST of an integer array and returns a sorted array.
*
* @author Bryan Guzman
* @version 1.0
* ID 001265918
* CSI 403-Project01
**/

// Import required java libraries
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.json.*;



// Extend HttpServlet class
public class SortList extends HttpServlet {

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
      doService(request, response); 
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


  // Our main worker method
  // Parses messages e.g. {"inList" : [5, 32, 3, 12]}
  // Returns the list reversed.   
  private void doService(HttpServletRequest request,
                    HttpServletResponse response)
            throws ServletException, IOException
  {
      // Get received JSON data from HTTP request
      BufferedReader br = new BufferedReader(new InputStreamReader(request.getInputStream()));
      String jsonStr = "";
      if(br != null){
          jsonStr = br.readLine();
      }
      
      // Create JsonReader object
      StringReader strReader = new StringReader(jsonStr);
      JsonReader reader = Json.createReader(strReader);

      try {
          // Get the singular JSON object (name:value pair) in this message.
          JsonObject obj = reader.readObject();
          // From the object get the array named "inList"
          JsonArray inArray = obj.getJsonArray("inList");

          // Sort the data in the list

          int[] temp = new int[inArray.size()];
          for (int z = 0; z < temp.length; z++) {
              temp[z] = inArray.getInt(z);
          }
          final long startTime = System.currentTimeMillis();
          for (int i = 1; i < temp.length; i++) {
              int k = temp[i];
              int j = i - 1;

          /* Elements are moved array[0..i-1] that are greater than key,
             to one position ahead of their current position*/
              while (j >= 0 && temp[j] > k) {
                  temp[j + 1] = temp[j];
                  j = j - 1;
              }
              temp[j + 1] = k;
          }
          final long endTime = System.currentTimeMillis();

          JsonArrayBuilder outArrayBuilder = Json.createArrayBuilder();
          for (int c = 0; c < temp.length; c++) {
              outArrayBuilder.add(temp[c]);
          }

          // Set response content type to be JSON
          response.setContentType("application/json");
          // Send back the response JSON message
          PrintWriter out = response.getWriter();
          out.println("{ \"outList\" : " + outArrayBuilder.build().toString() + ",\n\"algorithm\" : \"Insertion Sort\",\n\"timeMS\" : " + (endTime - startTime) + " }");
      }
      catch (Exception E){
          response.setContentType("application/json");
          PrintWriter err = response.getWriter();
          err.println("{ \"Error\" : \"Malformed JSON\" }");
      }

  }

    
  // Standard Servlet method
  public void destroy()
  {
      // Do any required tear-down here, likely nothing.
  }
}

