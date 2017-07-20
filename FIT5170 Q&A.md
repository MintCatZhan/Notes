# Week 1

1. What do you understand Distributed systems (DS) are and how do you define them?

   - Definition: A DISTRIBUTED SYSTEM (DS) consists of **a collection of autonomous computers**, connected through **a network** and distribution **middleware**, which **enables computers to coordinate their activities and to share the resources of the system**, so that users perceive the system **as a single, integrated computing facility.**
   - Distributed systems are groups of networked computers, which have the same goal for their work. <u>The terms "concurrent computing", "parallel computing", and "distributed computing" have a lot of overlap, and no clear distinction exists between them.</u> The same system may be characterized both as "parallel" and "distributed"; the processors in a typical distributed system run concurrently in parallel. Parallel computing may be seen as a particular tightly coupled form of distributed computing, and distributed computing may be seen as a loosely coupled form of parallel computing. Nevertheless, it is possible to roughly classify concurrent systems as "parallel" or "distributed". In parallel computing, all processors may have access to a shared memory to exchange information between processors. In distributed computing, each processor has its own private memory (distributed memory). Information is exchanged by passing messages between the processors.

2. Explain the characteristics of a DS?

   - Distributed computing is a field of computer science that studies distributed systems. 
     - A distributed system consists of <u>multiple computers</u> that <u>communicate through a computer network</u>. The computers <u>interact with each other in order to achieve a common goal</u> like solving large computational problem. 
     - A computer program that <u>runs in a distributed system</u> is called a distributed program, and distributed programming is the process of writing such programs. Certain common characteristics can be used to assess distributed systems
   - **Resource Sharing**: Ability to use any hardware, software or data anywhere in the system.
   - **Performance**:Latency and throughput are the two most fundamental measures of network performance. 
     - <u>*Latency*</u> measures the **amount of time between the start of an action and its completion**; throughput is the total number of such actions that occur in a given amount of time.
     - <u>*Throughput*</u> is **the amount of work that can be performed or the amount of output that be produced by a system or component in a given period of time**. It has a meaning similar to that of capacity, and the two are often used as synonyms. Allow the system to be reconfigured to improve performance as loads vary.
   - **Openness** is concerned with <u>extensions and improvements of distributed systems</u>. Detailed interfaces of components need to be published. New components have to be integrated with existing components. Differences in data representation of interface types on different processors (of different vendors) have to be resolved. Open systems can easily be extended and modified. It is achieved by communicating using well-defined interfaces.
   - **Concurrency Transparency**: Enables several processes to operate <u>concurrently</u> using shared information objects without interference between them. Example: NFS
   - **Scalability** is a desirable property of a system, like network, or a process, which <u>indicates its ability to either handle growing amounts of work in a graceful manner, or to be readily enlarged</u>. Allows the system and applications to expand and scale without change to the system structure or the application algorithms. Scalability denotes the ability to accommodate a growing load in the future.
   - **Fault-tolerance**: Hardware, software and networks fail. Distributed systems must <u>maintain availability even at low levels of hardware/software/network reliability</u>. Fault tolerance is achieved by <u>recovery, redundancy and RAID</u>. Fault-tolerance **refers when operations can continue even in the presence of any faults**. It is achieved in distributed system by means of replication.
   - **Transparency**: Distributed systems should be perceived by users and application programmers as a whole rather than as a collection of cooperating components.
   - **Heterogeneity** of components can arise in the programming languages, operating systems, hardware platforms and network protocols. Component heterogeneity can be accommodated by distributed systems. Often resources, i.e., hardware, software, and data need to be shared by more than one user. Distributed objects provide a sophisticated model of resource sharing. Security needs to be considered when it comes to sharing

3. Distinguish between Centralized and Distributed systems?

   - Centralized Systems
     - Centralized systems have <u>non-autonomous</u> components
     - Centralized systems are **often** built using homogeneous technology
     - Multiple users share the resources of <u>a centralized system at all times</u>
     - Centralized systems <u>have a single point of control and of failure</u>
   - Distributed Systems
     - Distributed systems have <u>autonomous</u> components
     - Distributed systems **may be** built using heterogeneous technology
     - Distributed system components <u>may be used exclusively</u>
     - Distributed systems are executed <u>in concurrent processes</u>
     - Distributed systems <u>have multiple points of failure</u>

4. Explain transparency in DS?

   - **Access transparency** means that <u>the interfaces for local and remote communication are the same</u> (Unix networked file systems)
   - **Location transparency** means that service requesters <u>do not need to know physical component locations</u> (NFS in UNIX environment, we don’t need to know the ip address).
   - **Migration transparency** means that <u>the component can be relocated without users or clients noticing it</u>. It depends on both *access and location transparency*.
   - **Replication transparency** means <u>the users and programmers do not know whether a replica or a master provides a service</u> (a replica is a component copy that remains synchronized with its original.) Example: video-on-demand. It depends on access and location transparency
   - **Concurrency transparency** means that <u>users and programmers are unaware that components request services concurrently</u>. (Bank application is an example)
   - **Scalability transparency** means that <u>users and programmers do not know *how* scalability of a distributed system is achieved</u>. (The Internet is an example). It depends on replication and migration transparency.
   - **Performance transparency** means that <u>users and programmers are unaware *how* good system performance is maintained</u>. It depends on replication and migration transparency.
   - **Failure transparency** means that <u>users and programmers are unaware of *how* distributed systems conceal failures</u>. It depends on concurrency and replication transparency. (Example: banking applications)

5. Explain Concurrency?

   - A concurrent program can be described as one that **does more than one thing at a time**.
   - Concurrency first appeared in **hardware** with e.g. dedicated I/O processors which offload processing from the main CPU.
   - Concurrency was mainly <u>*used in operating systems, with prime examples being Unix processes*</u>


- Distributed and concurrent systems both deal with "multiple things happening together"
     - **Distributed systems** deal with <u>multiple execution threads on ***more than one*** computer</u>
     - **Concurrent systems** deal with <u>multiple execution threads ***on a single*** computer</u>
     - They share some common aspects need to communicate and sharing of state, they <u>differ in the amount of shared information and in communication bandwidth</u>
     - These produce different programming concerns. 
- A common way of **dealing with some of the problems** caused by distributed systems on a local basis is to use **concurrency** techniques

6. Explain scheduling policies?

   - A process scheduler may be <u>*pre-emptive*</u> or <u>*co-operative*</u>
     - **Pre-emptive**: the <u>scheduler</u> is <u>in charge of how long a process runs</u> for. If a process exceeds its time slice, it is stopped by the scheduler
     - **Co-operative**: each <u>process</u> is <u>in charge of how long it runs</u> for. When a process feels like cooperating, it will surrender execution
   - **Pre-emptive is good, co-operative is usually bad**. Most O/S now support pre-emptive scheduling, but not all (Windows 3.1 is a major co-operative scheduler). NT has both models, to support "traditional" 16-bit Windows applications as well as newer 32-bit ones

