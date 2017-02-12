from SupportingFunctions import *

# IMR 18650, data from : https://www.imrbatteries.com/efest-purple-18650-3500mah-20a-flat-top-battery/

V_lvl = 3.7  # Volts per cell
A_cap = 10.0 # Amps per cell
Ah_cap= 3.5  # Ah per cell
D_cell=18.25 # mm diameter
L_cell=65.25 # mm length
Wt = 0.047   # kg per cell
Cost = 9.0   # $ per cell

def Battery(DCPowerLimits,Vs):

    global CellsPerBattery
    global BatteriesPerPack
    global CellsPerPack

    INCRMT_A = 0
    INCRMT_B = 0
    VoltsOut = 0

    print("----Battery----")

    minAmps = (DCPowerLimits[0]*1000)/Vs
    maxAmps = (DCPowerLimits[1]*1000)/Vs 

    while (Vs>VoltsOut) or (maxAmps>AmpsOut):

        CellsPerBattery = int(Vs/V_lvl) +INCRMT_A                   # Number of Series cells in 1 Battery
        BatteriesPerPack = int(maxAmps/A_cap) +INCRMT_B             # Number of Parallel Batteries
        CellsPerPack = CellsPerBattery * BatteriesPerPack           # (Number of Cells/Battery)*(Number of Batteries)

        VoltsOut = V_lvl*CellsPerBattery
        AmpsOut  = A_cap*BatteriesPerPack
        PwrOut   = VoltsOut*AmpsOut/1000 # kW

        if Vs>VoltsOut:
            INCRMT_A += 1
        if maxAmps>AmpsOut:
            INCRMT_B += 1

    Moolah = CellsPerPack*Cost
    
    if CellsPerPack > 50: # Quantity savings
        Moolah = Moolah-Moolah*(0.02)
        if CellsPerPack >100:
            Moolah = Moolah-Moolah*(0.05)
            if CellsPerPack > 200 and CellsPerPack < 10000 :
                Moolah = Moolah-Moolah*(0.08)
                if CellsPerPack > 10000 :
                    print("YO DUDE........ TOO MANY BATTERIES!")

    
    Ah = Ah_cap*BatteriesPerPack
    kWh= (VoltsOut*Ah)/1000 # V*A*h = Wh /1000 = kWh
    Kilograms= CellsPerPack*Wt # Cells/Pack * Weight/Cell = Weight/Pack
    TimeLimits=[60*Ah/maxAmps,60*Ah/minAmps] # 60min/hr * Ah / Amps
    
    print("Cells Per Battery =",double(CellsPerBattery))
    print("Batteries Per Pack=",double(BatteriesPerPack))
    print("Cells Per Pack    =",double(CellsPerPack))
    print("Cost Per Pack     =",double(Moolah),'$')
    print("Weight Per Pack   =",double(Kilograms),'kg')
    print("kWh Per Pack      =",double(kWh),'kWh')
    print(' ')
    print("Voltage Output    =",double(VoltsOut),'V')
    print("Max Amps Output   =",double(AmpsOut),'A')
    print("Max Power Output  =",double(PwrOut),'kW')
    print("Time Range        =",'['+double(TimeLimits[0]),',',double(TimeLimits[1])+']','mins')

    print("-------------")

    return Moolah

def Sizing():

    print("----Battery Sizing-----")
    
    global CellsPerBattery
    global BatteriesPerPack
    global CellsPerPack

    PackWallThickness = 20 #mm

    PackWidth = CellsPerBattery*D_cell  + PackWallThickness*2 # rows (mm)
    PackLength= BatteriesPerPack*D_cell + PackWallThickness*2 # columns (mm)
    PackDepth = L_cell                  + PackWallThickness*2 # depth (flat pack)

    print('Pack Width =',PackWidth,'mm')
    print('Pack Length =',PackLength,'mm')
    print('Pack Depth =',PackDepth,'mm')

    print("-----------------------")
    
