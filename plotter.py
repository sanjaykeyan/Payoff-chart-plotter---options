import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor, TextBox
import pandas as pd

def get_chart(net_PL,spot,title=""):
    x=spot
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(x, net_PL, label='Payoff')
    ax.set_xlabel('Stock Price')
    ax.set_ylabel('Profit/Loss')
    ax.set_title(title)
    ax.legend()
    ax.fill_between(x, net_PL, 0, where=(net_PL > 0), interpolate=True, color='green', alpha=0.5)
    cursor = Cursor(ax, useblit=True, color='red', linewidth=1)

    # define function to display profit/loss as popup
    def display_popup(event):
        if event.inaxes:
            x, y = event.xdata, event.ydata
            popup_text = f'Profit/Loss at {x:.2f}: {y:.2f}'
            ax.set_title(title + '\n' + popup_text)
            fig.canvas.draw_idle()

    # define function to remove popup when mouse is not hovering over graph
    def remove_popup(event):
        if event.inaxes:
            ax.set_title(title)
            fig.canvas.draw_idle()

    # attach the functions to mouse movement events
    fig.canvas.mpl_connect('motion_notify_event', display_popup)
    fig.canvas.mpl_connect('axes_leave_event', remove_popup)
    plt.show()
   

def PE_buy(strike,spot,prem,qty):
    PL = qty*(np.maximum(0,strike-spot) - prem)
    return PL
def PE_sell(strike,spot,prem,qty):
    PL = qty*(-(np.maximum(0,strike-spot)) + prem)
    return PL
def CE_buy(strike,spot,prem,qty):
    PL = qty*(np.maximum(0,spot-strike) - prem)
    return PL
def CE_sell(strike,spot,prem,qty):
    PL= qty*(-(np.maximum(0,spot-strike)) + prem)
    return PL

def BullCallSpread():
    ATM_strike = int(input("Enter ATM_strike : "))
    ATM_prem = float(input("Enter Premium : "))
    qty1=int(input("Enter Quantity : "))
    OTM_strike = int(input("Enter OTM_strike : "))
    OTM_prem = float(input(("Enter Premium : ")))
    qty2=int(input("Enter Quantity : "))

    spot=np.arange(ATM_strike-400,OTM_strike+400,50)
    PL1=CE_buy(ATM_strike,spot,ATM_prem,qty1)
    PL2=CE_sell(OTM_strike,spot,OTM_prem,qty2)
    net_PL = PL1+PL2
    get_chart(net_PL,spot)

def BullPutSpread():
    OTM_PE = int(input("Enter OTM_strike : "))
    OTM_PE_prem = float(input("Enter Premium : "))
    qty1=int(input("Enter Quantity : "))
    ITM_PE = int(input("Enter ITM_strike : "))
    ITM_PE_prem = float(input(("Enter Premium : ")))
    qty2=int(input("Enter Quantity : "))

    spot=np.arange(min(OTM_PE,ITM_PE)-700,max(OTM_PE,ITM_PE)+700,50)
    PL1=PE_buy(OTM_PE,spot,OTM_PE_prem,qty1)
    PL2=PE_sell(ITM_PE,spot,ITM_PE_prem,qty2)
    net_PL = PL1+PL2
    get_chart(net_PL,spot)

def short_straddle():
    ATM_CE = int(input("Enter ATM CE_strike : "))
    CE_prem = float(input("Enter Premium : "))
    qty1=int(input("Enter Quantity : "))
    ATM_PE = float(input("Enter ATM PE_strike : "))
    PE_prem = int(input(("Enter Premium : ")))
    qty2=int(input("Enter Quantity : "))

    spot=np.arange(ATM_CE-400,ATM_PE+400,50)
    PL1=CE_sell(ATM_CE,spot,CE_prem,qty1)
    PL2=PE_sell(ATM_PE,spot,PE_prem,qty2)
    net_PL = PL1+PL2
    get_chart(net_PL,spot)

def long_straddle():
    ATM_CE = int(input("Enter ATM CE_strike : "))
    CE_prem = float(input("Enter Premium : "))
    qty1=int(input("Enter Quantity : "))
    ATM_PE = float(input("Enter ATM PE_strike : "))
    PE_prem = int(input(("Enter Premium : ")))
    qty2=int(input("Enter Quantity : "))

    spot=np.arange(ATM_CE-400,ATM_PE+400,50)
    PL1=CE_buy(ATM_CE,spot,CE_prem,qty1)
    PL2=PE_buy(ATM_PE,spot,PE_prem,qty2)
    net_PL = PL1+PL2
    get_chart(net_PL,spot)

