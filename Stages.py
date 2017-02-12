import Fans as f
import Motor as m
import Inverter as i
import Battery as b

Vs = 230 # Standard System Voltage, selected because: minimum sparkover voltage is 327 V

f.GetPerformance()
PowerLimits, RPMLimits = m.Motor()
DCPowerLimits          = i.Inverter(PowerLimits, RPMLimits, Vs)
PackCost               = b.Battery(DCPowerLimits,Vs)
print(' ')
motorDiameter,motorL   = m.Sizing(PowerLimits[1],Vs)
inverterVolume         = i.Sizing(motorDiameter,motorL)
b.Sizing()
