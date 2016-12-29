Title: Automatic Bug Reporter GSOC 2013
Date: 2013-05-03 12:50
Slug: gsoc-2013
Tags: gsoc, 2013, python, Django, js, css, xhtml, open source, git
Authors: Rihan Pereira
Summary: A gsoc 2013 project proposal migrated from wordpress to pelican

This summer I plan to implement a popular technique of collecting
crash/bug reports via HTTP and automatically parse it into
sections, insert the fields in our bug tracking database, allowing
TimVideo developers to find and fix bugs that only happened in the
field. These are usually the kinds of bugs we can never catch in the
development mode, since the developers couldn’t possibly reproduce
every bizarre PC configuration remote users might have.
This bug detection and reporting has become common technique to take
care of reporting its own crashes.It is important to find out about
every crash, anywhere in the world to deliver a high quality working
program that will be used concurrently.
Sometimes it is not a great idea to rely on users to tell you about
tiny details of bug because its possible that many of them are not
technical enough, and most of them won’t bother to take time off of
their own important work to give you a useful crash report unless you
make it completely automatic.

The project will have two screens:

-   Client Bug Reporting Interface
-   Admin Dashboard(unified view of collected bugs)

![model\_diagram]({attach}../../images/gsoc_model_diagram1.png)

Collecting Data:
----------------

What data should be collected that will help developers find the crash?

Here is the list of data that can be collected from User System:

-   The OS type and version
-   Web Browser type and version
-   filename
-   line number in the code where the crash occurred
-   The error message, as a string
-   unique numeric code for this type of error(Bug ID)
-   Image capturing
-   The user’s description of what they were doing
-   The user’s email address(optional)

It is also possible that the more questions you ask users, the less
likely they are to answer. So I plan to ask bare minimum number of
questions that we think will help us diagnose the problem. What were you
doing? What is your email address? I emphasize that providing an email
address is optional, to alleviate privacy concerns.

Importantly knowing the exact line of code where the code crashed is key
information to fix almost any crash. For rare cases where this isn’t
enough information, developers can contact one of the users who
experienced the crash via email and ask for any additional information
that might help. The benefit of gathering so little information is that
the crash reporting process is very fast, making users less impatient.

Response to the server will be a JSON file which indicates that the
report was received, and includes a message which is displayed to the
user

Their also could be a possible scenario where crash was strong and
severe which caused working code to fail to send report instantly. So
in such case save the specific crash message to a file and then send it
the next time user reloads the web page(on browser restart).
All crash reports arrive at Tim Videos bug tracking database via a
single URL.Our bug tracking database receives bug reports via this
unique URL.In fact that URL is the only public access to our database;
everything else is locked out, so users can submit bugs, but they can’t
get into the database.

In case of Duplicate Crashes:
------------------------------

An important aspect of automatic crash collection is that the same crash
will probably happen many times to many users of the program, and
therefore no new bug should be generated for every duplicate of the
crash.This can be handled by constructing a unique string that
contains key elements of the crash data.The application will determine
duplicate errors by checking whether they have the same error ID.

The error ID is composed as follows:
`File_name:Line_num`

* In cases where new incoming errors are duplicates of old errors, the errors will not be dumbed into
the tracker instead they will be added as a comment to the original error report
* TimVideo bug tracker will automatically append future crashes with the same unique string to current
case, by identifying the Error_ID rather than opening a new case
* This helps the programmer/developer see all the duplicates of the same crash in one place
* The only new information contained in duplicate errors will be the comments, and (possibly) their stacktrace
* The stacktrace will be appended to the end of the user comment(bug description)
* Also the error ID is displayed in the title, there is an “Occurrences” field (which lists the number
of times this error has occurred), and there is an Action drop-down menu (which lets the admin accept
errors,delete it or postpone that decision).

search for bugs:
----------------

If time permits then I plan to built a search feature onto the admin dashboard. I plan to set up the
title in such a way that it can be easily searched for particular problems. Since I use the title format as __filename:lineNumber__ (note the colons), it’s
easy to search for bugs in a particular function just by searching for “filename” or “lineNumber” or
both.

Bug Reporter can have following tabs in which the crash information will
be organized:
![admin\_dashboard]({attach}../../images/gsoc_admin_dashboard.png)

Following control flow diagram demonstrates report handling by
developers:
![bg\_flow]({attach}../../images/gsoc_bg_flow.png)

Utilities for implementation:
-----------------------------

 * Python Web framework -> Django 1.5
 * Web Server -> For deploying Django site I will use Apache2 with its
 * __mod_python__ module because it is well tested and well Documented
 * Deployment option
 * Database -> PostgreSQL(To use PostgreSQL with Django I prefer utility interface library
   psycopg2)

Client User Interface Design:
-----------------------------

 * Django default template Engine
 * Jquery-1.8.3.min.js
 * jquery.ajax() utility for asynchronously loading and submiting crash data.
 * Stylus
    - CSS preprocessor engine(This utility provides easy way to write css and enhanced features like
    function reusability)

