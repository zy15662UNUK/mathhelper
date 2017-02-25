# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:14:44 2017

@author: James
"""

def fxy(x,y):
    return x+y
def predictorCorrectorMethod(x0,y0,x1,y1,x2,y2,h,upperlimit,lowerlimit):
   xlast=x0
   ylast=y0
   xsec_last=x1
   ysec_last=y1
   xcurrent=x2
   ycurrent=y2
   count=2
   while count<(upperlimit-lowerlimit)/h:
       count=count+1
       x=xcurrent+h
       ystar=ycurrent+h*(23*fxy(xcurrent,ycurrent)-16*fxy(xsec_last,ysec_last)+5*fxy(xlast,ylast))/12
       print('n= '+str(count)+', '+'x= '+str(x))
       print('n= '+str(count)+', '+'ystar= '+str(ystar))
       y=ycurrent+h*(5*fxy(x,ystar)+8*fxy(xcurrent,ycurrent)-fxy(xsec_last,ysec_last))/12
       print('n= '+str(count)+', '+'y= '+str(y))
       ylast=ysec_last
       xlast=xsec_last
       ysec_last=ycurrent
       xsec_last=xcurrent
       ycurrent=y
       xcurrent=x
       print('ylast= ',ylast)
       print('xlast= ',xlast)
       print('ysec_last= ',ysec_last)
       print('xsec_last= ',xsec_last)
       print('ycurrent= ',ycurrent)
       print('xcurrent= ',xcurrent)