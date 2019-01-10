package csi403;
/**
 * HASH ALGORITHM
 *
 *
 * Hash algorithm used on input string
 *
 * @author Bryan Guzman
 * @version 1.0
 * ID 001265918
 * CSI403-Project03
 */

import java.nio.charset.StandardCharsets;
import java.util.List;

public class HashAlg {

    public HashAlg(){}

    //Will run the hash algorithm on the elements of inList and return a new int list
    public static int[] hashAlg(List<String> list){
        int size = list.size();
        int[] hash = new int[size];
        int hashValue = 0, c = 0;

        //Store the ASCII values in a byte array, add them up and store in int array
        for(String input : list){
            //Extract the ascii value of each character and adds them together
            byte[] ascii = input.toLowerCase().getBytes(StandardCharsets.US_ASCII);//ASCII value of 1 string stored in ascii

            //Add up the ASCII values stored in ascii
            for(int i = 0; i < ascii.length; i++){
                hashValue += ascii[i];
            }
            //hashValue is stored at the same index as the string stored in list
            hash[c] = hashValue;
            c++;
            hashValue = 0;

        }
        return hash;
    }
}
