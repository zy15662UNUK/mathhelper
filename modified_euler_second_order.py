# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 21:25:07 2017

@author: James
"""
def zdesh(x,y):
    return x*x-9*y
    
def modi_euler(x0,y0,z0,h,upperlimit,lowerlimit):
    print("ATTENTION! z==y' ")
    x=float(x0)
    y=float(y0)
    z=float(z0)
    count=0
    print('the x'+str(count)+' is '+str(x))
    print('the y'+str(count)+' is '+str(y))
    k1y=0
    k2y=0
    k1z=0
    k2z=0
    while count<(upperlimit-lowerlimit)/h:
         count=count+1
         tempz=z
         tempy=y
         k1y=h*tempz
         k2y=h*(tempz+h*zdesh(x,tempy))
         k1z=h*zdesh(x,tempy)
         k2z=h*zdesh(x+h,tempy+h*tempz)
         changey=0.5*(k1y+k2y)
         changez=0.5*(k1z+k2z)
         y=y+changey
         z=z+changez
         x=x+h
         print('the change of y'+str(count)+' is '+str(changey))
         print('the change of z'+str(count)+' is '+str(changez))
         print('the x'+str(count)+' '+' is '+str(x))
         print('the y'+str(count)+' '+' is '+str(y))
         print('the z'+str(count)+' '+' is '+str(z))
         
        
         