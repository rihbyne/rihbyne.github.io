Title: Notification Core daemon
Date: 2016-08-11 16:24
Slug: notification-core
Summary: Designed & crafted a rolling Notifications backbone that shards data periodically in the background handling crash and resume operations. This made my lookup queries & data retrieval in batches faster.

Purpose:
--------
The need to persist data subsets across multiple collections arose when I stressed about achieving optimal data retrieval from MongoDB considering the volume of data sent and stored on average will be severely high.
This functionality was reused across many backend services. I am glad to have built it.
The below figure illustrates the mechanism taking place at app runtime.

![block\_diagram]({attach}../images/diy/notification_core_at_a_glance.png)


Workings:
---------
- The sacks or collections filled with data get archived periodically. This is done by setting 
*NOTIFY_ARCHIVE_INTERVAL_IN_DAYS* in .env settings file. The constant takes in an Integer which is used by the program to watch for the timeout in milliseconds, within that period notifications can come in and get saved to the collection. For each new time interval, new collection gets created, registered and assigned to mongoose instance programmatically at runtime.This is useful as it saves the mundane task of manually creating collections, every time when it is required to create fresh collection.

- The program is also designed to be capable of recovering from server crash. If such situation occurs then the program, since its resume time, performs the math to calculate the leftover time required to reach the final timeout.So within that period, request payload may or may not come in and get saved.Its probable.If suppose say for a particular collection, crash occurs, time flies by, and program misses to update mongoose instance with new collection then the very next time the app starts again it checks for such a scenario.If such a scenario occurs then it archives the unarchived collection and assigns new collection to the mongoose instance for that running interval.

- Next, is the *RESET_ARCHIVE_INTERVAL_ON_CRASH* variable. This takes a boolean value.if set to true then the program doesn’t care about continuing on same interval: It starts new interval every time it crashes. If set to false then it considers the case where it has to continue on the same interval until it reaches its final timeout in milliseconds and start a new interval thereafter.
