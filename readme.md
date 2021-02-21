# wg-dynamic-mesh
a program to dynamically (re)configure a wireguard interface based on factors

can be run in server or client mode
### server-mode:
* monitor connections to peers and other servers
* send current "routes" to clients
* (re)configure according to other servers
* ...
### client-mode
* receive "routes" from server
* reconfigure own interface accordingly
* ...
## TODO:
* everything
## scenario:
* 2 or more "Servers":
    * static ip addresses
    * comparetivly high bandwidth
    * must have connectivity with each other (or through other servers)
* 0 or more "clients":
    * may often change location/ip address
    * may not have (direct) access to one or more of the servers
    * ...

#### example
2 servers: Server[A,B]:

4 clients: client{1,4}
* client1 and 2 connected to both servers
* client3 only connected to serverA, can't reach serverB (for whatever reason)
* client4 only connected to serverB, can't reach serverA (for whatever reason)

client 3 wants to connect to client4, so the packets have to be routed trough both servers, but with "default wireguard" peer routes are not automatically be rewritten

A configuration program as this will be (hopefully) become, should help here
