//Server side   RMICalServer.java

import java.rmi.*;
public class RMICalServer
{
          public static void main(String args[])
{
                   try
{                            //creating implementation object
RMICalImpl si = new RMICalImpl();
                             Naming.rebind("calserver",si);
                             }
catch(Exception e){}
                   }
          }



