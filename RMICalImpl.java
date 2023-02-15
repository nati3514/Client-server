//Implementation RMICalImpl.java

import java.rmi.*;
import java.io.*;
import java.rmi.server.*;

public class RMICalImpl extends UnicastRemoteObject implements RMICalIntf
{                                     //Defining the methods declared in the interface
RMICalImpl() throws RemoteException
{
}
          public double add(double a, double b)throws RemoteException
{
return(a+b);
             }
          public double sub(double a,double b)throws RemoteException
{
                   return(a-b);
                   }
          public double mul(double a,double b)throws RemoteException
{
                   return(a*b);
                   }    
          public double div(double a,double b)throws RemoteException
{
                   return(a/b);
                   } 
}
