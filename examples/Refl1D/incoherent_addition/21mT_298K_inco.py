from refl1d.names import *
from numpy import *
# FIT USING REFL1D 0.6.19

# === Instrument specific header ===
from refl1d.ncnrdata import NCNRData, Monochromatic
class PBR(NCNRData, Monochromatic):
    """
    Instrument definition for NCNR PBR reflectometer.
    """
    instrument = "PBR"
    radiation = "neutron"
    wavelength = 4.75
    dLoL = 0.015
    d_s1 = 1835
    d_s2 = 343
    d_s3 = 380
    d_s4 = 1015   
# DEFINE BEAM PARAMETERS
FW = 0.057# FWHM of rocking curve in degrees
#FW = 0.04 # FWHM of rocking curve in degrees
d1 = 1835
d2 = 343
s1 = 1    # slit 1 value in mm
s2 = 1     # slit 2 value in mm
w = 10     # sample width in mm
broad = FW - degrees(0.5*(s1+s2)/(d1-d2))  # sample broadening value in degrees
instrument = PBR(slits_at_Tlo=(s1,s2),sample_width=w,sample_broadening=broad)
# LOAD DATA AND CREATE A PROBE
probe = instrument.load_magnetic('june_298K_21mT.reflA', back_reflectivity=False)

probe.xs[1],probe.xs[2] = None, None
#probe.oversample(n=50)

# === Constants ===
px = 0.28
Co_rho = 2.265
Co_irho = 0.009
Cr_rho = 3.027
# === Priming ===
# offsets
I0 = 1.08159559879009# normalization factor
th = 0.0110722577250943# theta offset in degrees
# divide sample into 3 domains
ratA = 0.180623644953364 # parallel, postive
ratB = 0.819376317430065 # antiparallel, bottom positive
ratC = 0.80 # parallel, negative
# SiO2 cap layer
SiO2_t = 124.037890937678
SiO2_sig = 25.1774192037633
SiO2_rho = 3.62631764400711
# top cobalt
top_rhoM = 4.00086354522975
top_t = 184.506745056161
top_sig = 30.8701720412254
# CoCr multilayer
pN = 1.03359526691485
CoCr_t = 26.7422122724653
center_t = 258.943271338257
CoCr_sig = 1
CoCr_rhoM = list(range(7))
CoCr_rhoM[0] = 3.46614455170393
CoCr_rhoM[1] = 3
CoCr_rhoM[2] = 2.45355506662747
CoCr_rhoM[3] = 2
CoCr_rhoM[4] = 1.27055015888177
CoCr_rhoM[5] = 1
CoCr_rhoM[6] = 0.131946246834194
# bot cobalt
bot_rhoM = 4.00086354522975
bot_t = 184.506745056161
bot_sig = 6.74524193762404
# Cr
Cr_t = 324.727526463155
Cr_sig = 20.6635301710672
# Ag
Ag_rho = 3.471
Ag_t = 670.896347017067
Ag_sig = 14.7778796564825
# Si
Si_rho = 2.074
Si_sig = 1.00031060473091

# === Materials ===
SiO2= SLD(name="SiO2",rho=SiO2_rho)
Co= SLD(name="Co",rho=Co_rho,irho=Co_irho)
x = Parameter.default(px, limits=(-10000,10000),name= "x")
N = Parameter.default(pN, limits=(0,10000),name= "tub density factor")

CoCr = list(range(7))
CoCr[6] = SLD(name="CoCr6",rho =N*((Co_rho*(1-(1.00*x)))+(Cr_rho*1.00*x)),irho=N*(Co_irho*(1-(1.00*x))))
CoCr[5] = SLD(name="CoCr5",rho =N*((Co_rho*(1-(0.85*x)))+(Cr_rho*0.85*x)),irho=N*(Co_irho*(1-(0.85*x))))
CoCr[4] = SLD(name="CoCr4",rho =N*((Co_rho*(1-(0.71*x)))+(Cr_rho*0.71*x)),irho=N*(Co_irho*(1-(0.71*x))))
CoCr[3] = SLD(name="CoCr3",rho =N*((Co_rho*(1-(0.57*x)))+(Cr_rho*0.57*x)),irho=N*(Co_irho*(1-(0.57*x))))
CoCr[2] = SLD(name="CoCr2",rho =N*((Co_rho*(1-(0.43*x)))+(Cr_rho*0.43*x)),irho=N*(Co_irho*(1-(0.43*x))))
CoCr[1] = SLD(name="CoCr1",rho =N*((Co_rho*(1-(0.29*x)))+(Cr_rho*0.29*x)),irho=N*(Co_irho*(1-(0.29*x))))
CoCr[0] = SLD(name="CoCr0",rho =N*((Co_rho*(1-(0.14*x)))+(Cr_rho*0.14*x)),irho=N*(Co_irho*(1-(0.14*x))))

