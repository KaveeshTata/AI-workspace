The most important thing to look for while hosting a website. Ex: Godaddy

Shared webhost and VPS - Virtual private server uses hypervisor for sharing the large number of split up operating systems to look like a shared hosts rather the Shared webhost you get the actual space you pay for in full rather than getting a copy of it. VPS is costly.

AWS EC2 you pay for what you use based on the number of VPSes you use which can be economic

Vertical scaling: Only one server is present and we scale the rest of the components. CPU scaling, memory scaling or RAM scaling which can be very costly. Physical constraints are high as you can go as high as technology or financial condition

4 core means 4 activities at once which means 4 different brains for activity.

Bigger servers chopped down to VPSes like amazon

SSDs faster than mechanical drive. 768 GB maximum SSD for a laptop.

 Clients will have the IP address of the load balancer which will be the only public IP address and all the server IP address will be private so that the LB can decide which server it will direct to. 

Load balancer is basically like a DNS server. BIND server basically does a round robin method to return a server IP address. A simple one

Caching can be done for reducing the load on the servers so that load balancer can assign different servers for a high load activity as everything is cached 

If a user is sent to server 2 as your session is expired instead of server 1 where you did the work, it will ask you to login again. THis is the problem while load balancing based on the round robin 

Redundant array of independent disks. RAID 0 is for performance. RAID 1 is for redundancy because it writes in two different disks. RAID 10 is mixture of 4 RAID 0 and RAID 1. RAID 5 is where 1 of the 5 disks is used for redundancy and teh rest 4 are usable space. RAID 6 is where 2 of the 6 disks are used for redundancy.

Software load balancers: Amazon ELB, HAProxy, LVS (Linux virtual server) etc
Hardware Load balancers: Barracuda, Cisco, Citrix

Sticky Sessions where multiple times visit will store the information about the user for that particular website or a system. The user will end up in the same backend server without the load balancing assigning a different server. 

Caching:  mysql query cache is for the query caching. Memcache is a mechanism to store whatever you want. memcache is a server. 

Replication: High redundancy because of master - slave approach. Easy replacement where we can plug in a slave if master is down. We can have a master - master relationship which again connect to their own slaves for more redundancy. 

![[Screenshot 2026-06-11 at 7.38.16 PM.png]]

Partitioning: Splitting the queries based on a condition to the slaves so that load is decreased and we have scale them horizontally. 

**Massive scaling of the web application:**

The first golden rule of scalability is every server present should contain same codebase and does not store any user-related data, like sessions or profile pictures, on local disc or memory. The user related data must be stored in sessions which in turn are stored in a central database which is accessible to all the servers alike which includes caches like redis etc

The database must always be external and near to the data centre rather than inside the application servers

Capistrano is a automation software where it deploys the new version of the application without disturbing the old version. 

Capistrano organizes your remote servers into a strictly defined, timestamped directory hierarchy. When a new version of your application is deployed, it is placed in a new directory, ensuring the old version is still live. Once the deployment is complete, a symlink (`current`) is flipped to point to the latest release, achieving seamless updates.

Cloning is basically a snapshot or instance of your latest codebase (Amazon machine image for example). We can use this image/super clone for instantly deploying  the latest codebase. This will help in horizontal scaling.

Next would be the database where you cant keep going with the horizontal scaling and add more RAM. Even replication does not help in future because of sharding and many problems which will make your application slower and slower or we can denormalise the queries and remove joins from the queries and join them in the application code. 

Now after database scaling, the number of requests handled by the server is still too much which can be solved my in-memory caches like redis or memcache. So your application goes through the cache first to retrieve info and only if its not present in the cache should it go to the main server because caches are incredibly fast and can retrieve any info in the RAM.

So simple method is to cache the database queries and its hashed version as the key so that its easier to retrieve. Then the application checks the cache first and then the database. But the main problem is the expiry of these caches where deleting the complex query would be difficult and when one gets deleted all the other cells related to that cell will get deleted

The other approach is to cache the entire class instance for example classes, methods, data, data types. So that when something needs to be changed we an discard the entire object 

Next would be to work on the millions of requests asynchronously. we can render a HTML page for every on hour on the website and then show these html files to the user which become responsive and fast to the users. but sometimes we cant do this so we have workers in the background who take the job and send the response back to the user.

Latency is normally a certain amount of time to perform an activity or to produce a result.
Throughput is number of such activities that can be done under a given amount of time.
So we normally aim for maximum throughput with minimal or acceptable latency











