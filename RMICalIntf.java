//Interface  RMICalIntf.java

import java.rmi.*;
import java.rmi.server.*;
public interface RMICalIntf extends Remote  
{                            //Declaring the methods to be implemented
          double add(double a,double b) throws RemoteException;
          double sub(double a,double b) throws RemoteException;
          double mul(double a,double b) throws RemoteException;
          double div(double a,double b) throws RemoteException;
}