7. Explain the terms process, threads, context switching, JAVA threads scheduling, deadlock & deadlock avoidance?

   - A **<u>*process*</u>** is <u>a program in execution</u>. <u>A process is associated with an address space a list of memory locations which the process can read and write contains the executable program, its data and its stack and a set of registers</u>, e.g., program counter, stack pointer, Program Status Word and other information needed to run the program E.g., files open, position in open files.
   - **<u>*Threads*</u>** are "lightweight processes". <u>They share more information than heavy-weight processes</u>. Typically <u>threads share the same system stack, the same heap memory and threads usually have their own procedure call/local variable stacks</u>.
   - The **<u>*scheduler*</u>** does not treat such an operation as "atomic" and may interrupt it half way through to perform a context switch to another process.
   - Two processes wish to communicate with each other, in a 2-way manner. A stalemate situation between two or more interacting processes is deadlock. Two main types of Deadlock handling Strategy and recovery
     - **Rollback**: the OS periodically checks whether two processes need the same resource, and one is “rolled back” to the state prior to requiring the resource
     - **Avoidance**: Special algorithms that decide on a scheduling order for the processes competing for the same resources





# Week 2

1. What are threads and what they are designed to solve?

   - Threads are "lightweight processes". 
   - They share more information than heavy weight processes. 
   - Threads are an attempt to deal with “Concurrency”. 
   - A concurrent program can be described as one that does more than one thing at a time. Typically threads share: <u>*the same system stack, the same heap memory*</u>

2. Name and describe two process scheduling policies. Which one is preferable and does the choice of policies have any influence on the behavior of Java threads?

   - In cooperative models, <u>once a thread is given control it continues to run until it explicitly yields control or it blocks.</u>
   - In a pre-emptive model, <u>the virtual machine is allowed to step in and hand control from one thread to another at any time</u>. Both models have their advantages and disadvantages.
   - Cooperative Threads: **Only one thread is ever active**. In other words you **cannot have a thread that runs independently** of all your other threads; for example a thread that is continuously backing up a data file, or running a report in the background. 
   - Preemptive threads **run independently of each other**. **Only one thread at a time has focus, but focus can change from one line of code to the next**. The switching between threads is under the control of the OS.

3. Write code declaring two classes that illustrate two ways threads can be implemented in Java:

   ```
   // method 1
   class MyThread extends Thread { 
   	public void run() {
   	// code for my thread declared here
   	} 
   }

   MyThread thr = new MyThread(); 
   thr.start(); //calls the run() method

   // method 2
   class MyRun implements Runnable { 
   	public void run() {
   	// code for my thread
   	} 
   }

   MyRun runner = new MyRun(); 
   new Thread(runner).start();

   ```

4. How is mutual-exclusion can be accomplished in Java and why is it needed?

   - Mutual exclusion refers to **the problem of ensuring that no two processes or threads are in their criticalstate at the same time**.


- Mutual exclusion is accomplished during execution of a particular section of code, which is regarded as a “critical section” of Java code. Methods, or blocks of code can become “critical sections”

5. Do we ever call the `stop()` method of a thread. Why not? Look up the Java API for this
   method.

   - Threads preserve class invariants when they are allowed to exit normally. Programmers often attempt to terminate threads abruptly when they believe the task is complete, the request has been cancelled, or the program or JVM must shut down expeditiously. Certain thread APIs were introduced to facilitate thread suspension, resumption, and termination but were later deprecated because of inherent design weaknesses. For example, the `Thread.stop()` method causes the thread to immediately throw a <u>*ThreadDeath exception*</u>, which usually stops the thread.
   - Invoking `Thread.stop()` results in **the release of all locks a thread has acquired, potentially exposing the objects protected by those locks when those objects are in an inconsistent state**. The thread might catch the ThreadDeath exception and use a finally block in an attempt to repair the inconsistent object or objects. However, this requires careful inspection of all synchronized methods and blocks because a ThreadDeath exception can be thrown at any point during the thread's execution. Furthermore, code must be protected from ThreadDeath exceptions that might occur while executing catch or finally blocks. Consequently, **programs must not invoke** `Thread.stop()`. 
   - Removing the `java.lang.RuntimePermission` stopThread permission from the security policy file prevents threads from being stopped using the `Thread.stop()` method. Although this approach guarantees that the program cannot use the `Thread.stop()` method, it is nevertheless strongly discouraged. Existing trusted, custom-developed code that uses the `Thread.stop()` method presumably depends on the ability of the system to perform this action. Furthermore, the system might fail to correctly handle the resulting security exception. Additionally, third-party libraries may also depend on use of the `Thread.stop()` method.
   - Because it is inherently unsafe; **stopping a thread causes it to unlock all the monitors that it has locked**. (The monitors are unlocked as the ThreadDeath exception propagates up the stack.) **If any of the objects previously protected by these monitors were in an inconsistent state, other threads may now view these objects in an inconsistent state**.

6. What is “deadlock” and what are the total conditions for deadlock to occur?

   - A deadlock is a situation in which **<u>two or more competing actions are each waiting for the other to finish, and thus neither ever does</u>**. 
   - In an operating system, a deadlock is a situation, which **occurs when a process enters a waiting state because a resource requested by it is being held by another waiting process**, which in turn is **waiting for another resource**. If a process is unable to change its state indefinitely because the resources requested by it are being used by other waiting process, then the system is said to be in a deadlock. 
   - A deadlock situation can arise if and only if all of the following **conditions** hold simultaneously in a system:
     - **Mutual Exclusion**: At least one resource must be non-shareable. Only one process can use the resource at any given instant of time.
     - **Hold and Wait** or **Resource Holding**: A process is currently holding at least one resource and requesting additional resources which are being held by other processes. 
     - **No Pre-emption**: The operating system must not de-allocate resources once they have been allocated; they must be released by the holding process voluntarily.
     - **Circular Wait**: A process must be waiting for a resource which is being held by another process, which in turn is waiting for the first process to release the resource. In general, there is a set of waiting processes, P = {P1, P2, ..., PN}, such that P1 is waiting for a resource held by P2, P2 is waiting for a resource held by P3 and so on till PN is waiting for a resource held by P1

7. What is the difference between deadlock detection and deadlock prevention?

   - Deadlock <u>prevention</u> is to **ensure that deadlocks never occur**. 
   - Deadlock <u>avoidance</u> is attempting to **ensure that resources are never allocated in a way that might cause deadlock**.





# Week 3

1. What is meant by the term “architecture" in the context of networks and distributed computing?

   - The **design of a computer network**.
   - “The **blueprint** that provides **a framework and technology foundation for designing, building and managing a communication network**.” 
   - “The **communication equipment, protocols and transmission links that constitute a network, and the methods by which they are arranged**.”
   - “The infrastructure, functionality, protocols, and standards implemented in a particular network design.”

