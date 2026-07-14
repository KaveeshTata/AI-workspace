Load balancers are hardwares or softwares which distribute client request to applications servers/ databases. They help in managing the traffic by distributing them to different servers based on certain rules and parameters. They can help in maintaining the server integrity and prevent overloading of them.

They can also provide SSL termination which means it can encrypt or decrypt which reduces load on the backend servers. They are very expensive too. Apart from that they also help in session maintenance which can persist a user to the same instance every time he sends a request. Which is helpful in cache maintenance too

So as to not make this a single point of failure the load balancers are normally connected in active-active or active passive formation which is already covered in scalability

The metrics that load balancers route traffic is:
Least used, Random, Session based, Round robin or weighted round robin, Layer 4, Layer 7

Round robin: Generally cycles through the servers to distribute the traffic, Although it is not efficient its easy to implement and maintain.

Weighted RR: The servers are assigned a weight based on its performance against other servers which can be decided for a fair distribution of traffic

Layer 4: This uses the information in the transport layer of the network for load balancing. These are mostly source, destination IP addresses rather than the content itself. This was the normal load balancing where the client side gets the IP address of the LB and then the LB takes over. When the packet or request reaches LB, it performs Network Address translation where the destination IP of the packet is changed from its own IP to the IP it has deduced internally for the processing. Similarly when it returns a response too.

Layer 7: This uses the information in the application layer of the network for load balancing. These include the header, content and message of the packet such as URL, type of data or cookies in the packet etc Which means they can understand the data as a whole before distributing the requests among the servers. NGINX is one of the popular software reverse proxies