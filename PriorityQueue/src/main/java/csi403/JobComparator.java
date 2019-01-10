package csi403;
/**
* PRIORITY QUEUE
* 
* 
* Used to compare priorities between objects
* 
* @author Bryan Guzman
* @version 1.0
* ID 001265918
* CSI403-Project02
**/
import java.util.Comparator;

class JobComparator implements Comparator<Job> {
    public int compare(Job job1, Job job2)
    {
        return (job1.getPriority() - job2.getPriority());
    }
}
