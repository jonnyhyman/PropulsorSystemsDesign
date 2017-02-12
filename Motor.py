import Fans as f
import numpy as n
from SupportingFunctions import *

MotorEfficiency = 0.95 # Important for heat calculations

def Motor():

    print("----Motor----")

    # Find max kW of all fans

    maxPower=0
    for i in range(len(f.Ns)):
        if f.Ns[i][1] > maxPower:
            maxPower=f.Ns[i][1]

    # Find min kW of all fans

    minPower=10000000000
    for i in range(len(f.Ns)):
        if f.Ns[i][1] < minPower:
            minPower=f.Ns[i][1]


    print("Power Range =",'['+double(minPower),',',double(maxPower)+']','kW')

    # Find max RPM of all fans

    maxRPM=0
    for i in range(len(f.Ns)):
        if f.Ns[i][4] > maxRPM:
            maxRPM=f.Ns[i][4]

    # Find min RPM of all fans

    minRPM=10000000000
    for i in range(len(f.Ns)):
        if f.Ns[i][4] < minRPM:
            minRPM=f.Ns[i][4]

    print("RPM Range   =",'['+double(minRPM),',',double(maxRPM)+']','RPM')


    minTorque=(maxPower*1000)/(maxRPM*(n.pi/30)) #  Newton Meters = (Watts)/(rad/s) 
    maxTorque=(maxPower*1000)/(minRPM*(n.pi/30)) #  Max torque is at minimum rpm

    print("Torque Range=",'['+double(minTorque),',',double(maxTorque)+']','Nm')

    print(' ')
    print('Design Limits:')

    DesignFactor = 0.5 

    minPower=minPower*DesignFactor
    maxPower=maxPower*(1+DesignFactor)

    minRPM=minRPM*DesignFactor
    maxRPM=maxRPM*(1+DesignFactor)

    minTorque=minTorque*DesignFactor
    maxTorque=maxTorque*(1+DesignFactor)

    minHeat = minPower*(1-MotorEfficiency)*1000 # Watts
    maxHeat = maxPower*(1-MotorEfficiency)*1000

    print("Power Range =",'['+double(minPower),',',double(maxPower)+']','kW')
    print("RPM Range   =",'['+double(minRPM),',',double(maxRPM)+']','RPM')
    print("Torque Range=",'['+double(minTorque),',',double(maxTorque)+']','Nm')
    print("*Heat Range =",'['+double(minHeat),',',double(maxHeat)+']','W')

    print("-------------")

    return ([minPower,maxPower],[minRPM,maxRPM])


def Sizing(kW,Vs):

    print("----Motor Sizing----")

    NumberOfSlots=48  
    WindingsPerSlot=6
    NumberOfPhases=3
    ConcetricSpacing=2.5  # mm
    MotorCaseThickness=0.010 # m
    AmpsPerPhase = (kW*1000/Vs)/NumberOfPhases # (kW->(W))/V = A

    WireDiameter,AWG = AWG_Diameter(AmpsPerPhase) # Slot Width
    Sw = WireDiameter

    print("Power Limit    =",kW,"kW")
    print("Voltage Supply =",Vs,"V")    

    print("Amps Per Phase =",double(AmpsPerPhase),"A")
    print("AWG            =",AWG,"")

    Wa = (n.pi*(WireDiameter/2)**2) # pi*r^2

    Sa = Wa*WindingsPerSlot
    Sh = Sa/Sw

    print("Slot Area      =",double(Sa),"mm^2")
    print("Slot Height    =",double(Sh),"mm")
    print("Slot Width     =",double(Sw),"mm")

    Ic = (Sw + ConcetricSpacing)*NumberOfSlots ## Inner circumference
    Id = Ic/n.pi                               ## Inner diameter
    Odi = Sh                                   ## Outer diameter increment

    Sd = Id+Odi                    ## Motor stator diameter (mm)

    print("Stator Diameter=",double(Sd),"mm")

    TeslaMotorVolume = n.pi*((0.2286/2)**2)*(0.2286) # m^3 = pi*r^2*h = V
    TeslaMotorKW     = 310 # kW
    TeslaKWPerVolume = TeslaMotorKW/TeslaMotorVolume # kW/m^3

    MotorVolume = (1/TeslaKWPerVolume)*kW  # note this is an outrageously loose approximation :)

    MotorDiameter = Sd/1000 + MotorCaseThickness # meters
    MotorArea = n.pi*(MotorDiameter/2)**2 # m^2
    MotorLength = MotorVolume/MotorArea
    
    print('Motor Diameter =',double(MotorDiameter*1000),'mm')
    print('*Motor Length  =',double(MotorLength*1000),'mm')

    print("--------------------")

    return MotorDiameter,MotorLength # Output meters
