# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:24:47 2017

@author: James
"""
def fxy(x,y):
    return y-x*x+1

def RK4_first_order_method(t0,y0,h,upperlimit,lowerlimit):
    t=float(t0)
    y=float(y0)
    count=0
    print('the t'+str(count)+' is '+str(t))
    print('the y'+str(count)+' is '+str(y))
    k1=0
    k2=0
    k3=0
    k4=0
    while count<(upperlimit-lowerlimit)/h:
        count=count+1
        k1=h*fxy(t,y)
        k2=h*fxy(t+0.5*h,y+0.5*k1)
        k3=h*fxy(t+0.5*h,y+0.5*k2)
        k4=h*fxy(t+0.5*h,y+k3)
        print('k1= ',k1)
        print('k2= ',k2)
        print('k3= ',k3)
        print('k4= ',k4)
        change=(k1+2*k2+2*k3+k4)/6
        y=y+change
        t=t+h
        print('the change'+str(count)+' is '+str(change))
        print('the t'+str(count)+' '+' is '+str(t))
        print('the y'+str(count)+' '+' is '+str(y))
        
        
        
        
    