2. What do we mean by the term “protocol” in the context of networks and distributed computing and why are protocols needed?

   - Protocol: **conventions**, expected languages or behaviours. 
   - A set of **rules** that <u>govern communication between hardware and/or software components</u>.
   - The processes have to have a protocol in place so that <u>message exchange or communication can take place **meaningfully**</u>. 
   - Protocols are needed so that <u>communicating devices and/or processes know what to expect and what is expected</u>. 
   - Devices and processes can <u>only communicate successfully if the agree to speak a common language</u>.

3. Name two connection models and the features of each model.

   - **Connection-Oriented Protocols** With connection-oriented protocols, you must establish a logical connection with the communication partner before exchanging data. This method of connection:
     - Is highly <u>*reliable*</u> (because of acknowledgements )
     - Requires <u>*more computational processing*</u>
     - Has <u>*more overhead*</u> because of connection establishment and termination
   - **Connectionless Protocols** With connectionless protocols, establishing a connection before sending data is not necessary. It uses self-contained messages that:
     - Include the <u>*full message*</u>
     - Do <u>*not*</u> require any <u>*response*</u>
     - Has <u>*no built-in reliability features*</u>, and therefore is best suited for use in highly reliable networks or when application itself can retransmit packets based on some other criteria (timeout, etc.).
     - Has <u>*lower overhead*</u> because it has no connection and no setup requirements.

4. Name and describe three distributed computing models?

   - **Peer-to-Peer**: If both components are <u>equivalent</u>, both <u>able to initiate and to respond to messages</u>, then we have a peer-to-peer system. 
     - *Note that this is a logical classification: one peer may be a 16,000 core mainframe; the other might be a mobile phone. But if both can act similarly then they are peers*.
   - **Filter**: A second model is the so-called filter. Here **<u>one component passes information to another which modifies it before passing it to a third</u>**. 
     - This is a fairly common model: for example, the middle component gets information from a database as SQL records and transforms it into an HTML table for the third component (which might be a browser).
   - **Client-Server**: At the highest level, we could consider the equivalence or the non-equivalence of components of a distributed system. 
     - The most common occurrence is an asymmetric one: **<u>a client sends requests to a server, and the server responds</u>**. This is a client-server system.

5. What could be described as the strength(s) or attraction of the client/server model?

   - The client-server model was originally developed to **allow more users to share access to database applications**. 
   - Compared to the mainframe approach, client-server **offers improved scalability** because <u>connections can be made as needed rather than being fixed</u>. 
   - The client-server model also **supports modular applications that can make the job of creating software easier**. 
   - In so-called "two-tier" and "three-tier" types of client-server systems, software applications are **separated into modular pieces**, and each piece is **installed on clients or servers** specialized for that subsystem.

