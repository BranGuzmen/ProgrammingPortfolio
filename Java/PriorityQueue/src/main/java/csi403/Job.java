package csi403;
/**
* PRIORITY QUEUE
* 
*
* Object that will store the command and priority. 
* 
* @author Bryan Guzman
* @version 1.0 
* ID 001265918
* CSI403-Project02
**/
class Job {
    private String jobName;
    private int priority;

    // Constructor
    Job(String job, int pri){
        this.jobName = job;
        this.priority = pri;
    }

    // Getters
    String getJobName() {
        return jobName;
    }
    int getPriority() {
        return priority;
    }
}
