Title: Multi-Tenant architecture for umbrella application
Date: 2016-11-05 11:07
Slug: multi-tenancy
Summary: Used software multi-tenancy to address the problem of data segregation and ACLs to control the scope of resources on users.

![block\_diagram]({attach}../images/diy/itd_org_architecture.png)



*Software multitenancy*  enabled me to achieve a granular control over each tenant’s resources like data for example. At the MongoDB level - every new tenant shares a common application server but has dedicated database and dedicated connection instance. 

PS:  In application context, tenant = merchant

Next immediate question is - how is the design useful and is it feasible?
-------------------------------------------------------------------------
Having db/merchant will have many advantages.

 - __Separation of concerns__ - The most sort after requirement in this type of software designs.It allows us to give specific privileges to each merchant and its users.Each merchant’s data doesn’t get mix up with others. Security wise like Nonce and Digital Signature can be controlled as per the specification.
 - __Self-Contained Mongoose instance__ - by default mongoose provisions 5 pool connections to each database for parallel simultaneous I/O so maintaining dedicated mongoose instances inside the node app will avoid long running callbacks.
 - __Flexibility in defining API endpoints__ - dedicated mongoose connection to the database will be configured at the base route level for each merchant.
 - __Scalability__ - Based on application monitoring and analytics if we find out that one merchant’s traffic is significantly higher than other then we can shard the mongodb itself at its database level and run individual mongod daemon for each sharded server. In contrast, we will not get this performance benefit if we persist merchant’s data collection-wise in single giant database and shard collections inside them. It will be cumbersome.