6. Name and describe 4 models for server distribution.

   - Single Client – Single Server

     ![11](https://ws1.sinaimg.cn/large/006tKfTcgy1fg7wtduj7sj30oc064jrs.jpg)

   - Multiple Clients – Single Server

     ![m1](https://ws1.sinaimg.cn/large/006tKfTcgy1fg7wtn7lswj315i0fe40a.jpg)

   - Single Client – Multiple Servers

     ![1m](https://ws3.sinaimg.cn/large/006tKfTcgy1fg7wtl7kk0j30ym06wwfc.jpg)

   - Multiple Clients – Multiple Servers

     - In this, the **master** **receives requests** and instead of handling them one at a time itself, **passes them off to other servers to handle**. This is a common model when concurrent clients are possible. 
     - **Master/slave** is a model for a communication protocol where **one device or process has unidirectional control over one or more other devices**. Once a master/slave relationship between devices or processes is established, the direction of control is always from the master to the slaves. In some systems a master is elected from a group of eligible devices, with the other devices acting in the role of slaves. This occurs frequently when a server needs to act as a client to other servers, such as a business logic server getting information from a database server. And of course, there could be multiple clients with multiple servers

7. What categorizing clients and servers as either “fat “ or “thin”? 

   - Clients and servers may be classified as "fat" or "thin" 
   - Fat clients **use up space on each client they run on**, may have complex installation requirements, etc. (e.g. Netscape or IE - which "has" to be part of the O/S). 
   - Thin clients have **reduced functionality, but are easier to manage**. 
   - The network computer model **favours <u>thin</u> clients**. A common labeling of components is "fat" or "thin". Fat components take up lots of memory and do complex processing. Thin components on the other hand, do little of either. There don't seem to be any "normal" size components, only fat or thin. Fatness or thinness is a relative concept. Browsers are often lapelled as thin because "all they do is display web pages".

8. What is middleware?

   - Middleware is the "glue" <u>connecting components of a distributed system</u>. 
   - Software that is logically placed between the higher level layer consisting of users and applications and layer underneath consisting of other services and the o/s.

9. What is an IP address? How is it constructed? 

   - "IP" stands for **Internet Protocol**, so an IP address is an Internet Protocol address. 
   - An Internet Protocol is **a set of rules** that <u>govern Internet activity and facilitate completion of a variety of actions on the World Wide Web.</u> 
   - Internet Protocol address is part of the systematically laid out interconnected grid that <u>governs online communication by identifying both initiating devices and various Internet destinations</u>, thereby making two-way communication possible.
   - An IP address consists of four numbers, each of which contains one to three digits, with a single dot (.) separating each number or set of digits.
   - Each of the four numbers can range from 0 to 255. 
   - Without this numeric protocol, sending and receiving data over the World Wide Web would be impossible. 
   - The Internet uses an address scheme for machines so that they can be located. The address is a 32 bit integer which gives the IP address for IPv4 or for IPv6 is 128 bit. This encodes a network ID and more addressing. The network ID falls into various classes according to the size of the network address.
   - The IP layer provides: 
     - a connectionless and unreliable delivery system
     - it considers each datagram independently of the others
     - any association between datagrams must be supplied by the higher layers.
     - supplies a checksum that includes its own header
     - header includes the source and destination addresses.
     - handles routing through an Internet.
     - responsible for breaking up large datagrams into smaller ones for transmission and reassembling them at the other end. 

10. What are symbolic names?

- Each host has a name. This can be found from the Unix user level command *hostname*
- A symbolic name for the network also exists. For our network it is "*monash.edu.au*".
- Each subnet also has a name, such as “infotech”. The symbolic network name for any host is formed from the two: *infotech.monash.edu.au* 

11. How do you get/manipulate an Internet address in Java? 

    - The Java class InetAddress can be used to get/manipulate internet addresses. Methods
      include:

      ```
      static InetAddress getByName(String host)
      static InetAddress getLocalHost()
      String getHostAddress(); // in dotted form
      String getHostName();
      GetInetInfo.java
      ```

12. What is a port, what are “well-known” ports, and what is a socket? 

    - In this context a port is a logical connection. It is an abstraction in the computer’s memory it is NOT a physical entity.
    - A socket is a connection for communication between two machines.
    - A service exists on a host, and is identified by its port.
    - A 16 bit number (0-65,000). To send a message to a server you send it to the port for that service of the host that it is running on.
    - This is not location transparency! Certain ports are "well known". In Unix O.S, they
      are listed in the file /etc/services. For example,
      - ftp: 21/tcp
      - time: 37/tcp
      - Time: 37/udp
      - Finger 79/tcp
    - Ports in the region 1-255 are reserved by the IETF (Internet Engineering Task Force). The system may reserve more. User processes (in Unix) may have their own ports above 1023. Ports 1-1023 are referred to as “well-known” ports

13. What does the ServerSocket method `accept()` do?

    - Listens for a connection to be made to this socket and accepts it. The method blocks until a connection is made. A new Socket s is created, i.e. returns a new Socket.






# Week 4

1. why do two or more communicating processes need a protocol?
   - Protocol–conventions–expected languages or behaviours. Often referred to as handshaking (manners). “A set of rules that govern communication between hardware and/or software components” 
   - The processes have to have a protocol in place so that **<u>*message exchange or communication can take place meaningfully*</u>**. Protocols are needed so that communicating devices and/or processes know <u>what to expect and what is expected</u>. Devices and processes can only communicate successfully if the agree to speak a common language.
2. What do we mean by broadcast vs. point-to-point?
   - <u>Broadcast</u>: A method of sending a signal where **multiple parties may hear a single sender**. 
   - <u>Point-to-point</u>: A method of communication where **one "point" (person or entity) speaks to another entity**.
3. What do we mean by state (or state-full) vs. stateless?
   - In general, "state" refers to **information about the current conditions of program execution** — runtime data stored in memory. 
   - State-full Protocols: 
     - A state-full protocol is a protocol in which **part of the data that is exchanged between the client and the server systems includes state information**. Both systems may track the state of the communication session.
     - The disadvantage of state-full protocols is the **overhead** incurred in maintaining state information.
     - The advantage of state-full protocols is **reliability** and **recovery** in the event of failure
   - Stateless protocols:
     - Protocols in which **neither the client nor the server system has an obligation to keep track of the state of the communication session**.
     - The disadvantage of stateless protocols is that they **do not support most reliability features**; and **data** that were sent can be **lost or delivered** out-of sequence. 
     - The main advantages of stateless protocols are **lower overhead** and a degree of **isolation** between the client and the server. 
4. What do we mean by reliable vs. unreliable protocols?
   - Reliable Protocols: 
     - A reliable protocol requires that **each transmission is acknowledged by the receiving host**. The sender retransmits, if necessary.
   - Unreliable Protocols: 
     - An unreliable protocol **does not require** that each transmission is **acknowledged** by the receiving host.
5. What do we mean by version control, what problem is associated with it. Does Java have a way of overcoming the problem?
   - A protocol used in a client/server system will evolve **over time**, c**hanging as the system expands**, which **raises <u>*compatibility*</u> problems**. <u>Each side should ideally be able to understand messages for its own version and all earlier ones.</u>
   - **JNLP (Java Network Launching Protocol)** is one attempt to overcome version problems for client-side applications.
6. What is data serialisation and what is the problem with respect to serialisation, programming languages and network programming?
   - <u>Messages are sent across the network as a sequence of bytes</u>, which has no structure except for a linear stream of bytes.
   - Programming languages use structured data such as
     - record/structure
     - variant records
     - array - fixed size or varying
     - string - fixed size or varying
     - tables - e.g. arrays of records
     - non-linear structures such as
       - circular linked list
       - binary tree
       - objects with references to other objects
   - There must be some agreement (protocol) on how to send such data.
   - Serialization (referring to objects) is the term used for **marshalling data** — which is the process of **<u>*breaking down data into a stream of bytes so that it can be sent over a communications channel*</u>**.
   - Deserialization (when referring to objects object) or the **un-marshalling** — is the process of **<u>*unpacking and reconstructing the data after it has been delivered*</u>**.
7. Name the methods of the Serializable interface in Java. What is the benefit of having a class implement the Serializable interface?
   - Java classes can be marked as implementing the interface Serializable. This interface has no methods, so no extra code has to be written for Serializable classes.
   - This allows an object (and all objects it references) to be written out (e.g. to a file) and then read back and restored. If a class is Serializable, then the methods `ObjectOutputStream.writeObject()` and `ObjectInputStream.readObject()` can be called.
8. The lecture mentioned communication between processes in terms of messages and message formats – byte and character. What was one thing these formats had in common with respect to “protocol”?
   - An input stream **lets an application read message from an underlying input stream** in a <u>machine-independent/Platform-independent/Architecture independent way</u>. 
   - An application **uses an output stream to write data that can later be read by an input stream**.



# Week 5

1. Applications often make use of “state” information. What do we mean by the term “state”?

   - By using this term we try to **indicate the current status of the system**, i.e. we mention what is going on. 
   - For example:
     - Keeping file pointers to current file location
     - Keeping current mouse position
     - Keeping current customer value

2. What are the important issues with respect to state in distributed systems?

   - In distributed system, we have to **make sure state information of the transaction or interaction** between **client and server process** have to be **maintained** carefully so that **both <u>can agree on</u> that and in case failure we should be able to <u>revert back</u> to a previous state**. 
   - In a distributed system, such state information **may be** kept **in** the **client** or in the **server** or in **both**.

3. With reference to the Week 4 Lecture slides, and the handouts, describe the Half Object plus Protocol design pattern. In particular, you should clarify the reason for the peculiar name of the pattern in terms of “Half-Object” and “plus Protocol”

   - To avoid the communicating object code to be procedural, it can be split in two: 
     - **one half** in the **client address space**
     - **the other half** in the **server address space**
   - The two half-objects will <u>**communicate using a private protocol**</u> that is unknown to the rest of the application. 
   - The private protocol here will be "message passing using <u>sockets</u>". Other implementations may use CORBA, RMI, JXTA, etc. 
   - This allows the implementation of the **HOPP objects** to be **changed** <u>*without*</u> affecting the rest of the application.

4. Draw class diagrams of a distributed system to illustrate your understanding of how the HOPP pattern is implemented?

   ![hopp](https://ws2.sinaimg.cn/large/006tKfTcgy1fg7wu8vqx8j30u40cqgmn.jpg)

5. What do we mean by “mutual agreement” when referring to structured data?

   - If the server decides to send e.g. an int, a byte and a null terminated string, then the client must be able to read them in this form. 
   - Mutual agreement means that **the client and the server must have agreed beforehand on the format of the messages**. <u>No information about the format is exchanged, because both client and server will be in mutual agreement and knows what to expect</u>. 
   - This method is commonly used. e.g. by most Remote Procedure Call (RPC) protocols. There is <u>no overhead or redundant information. **Only the necessary data is sent**</u>.

6. What is the problem with “mutual agreement” and how can it be overcome?

   - Mutual agreement is **not type safe**. 
     - If the server sends an int instead of a byte, then the client will just get the wrong data. It may even crash. 
   - Safer messages include some **sort of type information** as part of the message.

7. What is MIME?

   - MIME can be abbreviated as **Multipurpose Internet Mail Extensions**, which is designed for two purposes: 
     - to allow messages **composed** of **multiple parts**. For example, an archive of messages is maintained
     - to **handle non-ASCII data**

8. What is ASN.1?

   - ASN.1 can be abbreviated as **Abstract Syntax Notation 1**, which is designed as a “<u>self-describing data</u>”. 
   - ASN.1 has a number of basic and derived data types like, Integer, IA5SATRING (ASCII), Octet String, Sequence, Set of. 
     - A set of data is then given as a tagged sequence of data. 
     - Then each tag is given a value as a byte, and the primitive values are encoded. 
     - The rules for this are totally obscure, so that even elementary tutorials are nearly impossible to read. 
   - The result is **a sequence of bytes** that can be decoded by an ASN.1 parser into a set/sequence of data values of the correct types. This is a byte-format method.

9. What is XML? 

   - XML is the current favourite for the representation of structured data. 

   - It is a **character-format method** and simple XML documents are **human readable**. 

     - XML allows us to define our own tags as <u>*strings*</u>. 
     - Tags may be <u>*nested*</u>. 
     - To <u>*each begin tag there is an end-tag*</u>, except for the empty tags. 

   - Tags may also possess attributes to give more information about the tag. For example, a login message sent from client to server.

     ```
     <login-request>
     	<name> user21 </name> 
     	<password> abcdefg </password>
     </login-request>

     // The reply may be one of
     <login-reply status="succeeded" /> 
     // or
     <login-reply status="failed" />
     ```






# Week 6

1. What is the "Orange Book"?

   - Trusted Computer System Evaluation Criteria (TCSEC) is a United States Government Department of Defense (DoD) standard that **sets basic requirements for assessing the effectiveness of computer security controls** built into a computer system. 
   - The TCSEC was used to **evaluate, classify and select computer systems being considered for the processing, storage and retrieval of sensitive or classified information**. 
   - The TCSEC, frequently referred to as the Orange Book, is **the centerpiece of the DoD Rainbow Series publications**. Initially issued by the National Computer Security Center (NCSC) an arm of the National Security Agency in 1983 and then updated in 1985, TCSEC was replaced with the development of the Common Criteria international standard originally published in 2005. Such is the case of the Orange Book. 
   - **Different organizations required different levels of security**, and because **security professionals needed a metric to gauge if a computer system was secure enough for the intended purpose, the government developed the Trusted Computer System Evaluation Criteria (TCSEC) and published them in a book that had an orange cover, hence the nickname "Orange Book."** The Orange Book was part of a family of publications on security with different color covers called the Rainbow Book series.

2. The Orange Book defined four broad hierarchical divisions of security protection. In increasing order of trust, what were they?

   - The Orange Book defined four broad hierarchical divisions of security protection. In increasing order of trust, they were:
   - D: Minimal security
   - C: Discretionary protection
     - C1 — Discretionary Security Protection
       - Identification and authentication
       - Separation of users and data
       - Discretionary Access Control (DAC) capable of enforcing access
       - limitations on an individual basis
       - Required System Documentation and user manuals
     - C2 — Controlled Access Protection
       - More finely grained DAC
       - Individual accountability through login procedures
       - Audit trails
       - Object reuse
       - Resource isolation
   - B: Mandatory protection
     - B1 — Labelled Security Protection
       - Informal statement of the security policy model
       - Data sensitivity labels
       - Mandatory Access Control (MAC) over selected subjects and objects
       - Label exportation capabilities
       - All discovered flaws must be removed or otherwise mitigated
       - Design specifications and verification
     - B2 — Structured Protection
       - Security policy model clearly defined and formally documented
       - DAC and MAC enforcement extended to all subjects and objects
       - Covert storage channels are analysed for occurrence and bandwidth
       - Carefully structured into protection-critical and non-protection-critical
         elements
       - Design and implementation enable more comprehensive testing and
         review
       - Authentication mechanisms are strengthened
       - Trusted facility management is provided with administrator and operator
         segregation
       - Strict configuration management controls are imposed
     - B3 — Security Domains
       - Satisfies reference monitor requirements
       - Structured to exclude code not essential to security policy enforcement
       - Significant system engineering directed toward minimizing complexity
       - Security administrator role defined
       - Audit security-relevant events
       - Automated imminent intrusion detection, notification, and response
       - Trusted system recovery procedures
       - Covert timing channels are analyzed for occurrence and bandwidth
       - An example of such a system is the XTS-300, a precursor to the XTS-400
   - A: Verified protection
     - A1 — Verified Design 
       - Functionally identical to B3
       - Formal design and verification techniques including a formal top-level specification
       - Formal management and distribution procedures
       - An example of such a system is Honeywell's Secure Communications Processor SCOMP, a precursor to the XTS-400

3. What are some of the stated functions needed for security – what do they mean?

   - Identification
   - **Authentication**: proof of identity (you can elaborate more)
   - **Authorization**: privileges belonging to identity (you can elaborate more)
   - **Integrity**: data is not tampered with (you can elaborate more)
   - **Confidentiality**: data is not exposed to others (you can elaborate more)
   - **Delegation** and **administration** (you can elaborate more)
   - **Recording** (you can elaborate more)
   - **Monitoring** (you can elaborate more)

4. What are the 3 broad ways of achieving network security?

   - Isolating the network
   - using firewalls and
   - using proxy servers

5. What is a firewall?

   - A firewall is **software or hardware-based network security system** that **controls the incoming and outgoing network traffic** <u>by analyzing the data packets and determining whether they should be allowed through or not, based on a rule set.</u>
   - A network's firewall <u>builds a bridge between the internal network or computer it protects, upon securing that the other network is secure and trusted, usually an external (inter)network</u>, such as the Internet, that is not assumed to be secure and trusted.

6. What is a proxy server?

   - A proxy server is **a server (a computer system or an application) that acts as an intermediary** for <u>requests from clients seeking resources from other servers</u>. 
   - <u>A client connects to the proxy server,</u> <u>requesting some service</u>, such as a file, connection, web page, or other resource available from a different server and <u>the proxy server evaluates the request as a way to simplify and control its complexity</u>. 
   - Today, most proxies are web proxies, facilitating access to content on the World Wide Web.

7. What are some of the security lessons for client server computing?

   -  Verify IP origin
   - Use logging
   - Care with user configurable files
   - Care with passwords
   - Use handshaking
   - Keep security layer simple
   - Encrypt sensitive data
   - Design protocol to allow security checks
   - Ensure your protocol is allowed by security manager if crossing firewalls
   - More likely to find UDP blocked than TCP

8. What is a cipher?

   - Ciphers are certain cryptographic rules to <u>replace the plan text with a special form of text that is not understandable by the eavesdropper</u>, but it <u>can be converted back to original form at the destination</u>. 
   - **Substitution ciphers** are <u>easy</u> (e.g. 'a' replaced by 'b', 'b' replaced by 'c', etc.) and therefore they are relatively easy to crack. 
   - **Vernam ciphers** (one-time pad) can be totally secure, but are <u>impractical</u>.

9. What is DES?

   - Data Encryption Standard. US Govt. standardized this symmetric encryption algorithm since 1977. 
   - It uses 56-bit key and has very strong "Strong" algorithm that has very complex mathematical calculations. 
   - The underlying theory is based of the Fiestel function that operates on 64-bits of plaintext data. 
   - However, being the small key size, it can be cracked and therefore more than open application of DES is recommended. 
   - Triple-DES more secure. Triple-DES uses DES 3 times with 2 or 3 keys.

10. What does “secret key” encryption mean?

   - In “secret key” encryption, both the encryption and decryption is done using the same common key. 
   - This key must be kept in secret from all the others, and this key must be known to at least two people between whom the encryption is being done.

11. What does “public key” encryption mean?

    - In “public key” encryption, a pair of keys namely; the private and public key are needed. 

    - One of the keys is used to encrypt and the other to decrypt the text. 

    - Both these keys are generated at the same time and equally needed. 

    - Either of them cannot be derived easily from the other. 

    - The public key encryption between the sender and recipient can be seen in the figure below. 

    - When the Sender wants to send a message to recipient, it has recipient’s public key using which the sender encrypts its message which is decrypted by only the recipient using its private key.

      ![publickey](https://ws4.sinaimg.cn/large/006tKfTcgy1fg803zq9lgj30ys0komyx.jpg)

12. What is a digital signature?

    ![digitsignature](https://ws1.sinaimg.cn/large/006tKfTcgy1fg80426qr1j30va0sojua.jpg)

    - B wants to send a message to A. And A wants to check if it came from and un-tampered B. 
    - B encrypts the message using it private key and A can use B’s public key to decrypt it. 
    - There can be a chance that A received a garbage message that didn’t come from B or the message was changed in the transit. 
    - This tampering can be avoided by using digital signature, through which B can stamp the document and give the document its identity, through which A can identify that it came from B. 
    - The digital signature can be done by initially using hash algorithm to encrypt the text, and then sign the doc and hash function using its private key. This when given to A, checks the source to be B by the signature which can be checked using B’s public key.

13. What are some of Java’s responses to security needs in applications？

    - From JDK 1.2, Java provides a security manager on which the applications can be run. 
    - This can be set at run time by using the command `java -Djava.security.manager` and this can be set using code with the function `System.setSecurityManager(new SecurityManager())`. 
    - This can fail, if the current security permissions do not allow a security manager to be set. If the `System.getSecurityManager()` is null then a security manager can always be set. 
    - The security manager needs security policy which can be set at command line by `java -Djava.security.policy = someURL`. 
    - Policy file can have keystore which is used to use the digital signature and jarsigner to sign the jar files. Java 1.4 provide Java Cryptographic Extension by defining private key algorithms like DES.









# Week 7

1. What is a Remote Procedure Call?

   - Remote Procedure Call or RPC acts like a procedure call buts operates across a network transparently
   - The process makes a RPC call by pushing its parameters and a return address onto the stack and jumps to the start of the procedure. The procedure itself connects and operates through the network. After the procedure returns to the return address, it behaves like a normal procedure call.

2. What are “stubs” in the context of Remote Procedure Calls? 

   - The stub is <u>a piece of code</u> that exists on the **client side** which <u>receives the procedure call and sends all parameters to the remote machine and waits for a reply</u>.
   - When the program is run and the procedure call is issued, the stub receives the request and forwards it to a client runtime program in the local computer. The client runtime program has the knowledge of how to address the remote computer and server application and sends the message across the network that requests the remote procedure. Similarly, the server includes a runtime program and stub that interface with the remote procedure itself. Results are returned the same way.

3. Draw a diagram and describe the execution order of a Remote Procedure Call?

   ![rpc](https://ws3.sinaimg.cn/large/006tNc79gy1fgbbnv7tzzj30ms0n6tar.jpg)

   - Clients calls a local procedure on the client stub.
   - The client stub acts as a proxy and marshalls the call and the arguments.
   - The client stub send this to the remote system (via TCP/UDP).
   - The server stub un-marshalls the call and arguments from the client.
   - The server stub calls the actual procedure on the server.
   - The server stub marshalls the reply and sends it back to the client.

4. What is the relationship between RPC and HOPP?

   - RPC is like a HOPP or a procedural example of HOPP. 
   - The client-side implementation establishes a socket connection, sends parameters and reads results. However, like HOPP, its server-side implementation is called by a server and contains the real implementation of the procedure.

5. What are the components of RPC?

   - An RPC system consists of the following pieces:
     - set of data types that can be sent as parameters and receives results
     - representation of these data types
     - message format for sending procedure name and parameters and getting
       procedure reply
     - means of representing the procedures and their signatures
     - mechanism for automatically generating client stub and server stub

6. What is RMI?

   - RMI stands for (Remote Method Invocation). RMI is a cross between remote procedure call and mobile objects. A server side object is created along with a stub object wherein both implement a well-known interface. The server side object remains on the server and receives and executes remote method calls.
   - The stub is moved as a mobile object to a client and the client makes calls on the stub which makes remote calls on the server side object. RMI is usually a Java API that performs the object-oriented equivalent of remote procedure calls (RPC), with support for direct transfer of serialized Java objects and distributed garbage collection.

7. How is RMI implemented?

   - Simply by creating two processes and provides an extended remote interface.
     - Start with an interface specification
     - Write a Class that Implements the Interface
     - Create the Server Process
     - Create the client process

8. What is the role of a remote object server?

   - The role of the server is to
     - Creating the remote object
     - Exporting it to the RMI runtime system
     - Make it publicly visible in some way
     - Stay alive to respond to calls on the object - this is done automatically by the RMI runtime because it spawns another thread during construction
     - Ensure that the client know where the class files are stored. This is done by
       setting the property java.rmi.server.codebase to a URL

9. How are objects found in RMI?

   - One way to find object is using the RMI registry, this is a simple database of remote objects that builds up. Furthermore, Objects can be discovered using the RMIT registry as follows:

     ```
     Hello greeting = (Hello)Naming.lookup(“rmi://localhost/Hello”);
     ```





# Week 8

1. What is CORBA?
   - CORBA is the acronym for "Common Object Request Broker".
   - It is an extension of RPC that uses object methods instead of procedure calls.
   - It is used as middleware when construction distributed applications.
2. What is an ORB and what is its role?
   - ORB is the acronym for "Object Request Broker".
   - The role of an ORB is to marshall parameters, transfer data, make calls on a remote system and return the result.
3. Name 3 ways that objects may be located in CORBA
   - The 'Naming Service', this allows registered CORBA object to be located by name.
   - The 'Object Trader Service', this allows CORBA object to be located by
     services based on operation names, parameters and the type of result.
   - “Stringified” object reference if no naming service is available.
4. What is a CORBA IDL and why is it needed?
   - An IDL is an Interface Definition Language. 
   - This allows language independence since a given IDL description of an object may be understood by a variety of programming languages.
5. IDLs support inheritance. How is inheritance declared in an IDL declaration and how does it map to Java’s inheritance model?
   - IDL's have an interface definition that has support for inheritance, indicated by a colon followed by the inherited entity. For example (from the lecture notes), 'interface Rectangle: Shape {...}' indicates that Rectangle inherits Shape. Java uses interfaces to support inheritance.
6. IDL operations, analogous to Java methods, allow you to declare parameters of 3 “kinds”. What are they and what do the differences mean?
   - IN this type of parameter is input only and may be passed by value.
   - INOUT this type of parameter is analogous to the being 'passed by reference'. It passes a value into the call, but then expects a possibly updated, value to be returned.
   - OUT this type of parameter is used solely to store a result. Any value existing on input to the procedure will be ignores.
7. What are the 3 standardized formats under which CORBA objects can communicate?
   - CORBA objects can communicate using:
     - GIOP - General Inter-ORB Protocol
     - IIOP - Internet Inter-ORB Protocol
     - IOR - Interoperable Object Reference.
8. How is a “naming service” found in Java and how does a service register itself with a “naming service” in Java?
   - A naming service is found by the following code:
     - `org.omg.CORBA.Object obj;`
     - `org.omg.CosNaming.NamingContext nameComp;`
     - `obj = orb.resolve_initial_references("NameService");`
     - `nameComp = org.omg.CosNaming.NamingContextHelper.narrow(obj);`
   - A service registers with the naming service by passing its name, as a simple string, and an object reference to itself.
9. What does a “client” use the “naming service” for in Java?
   - To obtain a reference to the object with which it wishes to communicate.
10. What are the benefits of using EJBs?
    -  EJBs simplify the task of creating large distributed applications.
11. What are different types of EJBs and how are they used?
    - Session beans - encapsulate business logic and may be invoked, by a client, over local, remote or web service client views.
    - Message driven beans - Integrate with external systems by means of asynchronous messages that use the Java Messaging Service.
12. How EJBs achieve their benefits?
    - The EJB container provides system level services to the enterprise beans. This permits the developer to concentrate on only business logic, rather than having the extra task of handling the system services as well. Since beans contain the business logic it allows the developer, of a client application, to concentrate on the presentation logic resulting in a thinner client. EJBs are portable. Applications can potentially be constructed from existing beans.
13. How can EJBs be accessed by local and remote clients?
    - EJBs can only be accessed by the methods in their business interface or, in the case of a no-interface view, via its public methods. Clients need a reference to the EJB, which may be either through dependency injection or by JNDI lookup.







# Week 9

1. What are the historical issues that have led to Web Services? 
   - Integration issues, multiple platforms, middleware was platform specific. So from business standpoint Integration, within an organization, between companies, Allows time/cost efficiencies, Purchase orders, Answering inquiries, processing shipment requests, Do this without locking in to a single partner/vendor
2. What the service based architectures that evolved as an attempt to solve the historical issues?
   - Middleware components from different vendors
3. What are the problems with this approach?
   - The middleware soft wares are vendor specific and not compatible with many platforms. Web services are a new version of RPC, heavily reliant on XML; they have all the disadvantages we see in RPC such as Location dependence, Slow, Prone to network errors, Prone to security attacks, In addition, they have their own disadvantages, Verbose transport protocol, Heavy processing on client and server, Heavily centralized services in UDDI.
4. What is a Web Service? 
   - A web service is an interface that describes a collection of operations that are network accessible through standardized XML messaging. 
   - A Web service is a software system identified by a URI, whose public interfaces and bindings are defined and described using XML. Its definition can be discovered by other software systems.
   - These systems may then interact with the Web service in a manner prescribed by its definition, using XML based messages conveyed by internet protocols.
   - Web services allow applications and agents to browse the Web on behalf of users. Instead of a user navigating HTML screens, an agent can connect to services on the Web and interact with them directly without the distraction of presentation elements. 
   - SOAP/WSDL/UDDI is the technologies behind Web services.
5. What is the difference between Web Services and SOA?
   - Web Services are self-describing services that will perform well defined tasks and can be accessed through the web. By definition SOAP is "Simple Object Access Protocol". It is "a lightweight protocol for exchange of information in a decentralized, distributed environment". While Web service provides messaging and invocation; It is an XML based protocol so takes advantage of. XML Namespaces, XML Schema. 
   - Service Oriented Architecture (SOA) is (roughly) an architecture paradigm that focuses on building systems through the use of different Web Services, integrating them together to make up the whole system.
6. What do Web Services provide?
   - They are services that perform well defined tasks and are accessible through the web. 
   - Web services allow applications and agents to browse the Web on behalf of users and Instead of a user navigating HTML screens, an agent can connect to services on the Web and interact with them directly without the distraction of presentation elements. 
   - SOAP/WSDL/UDDI is the technologies behind Web services.
7. Why are XML Web Services the most widely used type of service?
   - XML is a language that is compatible with all languages and is platform independent. It is human readable. Web Services use XML extensively, and use DTD (Document Type Definition) and XML schema. XML-defined standard data types are required. XML generators and parsers are required
8. Who uses Web Services?
   - Web Services are combined to solve massive tasks in all industries. For example Web services are used within the organization between the companies, Allows time/cost efficiencies, purchase orders and processing of shipment requests.
9. What are the Web Service components WSDL, SOAP and UDDI?
   - WSDL - web services definition language - xml based interface description language that is used to describe functionality of a web service
   - SOAP - simple object access protocol - protocol used to exchange information in a distributed environment
   - UDDI - universal description discovery and integration - resource registration and lookup mechanism. It is not used widely anymore except for internal services.
10. What are the benefits of Web Services?
    - Provides Remote procedural calls and allows distributed and decentralized systems to function with service oriented architecture. Web services allow applications and agents to browse the Web on behalf of users. Instead of a user navigating HTML screens, an agent can connect to services on the Web and interact with them directly without the distraction of presentation elements.
11. What sort of environmental support is needed by Web Services?
    - They are RPC on port 80 which runs on a HTTP server. 
    - It requires a user agent that is not a browser to prepare requests and understand responses.
    - Web Services requires the following environmental support
      - An HTTP server configured to pass Web Service requests to a CGI script / servlet / JSP / ASP
      - A user agent that is not a browser to prepare Web method requests and understand responses
      - The user agent may make use of a browser for handling HTTP requests from the user side.
      - Firewall access to allow arbitrary content to pass on port 80 (could be exploited as a security hole)
12. What are some of the disadvantages of Web Services?
    - Security - very difficult to setup & Prone to security attacks
    - Not Object Oriented and has no language bindings
    - Not lightweight
    - Network dependent & Prone to network errors
    - No thin clients, both the server and client do heavy processing
    - Slow
    - Location dependence
    - Verbose transport protocol
    - Heavily centralized services in UDDI





# Week 10

1. What is JMS?
   - The Java Message Service (JMS) API is a Java Message Oriented Middleware (MOM) API for sending messages between two or more clients. JMS is a part of the Java Platform, Enterprise Edition, and is defined by a specification developed under the Java Community Process as JSR 914. It is a messaging standard that allows application components based on the Java Enterprise Edition (JEE) to create, send, receive, and read messages. It allows the communication between different components of a distributed application to be loosely coupled, reliable, and asynchronous.
2. What are JMS elements?
   - A JMS (Java Message Service) application is composed of the following parts:
     - A JMS provider: A messaging system that implements the JMS specification.
     - JMS clients: Java applications that send and receive messages.
     - Messages: Objects that are used to communicate information between JMS clients.
     - Administered objects: Preconfigured JMS objects that are created by the administrator for the use of JMS clients.
3. What are the two message delivery models that JMS API supports?
   - There are actually 3 message delivery models: Point-to-point (queue destination), Publish-subscribe (topic destination), and Request-Reply messaging.
   - The Java Message Service (JMS) provides a standard Java-based interface to the message services of a MOM of some other provider. Messaging systems are classified into different models that determine which client receives a message.
   - The most common messaging models are:
     - Point-To-Point Messaging
       - Messages are sent from an origin point to a destination point. They are sent through a queue system in the middle. The queue itself is a long-lived service. The source and destination may be transient. The source establishes a session with the queue and sends messages to it synchronously. 
       - The destination establishes a session with the queue and receives messages from it synchronously. A point-to-point (PTP) product or application is built around the concept of message queues, senders, and receivers. Each message is addressed to a specific queue, and receiving clients extract messages from the queue(s) established to hold their messages. Queues retain all messages sent to them until the messages are consumed or until the messages expire.
     - Publish-Subscribe Messaging
       - When multiple applications need to receive the same messages, Publish-Subscribe Messaging is used. The central concept in a Publish-Subscribe messaging system is the Topic. Multiple Publishers may send messages to a Topic, and all Subscribers to that Topic receive all the messages sent to that Topic. This model is extremely useful when a group of applications want to notify each other of a particular occurrence. The point to note in Publish-Subscribe Messaging is that, there may be multiple Senders and multiple Receivers. Also in publish / subscribe (pub/sub) product or application, clients address messages to a topic. Publishers and subscribers are generally anonymous and may dynamically publish or subscribe to the content hierarchy. The system takes care of distributing the messages arriving from a topic's multiple publishers to its multiple subscribers. Topics retain messages only as long as it takes to distribute them to current subscribers. 
       - Pub/sub messaging has the following characteristics.
         - Each message may have multiple consumers.
         - Publishers and subscribers have a timing dependency. A client that subscribes to a topic can consume only messages published after the client has created a subscription, and the subscriber must continue to be active in order for it to consume messages. 
     - Request-Reply Messaging 
       - When an application sends a message and expects to receive a message in return, Request-Reply Messaging can be used. This is the standard synchronous object-messaging format. This messaging model is often defined as a subset of one of the other two models described above. JMS does not explicitly support Request-Reply Messaging, though it allows it in the context of the first two methods
4. Explain the three possibilities for managing client state on the server, with their usage in different middleware models (including RMI, CORBA, Socket servers and Web Service).
   - There are three possibilities for managing client state on the server:
   - The server keeps no state (case-1): Server never store client status in server. While client only browse information from server without leaving any data or stay signed in.
   - The server keeps state on a per-client basis (case-2): Server will keep status for every client. Socket server creates a new service object for each client connection.
   - The session keeps a single client (case-3): Here is a single server object that keeps one copy of server state. For instance, CORBA and RMI servers. 
   - The Web Service follows (cases-1, 2 or 3) depending on scope of implementation. The CORBA and RMI servers follow case (3): there is a single server object that keeps one copy of server state. If multiple clients gives, for example , `chdir` command, then the value of the state changes for every client. The socket server creates a new service object for each client connection and so follows case (2) because each `chdir` command is unique for each client connection.







# Week 11

1. What is mobile computing?

   - Mobile computing is considered with exploiting the connectedness of the devices that move around in the everyday physical world.

2. What is ubiquitous computing?

   - Ubiquitous computing, also known as pervasive computing, is about exploiting the increasing integration of computing devices with our everyday physical world. 

3. What is a volatile system? List the main types of changes that occur in a ubiquitous system.

   - Volatile systems are the distributed systems that have the volatility property. Volatility means certain changes are common rather than exceptional. Some relevant forms of volatility: Failures of devices and communication links, changes in the characteristic of communication such as bandwidth, the creation and destruction of logical communication relationships between components resident on the devices.
   - From the point of view of distributed systems, there is no essential difference between mobile and ubiquitous computing. Due to the ways of physical integration, volatility is a distributed systems property – certain changes are common rather than exceptional. 
   - The relevant forms of volatility include:
     - Failures of devices and communication links
     - Changes in the characteristics of communication such as bandwidth
     - The creation and destruction of associations – logical communication relationships –between software components resident on the devices. 

4. List the most common mobile operation systems

   - S40 Nokia, MeeGo and BlackBerry, Evolving from previously Windows CE, Windows Mobile, Palm OS, Symbian to nowadays iOS, Android, WebOS, Bada etc.

5. What are differences between the Java and Android API, and virtual machines?

   - There is no Java Virtual Machine in the Android platform. Java byte code is not executed. Instead Java classes are compiled into Dalvik executables and run on Dalvik, a specialized virtual machine (VM) designed specifically for Android. Unlike Java VMs, which are stack machines, the Dalvik VM is a register-based architecture.
   - Dalvik has some specific characteristics that differentiate it from other standard VMs:
     - The VM was designed to use less space.
     - The constant pool has been modified to use only 32-bit indexes to simplify the
       interpreter.
     - Standard Java bytecode executes 8-bit stack instructions. Local variables must be copied to or from the operand stack by separate instructions. Dalvik instead uses its own 16-bit instruction set that works directly on local variables. The local variable is commonly picked by a 4-bit 'virtual register' field. Because of the fact that the bytecode loaded by the Dalvik virtual machine is not Java bytecode, and of the specific way Dalvik load classes, it is not possible to load Java libraries packages as jar files, and even a specific logic must be used to load Android libraries (specifically the content of the underlying dex file must be copied in the application private internal storage area, before being able to be loaded.
   - Android only reuses the Java language syntax and semantics, but does not provide the full class libraries and APIs bundled with Java SE or ME 
   - Key differences lie in:
     - Virtual Machine: Android does not use JVM, but run on Dalvik VM, so not possible to load Java libraries packages as jar file.
     - System Properties: some mandatory properties defined with the JVM have no meaning or a different meaning on Android
     - Class library: Java ME classes, AWT or Swing are not supported by Dalvik. Instead it uses its own library built on a subset of the Apache Harmony Java implementation.

   ​






























