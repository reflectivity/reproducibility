# IMPORTING LIBRARIES AND CLASSES
from refl1d.names import *
from copy import copy
from numpy import *
from scipy.special import erf
T = 29
probe = list(range(T))

probe[0] = load4('YIG_GGG_7K_3T.refl')
probe[1] = load4('YIG_GGG_50K_3T.refl')
probe[2] = load4('YIG_GGG_100K_3T.refl')
probe[3] = load4('YIG_GGG_150K_3T.refl')
probe[4] = load4('YIG_GGG_200K_3T.refl')
probe[5] = load4('YIG_GGG_250K_3T.refl')
probe[6] = load4('YIG_GGG_300K_3T.refl')

probe[7] = load4('YIG_GGG_6K_15mT.refl')
probe[8] = load4('YIG_GGG_50K_15mT.refl')
probe[9] = load4('YIG_GGG_100K_15mT.refl')
probe[10] = load4('YIG_GGG_150K_15mT.refl')
probe[11] = load4('YIG_GGG_200K_15mT.refl')
probe[12] = load4('YIG_GGG_250K_15mT.refl')
probe[13] = load4('YIG_GGG_300K_15mT.refl')

probe[14] = load4('YIG_GGG_Hdep_50mT_7K.refl')
probe[15] = load4('YIG_GGG_Hdep_100mT_7K.refl')
probe[16] = load4('YIG_GGG_Hdep_250mT_7K.refl')
probe[17] = load4('YIG_GGG_Hdep_500mT_7K.refl')
probe[18] = load4('YIG_GGG_Hdep_1000mT_7K.refl')
probe[19] = load4('YIG_GGG_Hdep_1500mT_7K.refl')
probe[20] = load4('YIG_GGG_Hdep_2000mT_7K.refl')


probe[21] = load4('YIG_GGG_Tdep_2T_7K.refl')
probe[22] = load4('YIG_GGG_Tdep_2T_10K.refl')
probe[23] = load4('YIG_GGG_Tdep_2T_15K.refl')
probe[24] = load4('YIG_GGG_Tdep_2T_20K.refl')
probe[25] = load4('YIG_GGG_Tdep_2T_25K.refl')
probe[26] = load4('YIG_GGG_Tdep_2T_30K.refl')
probe[27] = load4('YIG_GGG_Tdep_2T_35K.refl')
probe[28] = load4('YIG_GGG_Tdep_2T_40K.refl')


temp = list(range(T))
temp[0] = '7 K 3000 mT'
temp[1] = '50 K 3000 mT'
temp[2] = '100 K 3000 mT'
temp[3] = '150 K 3000 mT'
temp[4] = '200 K 3000 mT'
temp[5] = '250 K 3000 mT'
temp[6] = '300 K 3000 mT'

temp[7] = '6 K 15 mT'
temp[8] = '50 K 15 mT'
temp[9] = '100 K 15 mT'
temp[10] = '150 K 15 mT'
temp[11] = '200 K 15 mT'
temp[12] = '250 K 15 mT'
temp[13] = '300 K 15 mT'

temp[14] = '7 K 50 mT'
temp[15] = '7 K 100 mT'
temp[16] = '7 K 250 mT'
temp[17] = '7 K 500 mT'
temp[18] = '7 K 1000 mT'
temp[19] = '7 K 1500 mT'
temp[20] = '7 K 2000 mT'

temp[21] = '7 K 2000 mT b'
temp[22] = '10 K 2000 mT'
temp[23] = '15 K 2000 mT'
temp[24] = '20 K 2000 mT'
temp[25] = '25 K 2000 mT'
temp[26] = '30 K 2000 mT'
temp[27] = '35 K 2000 mT'
temp[28] = '40 K 2000 mT'


# offsets
probe[0].pp.intensity.value = 0.258361798868049
probe[1].pp.intensity.value = 0.261043044866879
probe[2].pp.intensity.value = 0.261043044866879
probe[3].pp.intensity.value = 0.261043044866879
probe[4].pp.intensity.value = 0.261043044866879
probe[5].pp.intensity.value = 0.261043044866879
probe[6].pp.intensity.value = 0.261043044866879

probe[7].pp.intensity.value = 1
probe[8].pp.intensity.value = 1
probe[9].pp.intensity.value = 1
probe[10].pp.intensity.value = 1
probe[11].pp.intensity.value = 1
probe[12].pp.intensity.value = 1
probe[13].pp.intensity.value = 1

probe[14].pp.intensity.value = 0.342001684909127
probe[15].pp.intensity.value = 0.342001684909127
probe[16].pp.intensity.value = 0.342001684909127
probe[17].pp.intensity.value = 0.342001684909127
probe[18].pp.intensity.value = 0.342001684909127
probe[19].pp.intensity.value = 0.851042900731781
probe[20].pp.intensity.value = 0.85

probe[21].pp.intensity.value = 0.360769611540784
probe[22].pp.intensity.value = 0.360769611540784
probe[23].pp.intensity.value = 0.360769611540784
probe[24].pp.intensity.value = 0.360769611540784
probe[25].pp.intensity.value = 0.360769611540784
probe[26].pp.intensity.value = 0.360769611540784
probe[27].pp.intensity.value = 0.360769611540784
probe[28].pp.intensity.value = 0.360769611540784

probe[0].pp.sample_broadening.value = 0.0367452564718337

probe[0].pp.theta_offset.value = 0
probe[1].pp.theta_offset.value = 0
probe[2].pp.theta_offset.value = 0
probe[3].pp.theta_offset.value = 0
probe[4].pp.theta_offset.value = 0
probe[5].pp.theta_offset.value = 0
probe[6].pp.theta_offset.value = 0

