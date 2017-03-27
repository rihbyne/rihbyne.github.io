Title: Stateless pagination API
Date: 2016-08-27 21:50
Slug: stateless-pagination
Summary: Designed & implemented a stateless cursor based pagination for batch retrieving of notifications data on top of the Notifications Core Daemon.

What is the need to Paginate?
-----------------------------
While it’s entirely possible to get all of the data at once using a single database query but the data will be so large or overtime it grow so large that it’s cumbersome for the end user to view all of the data at once. Especially, if the user wishes to view only the recent data, then, in such case, it’s necessary to break a large data set into smaller, readable chunks and respond to the caller. Pagination is used in such cases where the volume of consumable data is heavy on end user side. With Pagination technique, user consumes the data in batches and only on user’s request the next page is served.

This illustration explains how I pair the notifications core daemon module with paginator.

![block\_diagram]({attach}../images/diy/stateless_pagination.png)

In context of its app's nature, the API is stateless; the server-side does not keep track  about which page the user is currently at and which page should be made available next.Instead, the API designates a cursor to end consumer upon very first request and thereafter, every time, if the user wishes to view more, he/she has to send the parameters that he/she previously received. The server-side program uses those parameters sent by the user to figure out the next page for that user. The parameter value keeps on changing on each subsequent request to the server. This is how stateless pagination works as it avoids the clutter of keeping track of each user’s request.

The stateless Pagination API takes in four parameters to every user request:

 * __bkwd_cursor__ - Used as a pair to fetch recent data
 * __bkwd_cursor_offset_from__ - Used as a pair with above variable

 * __fwd_cursor__ - Used as a pair to fetch past data
 * __fwd_cursor_offset_from__ Used as a pair with above variable