Cr= SLD(name="Cr",rho=Cr_rho)
Ag= SLD(name="Ag",rho=Ag_rho)
Si= SLD(name="Si",rho=Si_rho)

# === extra parameters ===
#dM = Parameter.default(pdM, limits=(-10000,10000),name= "dqM")

# === Sample ===
sample = list(range(5))
#         0               1               2                                            
sample[0] = (Si(100,Si_sig)|Ag(Ag_t,Ag_sig)|Cr(Cr_t,Cr_sig)
#	   3       
	 |Co(bot_t,bot_sig,Magnetism(rhoM=bot_rhoM))	 
#	   4	  
	 |CoCr[0](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[0]))
#	   5	  
	 |CoCr[1](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[1]))
#	   6	  
	 |CoCr[2](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[2]))
#	   7	  
	 |CoCr[3](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[3]))
#	   8  
	 |CoCr[4](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[4]))
#	   9	  
	 |CoCr[5](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[5]))
#	   10	  
	 |CoCr[6]((center_t),CoCr_sig,Magnetism(rhoM=CoCr_rhoM[6]))
#	   11	  
	 |CoCr[5](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[5]))
#	   12	  
	 |CoCr[4](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[4]))
#	   13  
	 |CoCr[3](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[3]))
#	   14	  
	 |CoCr[2](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[2]))
#	   15	  
	 |CoCr[1](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[1]))
#	   16	  
	 |CoCr[0](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[0]))
#	   17	  
	 |Co(top_t,top_sig,Magnetism(rhoM=top_rhoM))	
#	   18
	 |SiO2(SiO2_t,SiO2_sig)|air)

#         0               1               2                                            
sample[1] = (Si(100,Si_sig)|Ag(Ag_t,Ag_sig)|Cr(Cr_t,Cr_sig)
#	   3       
	 |Co(bot_t,bot_sig,Magnetism(rhoM=bot_rhoM))	 
#	   4	  
	 |CoCr[0](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[0]))
#	   5	  
	 |CoCr[1](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[1]))
#	   6	  
	 |CoCr[2](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[2]))
#	   7	  
	 |CoCr[3](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[3]))
#	   8  
	 |CoCr[4](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[4]))
#	   9	  
	 |CoCr[5](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[5]))
#	   10	  
	 |CoCr[6]((center_t),CoCr_sig,Magnetism(rhoM=CoCr_rhoM[6]))
#	   11	  
	 |CoCr[5](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[5]))
#	   12	  
	 |CoCr[4](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[4]))
#	   13  
	 |CoCr[3](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[3]))
#	   14	  
	 |CoCr[2](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[2]))
#	   15	  
	 |CoCr[1](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[1]))
#	   16	  
	 |CoCr[0](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[0]))
#	   17	  
	 |Co(top_t,top_sig,Magnetism(rhoM=top_rhoM))	
#	   18
	 |SiO2(SiO2_t,SiO2_sig)|air)

#         0               1               2                                            
sample[2] = (Si(100,Si_sig)|Ag(Ag_t,Ag_sig)|Cr(Cr_t,Cr_sig)
#	   3       
	 |Co(bot_t,bot_sig,Magnetism(rhoM=bot_rhoM))	 
#	   4	  
	 |CoCr[0](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[0]))
#	   5	  
	 |CoCr[1](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[1]))
#	   6	  
	 |CoCr[2](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[2]))
#	   7	  
	 |CoCr[3](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[3]))
#	   8  
	 |CoCr[4](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[4]))
#	   9	  
	 |CoCr[5](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[5]))
#	   10	  
	 |CoCr[6]((center_t),CoCr_sig,Magnetism(rhoM=CoCr_rhoM[6]))
#	   11	  
	 |CoCr[5](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[5]))
#	   12	  
	 |CoCr[4](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[4]))
#	   13  
	 |CoCr[3](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[3]))
#	   14	  
	 |CoCr[2](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[2]))
#	   15	  
	 |CoCr[1](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[1]))
#	   16	  
	 |CoCr[0](CoCr_t,CoCr_sig,Magnetism(rhoM=CoCr_rhoM[0]))
#	   17	  
	 |Co(top_t,top_sig,Magnetism(rhoM=top_rhoM))	
#	   18
	 |SiO2(SiO2_t,SiO2_sig)|air)

# === Constraints ===
# cobalt is cobalt
if 1:
    sample[0][17].thickness = sample[0][3].thickness
# Co / CoCr interface is maximally rough
if 1:
    sample[0][3].interface = sample[0][4].thickness / 4.
    sample[0][16].interface = sample[0][4].thickness / 4.
# bathtub structure
if 1:
    for i in range(4,10):
        sample[0][i].thickness = sample[0][4].thickness
        sample[0][10].thickness = 10*sample[0][4].thickness
    for i in range(11,17):
	    sample[0][i].thickness = sample[0][4].thickness
    for i in range(4,16):
        sample[0][i].interface = sample[0][4].interface
        sample[0][16].interface = sample[0][3].interface

