Title: Application logging 
Date: 2016-09-13 23:18
Slug: appln-logging
Summary: Logging in server-side applications the right way

Loggging is considered as one of the many must have factor in 12-factor Apps. Fundamentally applications should be capable of logging to stdout by default. As an extra step, logs can be
pipped to a file as a stream. When logs are streamed to a file during application runtime it does not have 
start and end of file like a normal file instead its a flow of data similar to flow of water. A stream log 
is an established practice in large software firms. Sophisticated logging tools like Syslog allows anyone
to centralize logging data from distributed services. 

![model\_diagram]({attach}../images/diy/logging.png)

This diagram shows how I setup logging at work. These logs are crucial for us as many of our services are money related. Additionally, these are processed by Analytics & Monitoring tools to gain insights & predict positive
outcomes.

Logrotate is of the essential utility I considered in my logging configuration. Its directives do many useful tasks
and it avoids having to write external scripts.

Directives of logrotate :
--------------------------
* __notifempty__ - This directive monitors the log file to check if the file is empty. If its empty then it does not run its next directives and simply ignores the file.
* __Compress__ - This directive run a gzip compression on the log file once and only if it reaches its limits like for instance, the log is generated for a day or it has reached its size 2GB.
* __Daily__ - This directive if turned on, is responsible for everyday logging. It appends integers [0-9] for recognition and for avoiding overwrites.
* __Rotate__ - This directive takes in an Integer with which it continues dumping of log data into new file til it reaches its Integer target and after that it starts over again, but this time, empties the file.
* __Copytruncate__ - The copytruncate directive, empties the file in order to begin write the log data stream into the same file instead of creating a new file.
* __Date-ext__ - This directive’s only and only job is to rename the file by adding a date on which it was compressed.
