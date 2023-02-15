
//Client  side   RMICalClient.java

import javax.swing.*;
import java.awt.*;
import java.rmi.*;
import java.awt.event.*;
import java.io.*;
public class RMICalClient extends JFrame implements ActionListener
{
          double n1 = 0.0;
          double  d1;
double n2 = 0.0;
          JButton jb[] = new JButton[21];
          JTextField tf;
          Container con;
          int button,i;
          String str;
          String num="";
          JPanel tp,bp;                            //declaring 2 panels for textfield and buttons
          public RMICalClient()
{
                   setTitle("calculator");
                   tp = new JPanel();
                   bp = new JPanel();
                   tf = new JTextField(22);
                   tf.setEditable(false);
                   con = getContentPane();
                   bp.setLayout(new GridLayout(5,4));
                   tp.add(tf);
                   con.add(tp,"North");                  //placing the textfield in the north
                   for(int i=0;i<10;i++)                    //inserting and numbering buttons
{
                        jb[i] = new JButton(""+i);
}
                   jb[10] = new JButton("+");
                   jb[11] = new JButton("-");
                   jb[12] = new JButton("*");
                   jb[13] = new JButton("/");
                   jb[14] = new JButton("clear");
                   jb[15] = new JButton(".");
                   jb[16] = new JButton("=");
                   for(int i = 0;i<17;i++)
{
                             jb[i].addActionListener(this);
                             bp.add(jb[i]);
                             }
                   con.add(bp,"Center"); //placing the panel with the buttons in the center
                   setDefaultCloseOperation(EXIT_ON_CLOSE);
                   }     
public void actionPerformed(ActionEvent ae)
{  
str = ae.getActionCommand();             //get the text on the button
                   System.out.println(str);
                   for(int i=0;i<10;i++)
{
                          if(ae.getSource()==jb[i])
{
num = num+str;     //if the button clicked is a number,
                                      tf.setText(num);     
                             }
                   }
                   if((ae.getSource())==jb[15])                 
{
num = num+str;                         //concatenate it to num
                             tf.setText(num);
                             }
                   for(int i=10;i<14;i++)
{
                             if(ae.getSource()==jb[i])            //if the button is an operator
{
button = i-9;          
                                      if(num!="")             //obtain the first operand
{
                                      tf.setText("");
                                      n1 = Double.parseDouble(num);    //convert string in to
                                       num="";                           
                                      }
else
{
                                                          tf.setText("");
                                                }
}
                             }
                             if(ae.getSource()==jb[16])         
{
                                      if(!(tf.getText().equals("")))
{
                                                tf.setText("");
n2 = Double.parseDouble(num);//store 2nd operand
//in n2
                                                num = "";
                                                          try
{
                                                          String url = "rmi://localhost/calserver";
                                                          RMICalIntf a =(RMICalIntf) Naming.lookup(url);
                                                          switch(button)
{
                                                                   case 1:
                                                                                      d1 = a.add(n1,n2);
                                                                                      break;  
                                                                             case 2:
                                                                                      d1 = a.sub(n1,n2);
                                                                                      break;
                                                                   case 3:
                                                                                      d1 = a.mul(n1,n2);
                                                                                      break;
                                                                   case 4:
                                                                                      d1 = a.div(n1,n2);
                                                                                      break;
                                                                             default:
                                                                                      d1 = 0.0;
                                                                   }
str = String.valueOf(d1);          //convert the //value to string
                                                          tf.setText(str);       //print the value
                                                                   }
catch(Exception e){}
                                                          }
else
{
                                      tf.setText("");
                                                }
                             }
                             if(ae.getSource()==jb[14]) 
{
                                                tf.setText("");
                                                num = "";
                                                n1=0.0;
                                                n2=0.0;
                                                button=0;
                                      }
                             }
public static void main(String args[])
{
                   JFrame f = new RMICalClient();
                   f.setSize(400,400);
                   f.setVisible(true);
                   }
}

