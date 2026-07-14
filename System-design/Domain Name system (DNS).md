The DNS is created for a distributed and a hierarchical database containing various types of data and host names and their mappings. The names are normally divided into hierarchal names which are separated by a dot. This is done to break down the domains based on their namespaces and make the search easier.

The name space is basically a tree where every level of the tree represents either a branch or a leaf of the tree. Branch is used to identify a set of shared namespaces. The leaf represents a single name which is used and then point to the next one.

There are 5 categories based on their level of hierarchy: 
Root domain: The top of the domain tree and the highest branch of the DNS tree. It is normally started with a dot(.) and sometimes a blank space.
Top - level domain: It is a name used to indicate the country/organisation of the domain. Like .com
Second-level domain: It is the variable length name given to a individual or organisation used in the internet. These are mostly based on an appropriate top-level domain, depending on the organisation and the geography of where the server is used. like microsoft.com
Subdomain: It is the additional names given to a related second-level domain for a department, purpose or geography. Like example.google.com
Host: This is the leaf of the DNS tree which represents the host or a resource of the domain. Like hosta.exmpale.com

Resource records in a DNS identifies a particular resource within the database. There are various RRs within DNS. Some of which include. State of authority, Host, name server, Mail exchanger, Canonical name

A DNS database can be distributed into zones. A zone is a portion of the database with owner name of the contiguous portion of the DNS namespace. Each DNS server can be configured to multiple zones

Each zone consists information of all the namespaces which end with that zone namespace. The first record of each RR is always the state of authority and it identifies the primary DNS server for the zone as the best way to get information within that zone. 

A name within a zone can also be delegated to a different zone that is hosted on different DNS altogether. This os delegation, it is nothing but assigning responsibility of a potion of DNS namespace to another DNS server hosted in a different entity. This is represented by Name server (NS) resource record which has the zone name and the DNS server which is responsible for that zone.

This helps in delegating a server namespace with multiple organisations who responsible for their own DNS server. It also reduces load on a single server

There can be multiple zones representing the same portion of the namespace:
Primary: It is a zone where all the updates for the records which are happening in that zone are kept.
Secondary: It is a read-only copy of the primary zone.
Stub: It is a read only copy of the primary that contains only the RRs that identify the DNS servers which are authoritative for the DNS domain name.

So a DNS server hosting the primary file for that zone is said to be the primary server and the server which is hosting a secondary file for that zone is said to be the secondary server for that zone.

The process of replicating the zone files from one server to another server is called Zone transfer. It can be done with primary or secondary servers.

A master DNS server is the source of the zone information during the transfers. If it comes from the primary server, it comes from the DNS server hosting the primary file. Or else if it is secondary server then the read only copy is replicated.

There are 2 types of zone file transfers: 
Full zone transfer where everything is replicated 
Incremental zone transfer where only the changes or modifications are replicated.

A DNS query is normally between DNS client and a DNS server or between two DNS servers. A DNS query is merely a request for the DNS server RRs of a specified RR type of a specific DNS name.

There are two types of DNS queries:
Recursive: A recursive query forces a DNS server to respond to a request with either a failure or a success response. A DNS client normally makes a recursive query. So the DNS server must contact any DNS server which can get the job done and if it is successful then send the response back to the DNS client. It is also used in querying between resolver and DNS server and between DNS server forwarder and itself. When a DNS server does not contain the information it escalates it to the root server. Each level of DNS servers contain caches with the information of the root server.

Iterative: An iterative query is one in which the DNS server is expected to respond with the best local information it has, based on what the DNS server knows from local zone files or from caching. If a DNS server does not have any local information that can answer the query, it simply sends a negative response

The Time-to-Live (TTL) value in a resource record indicates a length of time used by other DNS servers to determine how long to cache information for a record before expiring and discarding it.

