It states that in a complex distributed system, only the two of the following three can be achieved simultaneously for a read/write pair which is the most basic SQL operations. 
Consistency: A read is guaranteed to return the most recent write or an error if it doesn't exist
Availability: A read/write operation will return a response within a reasonable amount of time. It does not give back any errors or timeouts
Partial tolerance: The system will continue to run even when there are partition inside the server or the system.

We need partition tolerance at all times because reliability is never a given. So we can choose between consistency and availability with each having their own tradeoffs and advantages.
CP: It always returns a response from the partitioned node or a timeout error. You choose when your business requirement is atomic read/writes. 
AP: Returns the most recent write data from the partitioned node which can be old and stale. But it returns a response and also can write in the partitioned node which resolves itself when the partition resolves itself. You choose this over consistency when you have a flexibility on when the data is supposed to be synchronised. It is also widely used hwen you definitely need a response even when there are errors.

Consistency patterns will be categorised as weak, strong and eventual consistency. So now weak consistency means high availability so this is best used in real time systems such as memcache or video chat where you wont hear the other persons voice when the reception is down. So rather than giving some response it totally cuts it down but does not cut the call altogether.

Eventual consistency is where a read will see the write eventually when the system is scheduled or ready for it. It is mostly used in DNS or email servers.

Strong consistency is where write is synchronously updated across ythe systems with no time delay. Its normally used in file systems or RDMSs and where transactions is required in a system.

In availability there are two types: Fail-over and replicate. And failover has active-passive where the passive is listening the heartbeat of active by sending a signal between them at all times. When the active does not send back, the passive takes over for the active under the previous actives IP address. Now there is also active-active failover where both are managing the load and traffic and any server can take over at any point of time. 

Replication is basically master-slave replication and master-master replication. All these have a downside of downtime under the other one takes over which is basically inevitable if you need highly available system.

Availability can be calculated of two systems based on their orientation. If there are two systems with 99.9%, their availability is only 99.8%. But if they are in parallel then their availability is 99.9999%.

