1. J2SDK是编程工具，不是API；Appletviewer.exe 就是用来解释执行java applet应用程序的,简单理解就是没有main函数的继承applet类的java类；能被Appletviewer成功运行的java class文件没有main()方法

2. final作为对象成员存在时，必须初始化；但是，如果不初始化，也可以在类的构造函数中初始。因为java允许将数据成员声明为final，却不赋初值。但是，blank finals必须在使用之前初始化，且必须在构造函数中初始化。

3. finalize()才是object方法，放在程序末尾，垃圾回收器运行到此程序时，执行此方法，通过重载此方法，可以在进行内存回收时实现其它功能，比如关闭文件等。finally()并不是。

4. 两个最基本的java回收算法：复制算法和标记清理算法
   - 复制算法：两个区域A和B，初始对象在A，继续存活的对象被转移到B。此为新生代最常用的算法
   - 标记清理：一块区域，标记要回收的对象，然后回收，一定会出现碎片，那么引出 3. 标记-整理算法：多了碎片整理，整理出更大的内存放更大的对象 

5. 两个概念：新生代和年老代
   - 新生代：初始对象，生命周期短
   - 永久代：长时间存在的对象
   - 整个java的垃圾回收是新生代和年老代的协作，这种叫做分代回收

6. 垃圾回收方式
   - Serial New收集器是针对新生代的收集器，采用的是复制算法 Parallel New（并行）收集器，新生代采用复制算法，老年代采用标记整理 
   - Parallel Scavenge（并行）收集器，针对新生代，采用复制收集算法 
   - Serial Old（串行）收集器，新生代采用复制，老年代采用标记整理 
   - Parallel Old（并行）收集器，针对老年代，标记整理 
   - CMS收集器，基于标记清理 
   - G1收集器：整体上是基于标记 整理 ，局部采用复制 
   - 综上：新生代基本采用复制算法，老年代采用标记整理算法。cms采用标记清理。

7. Java异常处理：

   - throws用于在方法上声明该方法不需要处理的异常类型,用在方法上后面跟异常类名 可以是多个异常类
   - throw用于抛出具体异常类的对象，用在方法内后面跟异常对象只能是一个异常类型实体
   - try块必须和catch块或和finally同在，不能单独存在，二者必须出现一个
   - finally块总会执行，不论是否有错误出现。但是若try语句块或会执行的catch语句块使用了JVM系统退出语句，finally块就不会被执行了。一般我们把关闭资源的代码放在finally里面，保证资源总是能关闭
   - final用于声明属性、方法、类。分别表示属性不可更改、方法不能被覆盖、类不能被继承

8. jdk1.8中，抽象类中的抽象方法和非抽象方法在不加修饰符的情况下，都是默认的default；jdk1.8之前，为protected

9. 空格的ASCII码值为32；数字0到9的ASCII码值分别为48到57；大写字母“A”到“Z”的ASCII码值分别为65到90；小写字母“a”到“z”的ASCII码值分别为97到到122。

10. 局部变量没有默认值；全局变量才有默认值

11. `ServerSocket(int port)` 是服务端绑定port端口，调`accept()`监听等待客户端连接，它返回一个连接队列中的一个socket。 

12. `Socket(InetAddress address , int port)`是创建客户端连接主机的socket流，其中InetAddress是用来记录主机的类，port指定端口。

13. **普通类也就是外部类**，通过 eclipse 的警告“Illegal modifier for the class Test; only public, abstract & final are permitted” 可知只能用 **public, abstract 和 final** 修饰。 内部类则可以用 修饰成员变量的修饰符修饰内部类，比如 **private, static, protected** 修饰。

14. 会话跟踪是一种灵活、轻便的机制，它使Web上的状态编程变为可能。

    HTTP是一种无状态协议，每当用户发出请求时，服务器就会做出响应，客户端与服务器之间的联系是离散的、非连续的。当用户在同一网站的多个页面之间转换时，根本无法确定是否是同一个客户，会话跟踪技术就可以解决这个问题。当一个客户在多个页面间切换时，服务器会保存该用户的信息。

    有四种方法可以实现会话跟踪技术：URL重写、隐藏表单域、Cookie、Session

    - 隐藏表单域：<input type="hidden">，非常适合步需要大量数据存储的会话应用。
    - URL 重写:URL 可以在后面附加参数，和服务器的请求一起发送，这些参数为名字/值对。
    - Cookie:一个 Cookie 是一个小的，已命名数据元素。服务器使用 SET-Cookie 头标将它作为 HTTP响应的一部分传送到客户端，客户端被请求保存 Cookie 值，在对同一服务器的后续请求使用一个Cookie 头标将之返回到服务器。与其它技术比较，Cookie 的一个优点是在浏览器会话结束后，甚至在客户端计算机重启后它仍可以保留其值
    - Session：使用 setAttribute(String str,Object obj)方法将对象捆绑到一个会话

15. 数组命名时名称与[]可以随意排列，但声明的二维数组中第一个中括号中必须要有值，它代表的是在该二维数组中有多少个一维数组。

16. 加载驱动方法

    - `Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");`
    - `DriverManager.registerDriver(new com.mysql.jdbc.Driver());`
    - `System.setProperty("jdbc.drivers", "com.mysql.jdbc.Driver");`

17. java的访问权限有public、protected、private和default的，default不能修饰变量；普通变量不能用abstract修饰，abstract一般修饰方法和类；被定义为abstract的类需要被子类继承，但是被修饰为final的类是不能被继承和改写的

18. ​