package csi403;
/**
 * FRIEND OF A FRIEND
 *
 *
 * Receive a post of a a JSON Array containing a series of string arrays containing "friends".
 * Return a JSON Array containing lists of friends that share friends at most one friend away.
 *
 * Contained in this class will be a small class to represent the friends array
 * JSON service that will receive and return a JSON Array
 * Methods to determine friends of a friend
 *
 * NOTE: FOAF stands for "Friend Of A Friend"
 *
 * @author Bryan Guzman
 * @version 1.0
 * ID 001265918
 * CSI403-Project05
 */

// Import required Java libraries
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.json.*;
import java.lang.reflect.Array;
import java.util.*;

/**
 * Used to store the posted JSON Array of Friends
 */
class Friends{
    public String friend;
    public String person;

    public Friends(String person, String friend){
        this.person = person;
        this.friend = friend;
    }

    @Override
    public boolean equals(Object obj){
        if(this == obj){
            return true;
        }
        else if(obj == null){
            return false;
        }
        else if(obj instanceof Friends){
            Friends friends = (Friends)obj;
            if((this.person.compareTo(friends.friend) == 0) && (this.friend.compareTo(friends.person) == 0)){
                return true;
            }
            else if((this.person.compareTo(friends.person) == 0) && (this.friend.compareTo(friends.friend) == 0)){
                return true;
            }
        }
        return false;
    }

    //@Override
    //public String toString(){
      //  return (this.person + " " +this.friend);
    //}
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
        while ((test = br.readLine()) != null) {
            //Make sure null is not added on to jsonStr
            if (test != null) {
                jsonStr += test;
            }
        }
        try {
            //Create a JsonArray from jsonStr
            StringReader strReader = new StringReader(jsonStr);
            JsonReader reader = Json.createReader(strReader);
            JsonObject obj = reader.readObject();
            inArray = obj.getJsonArray("inList");
        } catch (Exception e) {
            out.print("{\"Error\" : \"Malformed JSON\"}");
            return;
        }

        //Make an array of friends
        LinkedList<JsonObject> list = new LinkedList<JsonObject>();
        //int len = inArray.size();
        ArrayList<Friends> friends = new ArrayList();

        if (inArray == null) {
            out.print("{\"Error\" : \"Empty JSON message sent\"}");
            return;
        } else {
            try {
                for (int i = 0; i < inArray.size(); i++) {
                    list.add(inArray.getJsonObject(i));
                }
            } catch (Exception e) {
                out.print("\"Friend\" : \"Failed to add Json Object to list\"");
                return;
            }

            try {
                //Takes list and converts them to friend object
                for (int j = 0; j < list.size(); j++) {
                    JsonArray jFriend = list.get(j).getJsonArray("friends"); //Store the Json array labeled friend located within inList
                    friends.add(new Friends(jFriend.getString(0), jFriend.getString(1))); //only two indexes for friend array, the person and friend
                }
            } catch (Exception e) {
                out.print("\"Error\" : \"Failed to add Friends Json Array to friends array\"");
                return;
            }
        }
        try {
            //Print what pointsWithin returns in JSON format
            out.println("{ \"outList\" : " + foaf(friends).build().toString() + "}");
        }
        catch (Exception e){
            out.print("{\"Error\" : \"Something went wrong when trying to find a FOAF\"}");
            //out.print("{\"ListSize\" : " + list.size() + "}");
            return;
        }

    }


    // Standard Servlet method
    public void destroy() {
        // Do any required tear-down here, likely nothing.
    }


    //foaf will return a json array that will be the final JsonArray
    public static JsonArrayBuilder foaf(ArrayList<Friends> friends) {
        JsonArrayBuilder inputList = Json.createArrayBuilder();
        JsonArrayBuilder outList = Json.createArrayBuilder();
        ArrayList<Friends> tmpFriends = new ArrayList();//Used to store foaf
        String friend = "", person = "";

        for (int i = 0; i < friends.size(); i++) {
            friend = friends.get(i).friend;
            //Run through the friends array skipping one index
            for (int j = i + 1; j < friends.size(); j++) {
                person = friends.get(j).person;
                //Check friends array for equivalent friends and store in tmp array
                if ((friend.toLowerCase()).equals(person.toLowerCase())) {
                        tmpFriends.add(new Friends(friends.get(i).person, friends.get(j).friend));
                }
            }
        }//tmpFriends should hold all of foaf relationships

        //Checks for duplicates
        for(int c = 0; c < tmpFriends.size(); c++){
            for(int v = c + 1; v < tmpFriends.size(); v++){
                if((tmpFriends.get(c).person.compareToIgnoreCase(tmpFriends.get(v).friend)) == 0 && (tmpFriends.get(c).friend.compareToIgnoreCase(tmpFriends.get(v).person)) == 0){
                    tmpFriends.remove(v);
                }
            }
        }

        if(tmpFriends.size() < 1){
            return outList;
        }
        else {
            for (Friends f : tmpFriends) {
                if(f == null){
                    return outList;
                }
                else{
                    inputList.add(f.person);
                    inputList.add(f.friend);

                    outList.add(inputList);
                    inputList = Json.createArrayBuilder();
                }
            }
            return outList;
        }
    }
}