def long_strangle():
    OTM_CE = int(input("Enter OTM CE_strike : "))
    CE_prem = float(input("Enter Premium : "))
    qty1=int(input("Enter Quantity : "))
    OTM_PE = float(input("Enter OTM PE_strike : "))
    PE_prem = int(input(("Enter Premium : ")))
    qty2=int(input("Enter Quantity : "))

    spot=np.arange(min(OTM_CE,OTM_PE)-700,max(OTM_CE,OTM_PE)+700,50)
    PL1=CE_buy(OTM_CE,spot,CE_prem,qty1)
    PL2=PE_buy(OTM_PE,spot,PE_prem,qty2)
    net_PL = PL1+PL2
    get_chart(net_PL,spot)
    
def short_strangle():
    OTM_CE = int(input("Enter OTM CE_strike : "))
    CE_prem = float(input("Enter Premium : "))
    qty1=int(input("Enter Quantity : "))
    OTM_PE = float(input("Enter OTM PE_strike : "))
    PE_prem = int(input(("Enter Premium : ")))
    qty2=int(input("Enter Quantity : "))

    spot=np.arange(min(OTM_CE,OTM_PE)-700,max(OTM_CE,OTM_PE)+700,50)
    PL1=CE_sell(OTM_CE,spot,CE_prem,qty1)
    PL2=PE_sell(OTM_PE,spot,PE_prem,qty2)
    net_PL = PL1+PL2
    get_chart(net_PL,spot)

def custom(n):
    dict = {}
    nifty = int(input("Enter Current NIFTY Value : "))
    spot = np.arange(nifty-2000,nifty+2000,50)
    PL = np.array
    for i in range(0,n):
        SP = int(input("Enter Strike Price : "))
        type = int(input("CE(1)/PE(2) : "))
        pos = int(input("Buy(1) / Sell(-1) : "))
        prem = float(input("Enter Premium : "))
        qty = int(input("Enter Quantity : "))
        key = (type,pos,SP)
        val = [prem,qty]
        dict[key] = val

    #intialise PL 
    keys = list(dict.keys())
    key = keys[0]
    if key[0]==1: #Call Option
        SP = key[2]
        prem = dict[key][0]
        qty = dict[key][1]
        if key[1]==-1: #Sell
            PL=CE_sell(SP,spot,prem,qty)
        if key[1]==1:
            PL=CE_buy(SP,spot,prem,qty)

    else:  # Put Option
        SP = key[2]
        prem = dict[key][0]
        qty = dict[key][1]
        if key[1]==-1: #Sell
            PL=PE_sell(SP,spot,prem,qty)
        if key[1]==1:
            PL =PE_buy(SP,spot,prem,qty)
    del dict[key]

    for key in dict:
        if key[0]==1: #Call Option
            SP = key[2]
            prem = dict[key][0]
            qty = dict[key][1]
            if key[1]==-1: #Sell
                PL =PL + CE_sell(SP,spot,prem,qty)
            if key[1]==1:
                PL = PL + CE_buy(SP,spot,prem,qty)

        else:
            SP = key[2]
            prem = dict[key][0]
            qty = dict[key][1]
            if key[1]==-1: #Sell
                PL =PL + PE_sell(SP,spot,prem,qty)
            if key[1]==1:
                PL = PL + PE_buy(SP,spot,prem,qty)

    get_chart(PL,spot)

print("**************************PAYOFF DIAGRAM PLOTTER**************************")
print("1. Custom Strategy \n2. Bull Call Spread \n3. Bull Put Spread \n4.Short Straddle\n5. Long Straddle\n6. Short Strangle \n7. Long Strangle ")
print("\n\n")
choice = int(input("Enter your choice : "))

if choice == 1:
    n=int(input("Enter no of trades involved : "))
    custom(n)
elif choice ==2:
    print("\n\n")
    print("**************************BULL CALL SPREAD**************************")
    BullCallSpread()
elif choice==3:
    print("\n\n")
    print("**************************BULL PUT SPREAD**************************")
    BullPutSpread()
elif choice == 4:
    print("\n\n")
    print("**************************SHORT STRADDLE**************************")
    short_straddle()
elif choice == 5:
    print("\n\n")
    print("**************************LONG STRADDLE**************************")
    long_straddle()
elif choice == 6:
    print("\n\n")
    print("**************************SHORT STRANGLE**************************")
    short_strangle()
elif choice == 7:
    print("\n\n")
    print("**************************LONG STRANGLE**************************")
    long_strangle()





    
