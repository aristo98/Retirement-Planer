# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 23:49:03 2023

@author: arist
"""
import numpy as np
import matplotlib.pyplot as plt

class Retirement_Plan:
    def __init__(self,cap,anty,sav_rate,sav_interval,int_rate,comp,dur):
        '''
        Monthly       = 12 times annuity payment p.a.
        Quarterly     = 4 times annuity payment p.a.
        Half-yearly   = 2 times annuity payment p.a.
        Yearly        = 1 times annuity payment p.a.
        Continuosly   = continuos compounding
        ------------------------------------------
        Due (d)       = Annuity payment is made at the beginning of each period
        Immediate (i) = Annuity payment is made at the end of each period
        '''
        opt={"M":12,"Q":4,"H":2,"Y":1,"C":1000}
        self.para=(cap,anty,sav_rate,opt[sav_interval],int_rate,opt[comp],dur)
        '''
        start capital           = self.para[0] input: float(...)
        annuity(due/immediate)  = self.para[1] input:"due" or "immediate"
        savings rate            = self.para[2] input: float(...)
        savings intervall       = self.para[3] input: 1 or 2 or 4 or 12
        interest rate           = self.para[4] input: float(...)
        compounding             = self.para[5] input: 1 or 2 or 4 or 12 or 1000
        duration                = self.para[6] input: int(...)
        '''
    def formula(self,x,anty,indicat):
        if self.para[5]!=1000:
            if indicat:
                nom=(1+self.para[4]/self.para[5])**(self.para[5])
                denom=nom**(1/self.para[3])
                if anty=="immediate":
                    return self.para[0]*nom**(x)+self.para[2]*(nom**(x)-1)/(denom-1)
                else:
                    return self.para[0]*nom**(x)+self.para[2]*(nom**(x)-1)/(denom-1)*denom
            else:
                denom=(1+self.para[4]/self.para[5])
                nom=denom**(self.para[5])
                #if anty=="immediate":
                return self.para[0]*nom**(x)+self.para[2]*self.para[3]/self.para[5]*(nom**(x)-1)/(denom-1)*\
                    (1+(denom-1)*(1-np.heaviside(np.sign(self.para[2]),0)))
                #else:
                #    return self.para[1]*nom**(x)+self.para[0]*self.para[3]*self.para[4]/self.para[6]*(nom**(x)-1)/(denom-1)*\
                #        denom
        else:
            nom=np.exp(self.para[4])
            denom=nom**(1/self.para[3])
            if anty=="immediate":
                return self.para[0]*nom**(x)+self.para[2]*(nom**(x)-1)/(denom-1)
            else:
                return self.para[0]*nom**(x)+self.para[2]*(nom**(x)-1)/(denom-1)*denom
        
    def calculate_and_plot(self):
        if self.para[5]!=1000:
            self.time=np.linspace(0,self.para[6],self.para[6]*self.para[5]+1)
        else:
            self.time=np.linspace(0,self.para[6],self.para[6]*12+1)
        self.savings=np.array([int(self.formula(i,self.para[1],self.para[3]<=self.para[5])*100)/100 for i in self.time])/1000
        
        plt.rc('font', size=12)
        plt.plot(self.time,self.savings)
        plt.xlabel("Year")
        plt.ylabel("Savings x 1000 [\u20ac]")
        plt.grid()
        if np.sign(self.para[2])>0:
            plt.savefig("image.png",dpi=800,bbox_inches='tight')
        else:
            plt.savefig("image2.png",dpi=800,bbox_inches='tight')
        plt.close()
        
        if np.sign(self.para[2])>0:
            self.tb_displayed="Initial capital: "+"{:0,.2f}".format(self.savings[0]*1000)+" \u20ac\n"
            self.tb_displayed+="Total investment: "+"{:0,.2f}".format(self.para[3]*self.para[6]*np.abs(self.para[2]))+" \u20ac\n"
            self.tb_displayed+="Capital gain: "+"{:0,.2f}".format((self.savings[-1]-self.savings[0])*1000-self.para[3]*self.para[6]*np.abs(self.para[2]))+\
                " \u20ac\n\n"
            self.tb_displayed+="Capital after "+str(int(self.time[-1]))+" years: "+"{:0,.2f}".format(self.savings[-1]*1000)+" \u20ac\n"
            self.tb_displayed+="(Final capital=Initial capital+Total investment+Capital gain)"
        else:
            self.tb_displayed="Initial capital: "+"{:0,.2f}".format(self.savings[0]*1000)+" \u20ac\n"
            self.tb_displayed+="Total withdrawal: "+"{:0,.2f}".format(self.para[3]*self.para[6]*np.abs(self.para[2]))+" \u20ac\n"
            self.tb_displayed+="Capital gain: "+"{:0,.2f}".format((self.savings[-1]-self.savings[0])*1000+self.para[3]*self.para[6]*np.abs(self.para[2]))+\
                " \u20ac\n\n"
            self.tb_displayed+="Capital after "+str(int(self.time[-1]))+" years: "+"{:0,.2f}".format(self.savings[-1]*1000)+" \u20ac\n"
            self.tb_displayed+="(Final capital=Initial capital+Capital gain-Total withdrawal)"
