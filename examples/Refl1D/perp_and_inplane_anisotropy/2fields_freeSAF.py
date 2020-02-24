# multilayer with perpendicular anisotropy FePd synthetic antiferromagnet (SAF) and in-plane Co2MnSi
# measured at two values of in-plane field (saturation and near-remenance)
# grown by Dan Gopman, NIST
from refl1d.names import *
from numpy import *
# LOAD DATA AND CREATE A PROBE
H = 2 # number of field conditions
probe = list(range(H))
probe[0] = load4('SAFH_2490703A_300K_700mT72499.refl')
probe[1] = load4('SAFH_2490703A_300K_1mT72513.refl')
probe[0].pp.intensity.value = 1
probe[0].pp.sample_broadening.value = 0.06
probe[0].pp.theta_offset.value = 0
probe[1].pp.intensity.value = 1
probe[1].pp.theta_offset.value = 0

for i in range(0,H):
    probe[i].mm.intensity = probe[i].pp.intensity
    probe[i].mm.theta_offset = probe[i].pp.theta_offset
    probe[i].pp.sample_broadening = probe[0].pp.sample_broadening
    probe[i].mm.sample_broadening = probe[i].pp.sample_broadening

# DEFINE MATERIALS
# enter initial values for nuclear sld in 10^-6 A^-2
MgO= SLD(name="MgO",rho=5.98)
Cr= SLD(name="Cr",rho=3.027)
Pt= SLD(name="Pt",rho=6.357)
FePd= SLD(name="FePd",rho=6.02)
Ir= SLD(name="Ir",rho=7.446)
Co2MnSi= SLD(name="Co2MnSi",rho=0.9)
Ru= SLD(name="Ru",rho=5.191)
Ta= SLD(name="Ta",rho=3.83)

# DEFINE A LAYER STRUCTURE
# define each layer as:
# material(thickness,roughness,Magnetism(rhoM,thetaM))
# thickness & roughness are in A
# rhoM is in 10^-6 A^-2
# thetaM is in degrees (270 is parallel to H)
sample = list(range(H))
for i in range(0,H):
#              0    
    sample[i]=(MgO(5000,5)
#              1   
              |Cr(150,5)
#              2   
              |Pt(50,5)
#              3   
              |FePd(60,5,Magnetism(1))
#              4   
              |Ir(5,5)
#              5   
              |FePd(60,5,Magnetism(1))
#              6   
              |Co2MnSi(100,5,Magnetism(1))
#              7   
              |Ru(30,5)
#              8   
              |Ta(20,5)
#              9         
              |air)

# CONSTRAINTS
if 1:
    for i in range(1,10):
        sample[0][i].interface = sample[0][0].interface
if 1:
    sample[0][5].thickness = sample[0][3].thickness
    sample[0][4].thickness = sample[0][3].thickness*5/60.
if 0:    
    for i in range(0,H):
        sample[i][5].magnetism.rhoM = sample[i][3].magnetism.rhoM
for i in range(1,H):
    for j in range(0,10):
        sample[i][j].thickness = sample[0][j].thickness
        sample[i][j].interface = sample[0][j].interface
# DEFINE FITTING PARAMETERS
# Beam parameters
if 1:
    for i in range(0,H):
        probe[i].pp.intensity.range(0.1,3)
        probe[i].pp.intensity.name = "I0 %s"%(i)
if 1:
    for i in range(0,H):
        probe[i].pp.theta_offset.range(-0.02,0.02)
        probe[i].pp.theta_offset.name = "th %s"%(i)
if 1:
    for i in range(0,H):
        probe[i].pp.sample_broadening.range(0,0.1)
# global roughness
if 1:
    sample[0][0].interface.range(1,50)
# Ta
if 1:
    Ta.rho.range(2,12)
if 1:
    sample[0][Ta].thickness.range(10,40)
# Ru
if 1:
    Ru.rho.range(2,6)
if 1:
    sample[0][Ru].thickness.range(10,90)
# Co2MnSi
if 1:
    Co2MnSi.rho.range(-1,3)
if 1:
    sample[0][Co2MnSi].thickness.range(2,130)
if 1:
    for i in range(0,H):
        sample[i][Co2MnSi].magnetism.rhoM.range(-5,5)
        sample[i][Co2MnSi].magnetism.rhoM.name = "Co2MnSi rhoM %s"%(i)
# SAF
if 1:
    FePd.rho.range(2,7)
if 1:
    sample[0][3].thickness.range(40,80)
if 1:
    for i in range(0,H):
        sample[i][3].magnetism.rhoM.range(-5,5)
        sample[i][3].magnetism.rhoM.name = "bot FePd rhoM %s"%(i)
if 1:
    for i in range(0,H):
        sample[i][5].magnetism.rhoM.range(-5,5)
        sample[i][5].magnetism.rhoM.name = "top FePd rhoM %s"%(i)
# Pt
if 1:
    Pt.rho.range(4,8)
if 1:
    sample[0][Pt].thickness.range(20,90)
# Cr
if 1:
    Cr.rho.range(2,5)
if 1:    
    sample[0][Cr].thickness.range(100,200)
if 0:
    MgO.rho.range(4,7)
# PROBLEM DEFINITION
zed = 0.2 # microslabbing bin size, in A
alpha = 0.0 # integration factor - leave this at zero
step = False # Nevot-Croce = False
model = list(range(H))
for j in range(0,H):
    model[j] = Experiment(sample=sample[j], probe=probe[j], dz=zed, dA=alpha, step_interfaces=step)
# we have 2H models in this case
models = model
# we plug the model into the "FitProblem" object to pass to the fitting program
problem = MultiFitProblem(models=models)