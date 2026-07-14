Application layer mostly consists of stateful components where we have to take care of the information, user queues, caches, databases etc. 

Usually both horizontal scaling and redundancy are achieved by load balancing. Normally a large system, balances the load at 3 places which may be at user to web server, web server to internal platform server or from internal server to database. But at least one of them must be balanced

After load balancing and caching, offline processing becomes very important. The most easiest way is to create message queues for it. If processing is taking too long, we can create a message queue to pool all the requests from the user and process them in the background. So normally:

We just schedule a task and perform no work in the consumer. Inform the user that then processing is done offline with an added polling mechanism where the user gets to know when the process is done. Like assigning something to the user

Perform some work in-line and inside the consumer to make the user think the process is done but actually perform the process in the offline. Like facebook/twitter messaging.

The other method is scheduling periodic jobs using cron for example. The cron is incharge of scheduling and pooling the message queue rather than processing.

At last separating platform layer and web server is very efficient because we can scale the platform layers for APIs rather than the whole web server which is actually very costly. They can also be reused for multiple types of products and interfaces.

Coordination between two nodes in a distributed system is very hard. it is usually done by locking, synchronisation, publisher/subscriber etc. This is where zookeeper comes in which helps in communicating between the nodes. Zookeeper allows distributed processes to communicate and coordinate with the help of a shared hierarchical name space of data registers. It exposes naming, configurations, locks and synchronisations etc

Each node in the zookeeper came space is called a Znode. Where they are categorised by:
Permanent nodes which will exist until they are explicitly deleted
Ephemeral nodes which exist as long as the session is active. They cant have any children
sequence nodes which append a monotonically increasing counter to the end of the path
