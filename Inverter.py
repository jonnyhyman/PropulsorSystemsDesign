from SupportingFunctions import *
import numpy as n

Nph = 3 # Number of Phases
Npo = 4 # Number of Poles

InverterEfficiency = 0.95 # Important for heat calculations

def Inverter(PowerLimits, RPMLimits,Vs):
    print("----Inverter----")

    minFrequency = ((RPMLimits[0])*Npo)/120 # 120 comes from Hertz -> RPM
    maxFrequency = ((RPMLimits[1])*Npo)/120

    print("Freq Range    =",'['+double(minFrequency),',',double(maxFrequency)+']','Hz')

    minAmps = (PowerLimits[0]*1000)/Vs # Total DC Amps To Convert
    maxAmps = (PowerLimits[1]*1000)/Vs
    
    print("Amps Range    =",'['+double(minAmps),',',double(maxAmps)+']','A')

    maxAmpsPerPhase = maxAmps / Nph

    print("Amps Per Phase=",double(maxAmpsPerPhase),'A')

    minDCPower = minAmps*Vs/1000 # kW
    maxDCPower = maxAmps*Vs/1000

    DCPowerLimits = [minDCPower,maxDCPower]

    print("DC Power Range=",'['+double(minDCPower),',',double(maxDCPower)+']','kW')

    minHeat = minDCPower*(1-InverterEfficiency)*1000  # Watts
    maxHeat = maxDCPower*(1-InverterEfficiency)*1000

    print("*Heat Range   =",'['+double(minHeat),',',double(maxHeat)+']','W')
        
    print("-------------")

    return DCPowerLimits

def Sizing(MotorDiameter,MotorLength):

    print("----Inverter Sizing----")

    PylonLength    =  MotorLength*2 # 2 motors per pylon
    PylonWidth     = (MotorDiameter/2)

    ShroudDiameter = 0.440 # meters
    PylonHeight    = ShroudDiameter/2 - MotorDiameter/2

    PylonVolume    = (n.pi*(PylonLength*1000/2)*(PylonWidth*1000/2))*(PylonHeight*1000) # mm^3

     # Pylons are extruded ellipses

    print('Pylon Height  =',double(PylonHeight*1000),'mm')
    print('Pylon Width   =',double(PylonWidth*1000),'mm')
    print('Pylon Length  =',double(PylonLength*1000),'mm')
    print('Pylon Volume  =',double(PylonVolume),'mm^3')

    print("-----------------------")
    
    return PylonVolume
