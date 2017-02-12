from SupportingFunctions import *

# All runs use last exitvel except N1 (static) ----&---- 504m/1653ft , ISA

N1 = [125,                      # Thrust(N)
      3.65,                     # Power(kW)
      0.86177706194178263E-01,  # ExitVelocity(Mach) # 0.086
      0.2,                      # Radius(m)
      2500,                     # RPM
      14,           	        # Blades
      99.8,                     # Power Efficiency
      108.91183314148280,       # Wake Angular Velocity (rad/s)
      0.12566370614359174,      # Wake Axial Area (m^2)
      3.6639689109445497,       # Volumetric Flow Rate (m^3/s)
      4.2871442559190482        # Mass Flow Rate (kg/s)
      ]

N2 = [50,
      1.65,
      0.74141392429965688E-01, # 0.074
      0.147,
      5000,
      12,
      88.1,
      111.76041681658774,
      0.67910705044350095E-01,
      1.7035150045885317,
      1.9932523294557400
      ]

N3 = [94.00,
      2.94,
      0.79539312089252273E-01, # 0.08
      0.187,
      7600,
      4,
      80.2,
      65.780548634913302,
      0.11054688256999130,
      2.9800875151730351,
      3.4869469101244510
      ]

N4 = [94.00,
      3.05,
      0.77458461924095584E-01, #  0.08
      0.193,
      6550,
      5,
      83.3,
      67.274338668248149,
      0.11697143740873875,
      3.0654601977734801,
      3.5868399536297093
      ]

N5 = N4 # Identically

N6 = N5 # Identically

Ns = [N1,N2,N3,N4,N5,N6]

Total_Thrust =0
Total_Power  =0

def GetPerformance():

    global Total_Thrust
    global Total_Power

    print("----Fans----")

    for n in range(len(Ns)):
        Total_Thrust += Ns[n][0]
        Total_Power  += Ns[n][1]

    Total_Effectiveness = Total_Thrust/Total_Power

    print("Total Thrust       =",Total_Thrust,'N')
    print("Total Power        =",Total_Power,'kW')
    print("Total Effectiveness=",double(Total_Effectiveness),'N/kW')

    print("------------")

#------------------------------------------------
#   Check for physics violations (conservations)
#------------------------------------------------

print(' ')

def MassConservation(mdot1,mdot2): # 1,2 = upstream, downstream
    print('    ','mdotin =',mdot1,'mdotout =',mdot2)
    if mdot1 > mdot2:
        return True # Mass is conserved
    else:
        return False # Mass is not conserved

def MomentumConservation(p1,p2): # 1,2 = upstream, downstream
    print('    ','inp =',p1,'outp =',p2)
    if p1 > p2:
        return True # Mass is conserved
    else:
        return False # Mass is not conserved

def CheckConservations():

    def MachToMeters(mach):
        return mach*340.29 # mach 1 = 340.29 m/s

    # 0 and 1 at 1 by definition are correct
    
    # 1 and 2 at 2

    Afrac_1_2 = N2[8]/N1[8]
    print('    ','Afrac_1_2 =',Afrac_1_2)
    Mdot1=Afrac_1_2*N1[10]
    Mdot2=N2[10]

    print(' ')
    
    if MassConservation(Mdot1,Mdot2):
        print(":) For 1 and 2, Mass Conserved")
    else:
        print(":( For 1 and 2 Mass NOT Conserved")

    print(' ')

    Vdot1=Afrac_1_2*N1[9]
    Vdot2=N2[9]

    rho1 = Mdot1/Vdot1
    rho2 = Mdot2/Vdot2

    v1=MachToMeters(N1[3])
    v2=MachToMeters(N2[3])

    p1 = rho1*(v1**2)*N1[8]
    p2 = rho2*(v2**2)*N2[8]

    if MomentumConservation(p1,p2):
        print(":) For 1 and 2, Momentum Conserved")
    else:
        print(":( For 1 and 2, Momentum NOT Conserved")

    print(' ')

    # 1, 2 and 3 at 3

    Afrac_1_3 = N3[8]/N1[8]

    print('    ','Afrac_1_3 ',Afrac_1_3)

    Mdot1=Afrac_1_3*N1[10]
    Mdot3=N3[10]

    print(' ')
    
    if MassConservation(Mdot1,Mdot3):
        print(":) For 1, 2 and 3, Mass Conserved")
    else:
        print(":( For 1, 2 and 3, Mass NOT Conserved")

    print(' ')

    Vdot1=Afrac_1_3*N1[9]
    Vdot3=N3[9]

    rho1 = Mdot1/Vdot1
    rho3 = Mdot3/Vdot3

    v1=MachToMeters(N1[3])
    v3=MachToMeters(N3[3])

    p1 = rho1*(v1**2)*N1[8]
    p3 = rho3*(v3**2)*N3[8]

    if MomentumConservation(p1,p3):
        print(":) For 1, 2 and 3, Momentum Conserved")
    else:
        print(":( For 1, 2 and 3, Momentum NOT Conserved")

    print(' ')

    # 1, 2, 3 and 4 at 4

    Afrac_1_4 = N4[8]/N1[8]

    print('    ','Afrac_1_4 ',Afrac_1_4)

    Mdot1=Afrac_1_4*N1[10]
    Mdot4=N4[10]
    
    if MassConservation(Mdot1,Mdot4):
        print(":) For 1, 2, 3 and 4, Mass Conserved")
    else:
        print(":( For 1, 2, 3 and 4, Mass NOT Conserved")

    print(' ')

    Vdot1=Afrac_1_4*N1[9]
    Vdot4=N4[9]

    rho1 = Mdot1/Vdot1
    rho4 = Mdot4/Vdot4

    v1=MachToMeters(N1[3])
    v4=MachToMeters(N4[3])

    p1 = rho1*(v1**2)*N1[8]
    p4 = rho4*(v4**2)*N4[8]

    if MomentumConservation(p1,p4):
        print(":) For 1, 2, 3 and 4, Momentum Conserved")
    else:
        print(":( For 1, 2, 3 and 4, Momentum NOT Conserved")

    print(' ')

#CheckConservations()
        
    