for i in range(0,19):
    for j in range(1,3):
        sample[j][i].thickness = sample[0][i].thickness
        sample[j][i].interface = sample[0][i].interface
# sample A (0) has parallel alignment of + magnetizations
# top Co
if 1:
    sample[0][17].magnetism.rhoM = sample[0][3].magnetism.rhoM
# factor of 2 interpolation in tub
    for i in range(5,10,2):
        sample[0][i].magnetism.rhoM = (sample[0][i-1].magnetism.rhoM+sample[0][i+1].magnetism.rhoM) / 2.0
# CoCr is bathtub
    for i in range(1,7):
        sample[0][10+i].magnetism.rhoM = sample[0][10-i].magnetism.rhoM
# sample B (1) is just like A, but exhibits antiparallel alignment of Co (bottom +)
# and center layer is +
if 1:
    # bottom Co
    sample[1][3].magnetism.rhoM = sample[0][3].magnetism.rhoM
    # top Co
    sample[1][17].magnetism.rhoM = -1*sample[0][3].magnetism.rhoM
    # bottom CoCr
    for i in range(4,11):
        sample[1][i].magnetism.rhoM = sample[0][i].magnetism.rhoM
    for i in range(11,17):
        sample[1][i].magnetism.rhoM = -1*sample[0][i].magnetism.rhoM
# sample C (2) has parallel alignment of - magnetizations
if 1:
    # all layers at once
    for i in range(3,18):
        sample[2][i].magnetism.rhoM = -1*sample[0][i].magnetism.rhoM

# initialize theta offset and renormalization factor
probe.pp.theta_offset.value = th
probe.pp.intensity.value = I0
# theta offset and renorm are spin-independent
probe.mm.theta_offset = probe.pp.theta_offset
probe.mm.intensity = probe.pp.intensity
	
# === Fit parameters ===
# OFFSETS
if 1:
    probe.pp.theta_offset.range(-.02,.02)
    probe.pp.intensity.range(0.1,2)
# SiO2
if 0:
    sample[0][SiO2].thickness.range(50,150)
    sample[0][SiO2].interface.range(1,50)
    SiO2.rho.range(1,6)
# top Co
if 0:
    sample[0][17].thickness.range(150,250)
    sample[0][17].interface.range(1,50)
    sample[0][17].interface.name = "top Co interface"
    Co.rho.range(1,5)
if 0:
    sample[0][17].magnetism.rhoM.range(0,5)
# CoCr
if 0:
    sample[0][16].interface.range(1,10)
    N.range(0.5,1.5)
  #  x.range(0.18,0.38)
    sample[0][4].thickness.range(20,40)
    sample[0][10].thickness.range(100,500)
   # sample[0][4].interface.range(1,10)
#sample[0][4].magnetism.rhoM.range(0,5)
#sample[0][6].magnetism.rhoM.range(0,5)
#sample[0][8].magnetism.rhoM.range(0,5)
#sample[0][10].magnetism.rhoM.range(-5,5)
#sample[1][10].magnetism.rhoM.range(-5,5)
if 0:
    for i in range(4,10,2):
        sample[0][i].magnetism.rhoM.range(0,5)
        sample[0][i].magnetism.rhoM.name = "CoCr rhoM%s"%(i-4)
        sample[0][10].magnetism.rhoM.range(-5,5)
        sample[0][10].magnetism.rhoM.name = "center rhoM A"
        #sample[1][10].magnetism.rhoM.range(-5,5)
        # #sample[1][10].magnetism.rhoM.name = "center rhoM B"
    
# bot Co
if 0:
    sample[0][3].thickness.range(150,250)
    sample[0][3].interface.range(1,10)
    sample[0][3].interface.name = "bot Co interface"
if 0:
    sample[0][3].magnetism.rhoM.range(0,5)
# Cr
if 0:
    sample[0][Cr].thickness.range(300,700)
    sample[0][Cr].interface.range(1,350)
    Cr.rho.range(2,5)
# Ag
if 0:
    sample[0][Ag].thickness.range(600,1000)
    sample[0][Ag].interface.range(1,50)
    Ag.rho.range(2,5)
if 0:
    sample[0][Si].interface.range(1,50)
   # Si.rho.range(1,3)

# === Problem definition ===
zed = 2 # microslabbing bin size, in A
alpha = 0.0 # integration factor - leave this at zero
step = True
M = MixedExperiment(samples=[sample[0],sample[1],sample[2]], probe=probe, dz=zed,dA=0, ratio=[ratA,ratB,ratC])
M.ratio[0].range(0.0,1)
M.ratio[1].range(0.0,1)
M.ratio[2] = 1 - M.ratio[0] - M.ratio[1]
M.ratio[0].name = "Vf A"
M.ratio[1].name = "Vf B"
M.ratio[2].name = "Vf C"

problem = FitProblem(M)
problem.name = "bth 28"