package csi403;
/**
 * HASH ALGORITHM
 *
 *
 * Receive a POST of strings and run a hash algorithm on strings to determine which strings contain equivalent characters. 
 * Strings containing characters in the same order appearing multiple times will be disregarded. 
 *
 * @author Bryan Guzman
 * @version 1.0
 * ID 001265918
 * CSI403-Project03
 */
// Import required java libraries
import javax.json.*;
import javax.json.JsonArrayBuilder;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;
import java.util.*;

// Extend HttpServlet class
public class JsonService extends HttpServlet {

    // Standard servlet method
    public void init() throws ServletException {
        // Do any required initialization here - likely none
    }

    // Standard servlet method - we will handle a POST operation
    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doService(request, response);
    }

    // Standard Servlet method
    public void destroy() {
        // Do any required tear-down here, likely nothing.
    }

    // Standard servlet method - we will not respond to GET
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // Set response content type and return an error message
        response.setContentType("application/json");
        PrintWriter out = response.getWriter();
        // We can always create JSON by hand just concating a string.
        out.println("{ 'message' : 'Use POST!'}");
    }

    // Our main worker method
    private void doService(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        List<String> inList = new ArrayList<String>();

        // Get received JSON data from HTTP request
        BufferedReader br = new BufferedReader(new InputStreamReader(request.getInputStream()));
        String jsonStr = "";
        /*if(br != null){
            jsonStr = br.readLine();
        }
        try {
            StringReader strReader = new StringReader(jsonStr);
            JsonReader reader = Json.createReader(strReader);

            JsonObject inListJson = reader.readObject();
            JsonArray inListArray = inListJson.getJsonArray("inList");

            for(int i = 0; i < inListArray.size();i++){
                inList.add(inListArray.getString(i));
            }
        }
        catch(Exception e){
            response.setContentType ("application/json");
            PrintWriter out = response.getWriter();
            out.println("{\"message\" : \"Error - Malformed JSON\"}");
        }*/

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

        for(int i = 0; i < inListArray.size(); i++){
            inList.add(inListArray.getString(i));
        }


        //hashed values from strings in inList
        int[] hashValue = Arrays.copyOf(HashAlg.hashAlg(inList), inList.size());

        JsonArrayBuilder outList = Json.createArrayBuilder();
        JsonArrayBuilder inputList = Json.createArrayBuilder();
        ArrayList<String> tmpInput = new ArrayList<String>();

        //Compare values stored in both arrays
        for(int c = 0; c < hashValue.length; c++){
            if(hashValue[c] == -1){
                continue;
            }
            tmpInput.clear();//Make sure arraylist is clear
            int tmp = hashValue[c];
            for(int j = c + 1; j < hashValue.length; j++){
                if(tmp == hashValue[j]){
                    if(tmpInput.isEmpty()){
                        tmpInput.add(inList.get(c));
                        tmpInput.add(inList.get(j));
                        hashValue[j] = -1;//Set hashValue farther down in the list to -1 so it won't be used for comparison again
                    }
                    else{
                        tmpInput.add(inList.get(j));
                        hashValue[j] = -1;//Set hashValue farther down in the list to -1 so it won't be used for comparison again
                    }
                }
            }
            //outList is only filled if equivalent values were found
            if(!tmpInput.isEmpty()) {
                for (String s : tmpInput) {
                    inputList.add(s);
                }
                outList.add(inputList);
                inputList = Json.createArrayBuilder();//clear inputList of any previous entries
                tmpInput.clear();
            }
        }
        // Set response content type to be JSON
        response.setContentType("application/json");
        // Send back the name of the class as a JSON message
        PrintWriter out = response.getWriter();
        out.println("{ \"outList\" : " + outList.build().toString() + "}");
    }


}

