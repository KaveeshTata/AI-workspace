ACID properties must be followed by the relational database transactions
Atomicity: Each transaction is all or nothing
Consistency: Every transaction must be in a single state and the update must be spread cross all the relational databases
Isolation: Each transaction must be carried out as if it is alone
Durability: Once a transaction is committed it remain so

Scaling a RDB is through master-master replication, master-slave replication, federation, sharding, denormalisation, SQL tuning

M-S replication: Where the master serves to read/write and it passes the read to one or more slaves which can only read. Slaves can also replicate more slaves in a tree fashion. When the master is down or failed, the DB can serve for only read until one of the slaves is promoted to master. But this requires additional logic so this comes as a tradeoff

M-M replication: Same as before but there are two masters who communicate with each other. They have their own slaves. If one master goes down, the other takes over. Normally this takes more time and we should introduce a load-balancer additionally, which takes more resources. They are loosely consistent or latency is very high for following consistency.

Normally there is some data lose when the master goes down and it takes time to the next master to come up. Also sometimes if more read slaves are present, then more the write replication is run, which creates a time lag. Also sometimes there are parallel threads for write to master which bogs down read quality of master and slaves.

Federation: Breaking down of a single monolithic database into smaller parts based on functionality. These smaller databases normally result in smaller reads and more cache hits which reduces load on the database. With no single point of write like in replication, you can write in parallel. But it is not effective when you need huge tables and functions to access it. Need to change the application logic for this which in itself is a overhead. Also adding data from two different DB servers require server link which is not safe sometimes.

Sharding: Similar to federation but this is done with horizontal partitioning rather than functionality. It also reduces read speed and increases cache hits. It is also similar to federation as it does not require replication which means down time and latency is very less. Data is kept very less so that storing, managing and caching it is very easy. Data is also denormalized for better reads rather than writes. But it does require additional code changes. It is also very hard to join multiple shards together when we need them. 

Denormalisation: After distributing data with sharding and federation, the data is denormalised for better reads than writes. So adding duplicate rows for reducing read times as normally reads outnumber writes in a system. The need to join multiple tables will be low which makes it faster. But this has its tradeoffs, the writes will be slow as now one change must be applied to all the duplicate entries in other tables. Data duplication is also done which is a constraint

SQL tuning: Basically some of the principles we can use to make the query run much faster and smoother. By maybe using correct datatypes and constraints. Denormalise where required, use proper distribution techniques. Test for benchmarks regularly. 

Next comes NoSQL, which is a combination of entries in key-value store, document store, wide-column store or graph DB. It does not have a specific structure or data types. Data is generally denormalised. And it follows the rule of eventual consistency. So instead of following ACID properties. NoSQL follows BASE properties. It follows availability over consistency.
So its :
Basically available: Which means it is highly available
Soft state: The state of the system might change over time even without any input
Eventual consistency: Which means it will slowly move towards consistency given that the system doesnt get any input during this time

So first type is the key-value store which stores the data in key-value pairs. The keys are stored lexicographically and are generally stored in SSD. Time complexity for read and write is o(1). Very easy to implement and generally used for very minimum operations. So complexity is shifted to the application layer, which makes it difficult to customize.