probe[7].pp.theta_offset.value = 0
probe[8].pp.theta_offset.value = 0
probe[9].pp.theta_offset.value = 0
probe[10].pp.theta_offset.value = 0
probe[11].pp.theta_offset.value = 0
probe[12].pp.theta_offset.value = 0
probe[13].pp.theta_offset.value = 0

probe[14].pp.theta_offset.value = 0
probe[15].pp.theta_offset.value = 0
probe[16].pp.theta_offset.value = 0
probe[17].pp.theta_offset.value = 0
probe[18].pp.theta_offset.value = 0
probe[19].pp.theta_offset.value = 0
probe[20].pp.theta_offset.value = 0

probe[21].pp.theta_offset.value = 0
probe[22].pp.theta_offset.value = 0
probe[23].pp.theta_offset.value = 0
probe[24].pp.theta_offset.value = 0
probe[25].pp.theta_offset.value = 0
probe[26].pp.theta_offset.value = 0
probe[27].pp.theta_offset.value = 0
probe[28].pp.theta_offset.value = 0


for i in range(1,T):
    probe[i].pp.sample_broadening = probe[0].pp.sample_broadening
for i in  range(0,T):
    probe[i].mm.intensity = probe[i].pp.intensity
    probe[i].mm.theta_offset = probe[i].pp.theta_offset
    probe[i].mm.sample_broadening = probe[i].pp.sample_broadening
if 0:
    for i in range(0,T):
        probe[i].oversample(n=21)
#from scipy.special import erf
# MATERIAL CONSTANTS
b_Y = 7.75
b_Fe = 9.45
b_O = 5.805
b_Gd = 1.44
i_Gd = 11.00
b_Ga = 7.288
cYIG_rho = 5.845
cGGG_rho = 4.65
cGGG_irho = 1.39
# INITIAL PARAMETER VALUES 
YIG_t = 150
YIG_sig = 13.4220687631897
diff_t = 50
diff_rho = 5.845
GGG_sig = 10

diff_rhoM = list(range(T))
YIG_rhoM = list(range(T))
GGG_rhoM = list(range(T))

for i in range(0,T):
    YIG_rhoM[i]= 0.5237
    GGG_rhoM[i] = 0
    diff_rhoM[i] = -0.08221
GGG_rhoM[0] = 1

# DEFINE MATERIALS
# enter initial values for nuclear sld in 10^-6 A^-2
GGG= SLD(name="GGG",rho=cGGG_rho,irho=cGGG_irho)
YIG= SLD(name="YIG",rho=cYIG_rho)
diff= SLD(name='diffuse',rho=diff_rho)
# EXTRA PARAMETERS
#xmax = Parameter.default(maxseg, limits=(0,1000),name= "max segregant conc")
sample=list(range(T))
for i in range(0,T):
    #              0    
    sample[i]=(GGG(100,GGG_sig,Magnetism(rhoM=GGG_rhoM[i]))
    #              1
                |diff(diff_t,GGG_sig,Magnetism(rhoM=diff_rhoM[i]))
    #              2
                |YIG(YIG_t,YIG_sig,Magnetism(rhoM=YIG_rhoM[i]))
    #              3             
                |air)
# CONSTRAINTS
# diffusion layer has symmetric roughness
sample[0][diff].interface = sample[0][GGG].interface
# structure is temperature-independent
for i in range(0,T):
    for j in range(0,3):
        sample[i][j].thickness = sample[0][j].thickness
        sample[i][j].interface = sample[0][j].interface
# FITTING PARAMETERS
# OFFSETS
if 1:
    for i in range(0,T):
        probe[i].pp.theta_offset.range(-0.06,0.06)
        probe[i].pp.theta_offset.name = "th "+temp[i]
if 1:
    for i in range(0,T):
        probe[i].pp.intensity.range(0.05,1.5)
        probe[i].pp.intensity.name = "I0 "+temp[i]
if 1:
    probe[0].pp.sample_broadening.range(0.,0.1)
# YIG
if 1:
    sample[0][YIG].thickness.range(50,300)
if 1:
    sample[0][YIG].interface.range(1,50)
if 0:
    YIG.rho.range(4,8)
if 1:
    for i in range(0,T):
        sample[i][YIG].magnetism.rhoM.range(-5,5)
        sample[i][YIG].magnetism.rhoM.name = "YIG rhoM " + temp[i]
# diff
if 1:
    sample[0][diff].thickness.range(2,200)
if 1:
    sample[0][diff].interface.range(1,50)
if 1:
    diff.rho.range(2,8)
if 1:
    for i in range(0,T):
        sample[i][diff].magnetism.rhoM.range(-5,5)
        sample[i][diff].magnetism.rhoM.name = "diff rhoM " + temp[i]
# GGG
if 1:
    sample[0][GGG].interface.range(0,50)
if 0:
    GGG.rho.range(4,8)
if 0:
    GGG.irho.range(0,5)
if 1:
    for i in range(0,T):
        sample[i][GGG].magnetism.rhoM.range(0,5)
        sample[i][GGG].magnetism.rhoM.name = "GGG rhoM " + temp[i]
# problem definition
zed = 0.2 # microslabbing bin size, in A
alpha = 0.0 # integration factor - leave this at zero
step = False # Nevot-Croce = False
model = list(range(T))
for j in range(0,T):
    model[j] = Experiment(sample=sample[j], probe=probe[j], dz=zed, dA=alpha, step_interfaces=step)
# we have 2T models in this case
models = model
# we plug the model into the "FitProblem" object to pass to the fitting program
problem = MultiFitProblem(models=models)