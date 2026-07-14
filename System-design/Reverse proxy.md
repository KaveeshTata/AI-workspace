Opposite to the forward proxy. Normally in a proxy, the client is masked because of safety purposes. So the server sees the proxy address instead of client IP address. Now reverse proxy is the same except that this server IP address is masked and the proxy address is returned back to the client. As the direction is revered, hence the name reverse proxy. ex: NGINX

This helps the servers to be scaled as client does not have direct information. It also keeps the servers safe and secure. It also performs SSL termination and sends teh decrypted message to the server and encrypted message back to the client. It can cache and compress the responses.

Every Layer 7 load balancer is effectively a reverse proxy, but not every reverse proxy is a load balancer.