Admin Dashboard:
----------------

 * **Dashboard UI**:
     - Django 1.5
         * I will use connection module from Django.db to execute raw SQL commands
         mail module from django.core to send emails to users for feedbacks
     - Jquery-1.8.3.min.js
     - Stylus
         * CSS preprocessor engine
         * more info ->  [http://earnboost.github.io/stylus/‎](http://earnboost.github.io/stylus/)
     - Html5

Deliverables:
-------------

 - users can open a form (without logging in) to report issue
 - Form will have a TextArea to fill in description of the bug, a checkbox if enabled
 will force user to enter email_id, auto image capturing and
 automatically captured crash
 - Form will be simple and jargon free
 - users should be able to report bugs without logging in and without
 registration
 - when someone reports bug, server parses the jsondata to nicely formated
 structure for dashboard view
 - when a developer ends bugfix cycle he/she should be able to “close it”
 - On the admin dashboard there will be automatically updated list of bugs
 reported with status so that other users can see what was just fixed
 - It should allow voting on bugs by users, but it’s not a requirement.(optional feature)
 each specific bug report(optional feature)

Benefits for TimVideos Organization:
-----------------------------------

I admit to make an attempt to deliver a working automated bug reporter
which will help TimVideos improve there project quality, reduce
development time and also provide useful crash reports for better
inspection and debugging.

Proposal Timeline:
-----------------

I will be having my exams starting from 11th May to 7th June. To be specific I will have exams on
following days:

- 11th May(Saturday)
- 18th May (Saturday)
- 23th May (Thursday)
- 29th May(Wednesday)
- 3rd June(Monday)
- 7th June( Friday)

*PS - During exam days I will not be active for project discussions and code
building since I will be busy studying. But sooner after examination I
will start with my regular schedule with 40 hours a week work*

I plan to complete my GSoC project by following the schedule given
below.

Before June 16:
---------------

- Familiarize myself with TimVideos streaming System.
- Become familiar with Sphinx auto documenting tool
- Setup development environment considering project dependencies
- Initialize git repository
- Design User stories which will be delivered in milestone 1.0

June 17: Official coding period begins:
---------------------------------------
In this phase I plan to deliver a working application with its basline functionality created successfully.
Milestone 1.0 will be my first major release.

 * __June 17 - June 22__ : Design schema and entity relationship diagram and implement database scripts to make database ready
 * __June 25 - June 29__ : Implement UI for Admin Dashboard and write test code
 * __July 1 - July 6__ : Implement user report form
 * __July 8 - July 13__ : Implement program to collect crashreport(packagename, filename, linenumber) and other details
 * __July 15 - July 20__ : implement code to transfer and parse bug data to be insert into database and write test code
 * __July 22 -July 27__ : check for bugs and missing functionality.write documentation.

If some User stories with iterations cannot be completed,then they are
postponed to next milestone.

August 2: Midterm Evaluation (Milestone 1.0):
--------------------------------------------
Code planned for Milestone 1.0 is submitted.

* __August 3 - August 10__ : Complete leftover user stories from Milestone 1.0.Refine baseline functionality
by writing robust code.
* __August 12 - August 17__ : Implement code for sending email to users for getting feedback/asking additional
info about the bug and write test code
* __August 19 - August 24__ : Write code to avoid generating duplicate bug reports, write test code
* __August 26 - August 31__ : Implement action drop-down button to accept, delete particular bug, write test code
* __September 2 - September 7__ : Implement 'close bug' feature to stop bug life cycle, write test code
* __September 9 -September 14__ : Experiment, write code for capture image(crashed web page) which can be
compressed and send to the server, write test code
* __September 16('pencils down' date)__ - September 21 : update documentation, check with various test cases, remove unused code

September 23: Final evaluations (Milestone 2.0):
-----------------------------------------------

* At this point, I make sure that my proposed project functions as Expected
* This is the point where a set of functionality meets needs of the users
* Finally commit untracked code to git repository and push to Github
* Submit code sample to Google

Personal Information:
--------------------

I am 3rd year undergraduate student from India majoring in Information
Technology pursuing Bachelor degree. I prefer to communicate mostly using
IRC and email. I would also like to update my work progress on twitter
post.

* email : rihen234@gmail.com
* IRC network : freenode.net
* IRC Nickname: rihbyne

what I will be doing next in the upcoming week.

- User stories that I completed.
- User stories in progress.

Open Source Experience:
----------------------

I was inspired and motivated by the speech of Richard Stallman, who is the founder of Emacs Text Editor to join Free
and open source software development ecosystem which motivated me to write code for FOSS. I believe that getting yourself involved into a open source software community helps you to gauge where you stand as an maker when it comes to solving real world problems. I have been exploring open source utilities and I have never turned back. Initially, in the beginning I was not aware of VC concepts in general but figured that out through web sources. Over time things got interesting day by day.

Following developer tools that I just started using few months ago:

1. Vim 
2. Emacs

I have Python web development with Django experience of approx. 7 months, javascript/html/css of approx.
12 months. I have come across various version control types like DVCS and CVS. Git is an example of DVCS which is highly favoured by folks around FOSS projects.

My Github repository link: [https://github.com/rihbyne](https://github.com/rihbyne)

Project contributions:
---------------------

A web-based 2-tier application started for our local family doctor, written in PHP, MySQL, javascript, html.
The project is still in initial phase of development. We are 4 to 5 contributors for the project.
The project makes use of CodeIgnitor PHP MVC framework for easy development and time constraints.
Currently the project is not active. This project was started as a hobby and means of practice.
Link to the project: [http://code.google.com/p/patient-info-system/](http://code.google.com/p/patient-info-system/)
