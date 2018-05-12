from modules.CreateSubsystem import *
from modules.NewReaction import *

# Create a new SBML Document to hold the subsystem model
sbmlDoc1 = createNewDocument(3,1)
sbmlDoc = CreateSubsystem(sbmlDoc1)

# Create a new model inside the document
model = sbmlDoc.createNewModel("seconds","mole","count")

# Create a unit arguments - id, unitKind, exponent, scale, multiplier
per_second = sbmlDoc.createNewUnit('per_second',UNIT_KIND_SECOND,-1,0,1)

# createNewcompartment arguments - compartment ID, Name, Size, Units, isConstant
comp = sbmlDoc.createNewCompartment('cell','cell',1,'litre',True)

# createNewSpecies arguments - id, name, compartment,
#  initial amount, isConstant, BoundaryCondition, Substance units, HasOnlySubstance

inp = sbmlDoc.createNewSpecies( 'inp','inp','cell',50,False,False,'count',False)
X = sbmlDoc.createNewSpecies( 'X','X','cell',50,False,False,'count',False)
C1 = sbmlDoc.createNewSpecies( 'C1','C1','cell',0,False,False,'count',False)
Xp = sbmlDoc.createNewSpecies( 'Xp','Xp','cell',0,False,False,'count',False)
E = sbmlDoc.createNewSpecies( 'E','E','cell',50,False,False,'count',False)
C2 = sbmlDoc.createNewSpecies( 'C2','C2','cell',0,False,False,'count',False)
C3 = sbmlDoc.createNewSpecies( 'C3','C3','cell',0,False,False,'count',False)
out = sbmlDoc.createNewSpecies( 'out','out','cell',0,False,False,'count',False)
C4 = sbmlDoc.createNewSpecies( 'C4','C4','cell',0,False,False,'count',False)

# Create all parameters 
k1f = sbmlDoc.createNewParameter( 'k1f','k1f',1,False,'per_second')
k1r = sbmlDoc.createNewParameter( 'k1r','k1r',1,False,'per_second')

k2f = sbmlDoc.createNewParameter( 'k2f','k2f',1,False,'per_second')

k3f = sbmlDoc.createNewParameter( 'k3f','k3f',1,False,'per_second')
k3r = sbmlDoc.createNewParameter( 'k3r','k3r',1,False,'per_second')

k4f = sbmlDoc.createNewParameter( 'k4f','k4f',1,False,'per_second')

k5f = sbmlDoc.createNewParameter( 'k5f','k5f',1,False,'per_second')
k5r = sbmlDoc.createNewParameter( 'k5r','k5r',1,False,'per_second')

k6f = sbmlDoc.createNewParameter( 'k6f','k6f',1,False,'per_second')

k7f = sbmlDoc.createNewParameter( 'k7f','k7f',1,False,'per_second')
k7r = sbmlDoc.createNewParameter( 'k7r','k7r',1,False,'per_second')

k8f = sbmlDoc.createNewParameter( 'k8f','k8f',1,False,'per_second')

# Create all reactions
# Arguments - id, isReversible, isFast
r1 = NewReaction(sbmlDoc.createNewReaction('r1',True,False))   
# Arguments - species id, isConstant, Stoichiometry
sref1_inp = r1.createNewReactant('inp',False,1)
sref1_X = r1.createNewReactant('X',False,1)
sref1_C1 = r1.createNewProduct('C1',False,1)
math_r1 = r1.createMath('k1f * inp * X - k1r * C1')
r1_rate = r1.createRate(math_r1)


r2 = NewReaction(sbmlDoc.createNewReaction('r2',False,False))
sref2_C1 = r2.createNewReactant('C1',False,1)
sref2_inp = r2.createNewProduct('inp',False,1)
sref2_Xp = r2.createNewProduct('Xp',False,1)
math_r2 = r2.createMath('k2f * C1')
r2_rate = r2.createRate(math_r2)

r3 = NewReaction(sbmlDoc.createNewReaction('r3',True,False))
sref3_E = r3.createNewReactant('E',False,1)
sref3_Xp = r3.createNewReactant('Xp',False,1)
sref3_C2 = r3.createNewProduct('C2',False,1)
math_r3 = r3.createMath('k3f * E * Xp - k3r * C2')
r3_rate = r3.createRate(math_r3)

r4 = NewReaction(sbmlDoc.createNewReaction('r4',False,False))
sref4_C2 = r4.createNewReactant('C2',False,1)
sref4_E = r4.createNewProduct('E',False,1)
sref4_X = r4.createNewProduct('X',False,1)
math_r4 = r4.createMath('k4f * C2')
r4_rate = r4.createRate(math_r4)

r5 = NewReaction(sbmlDoc.createNewReaction('r5',True,False))
sref5_inp = r5.createNewReactant('inp',False,1)
sref5_Xp = r5.createNewReactant('Xp',False,1)
sref5_C3 = r5.createNewProduct('C3',False,1)
math_r5 = r5.createMath('k5f * inp * Xp - k5r * C3')
r5_rate = r5.createRate(math_r5)

r6 = NewReaction(sbmlDoc.createNewReaction('r6',False,False))
sref6_C3 = r6.createNewReactant('C3',False,1)
sref6_out = r6.createNewProduct('out',False,1)
sref6_inp = r6.createNewProduct('inp',False,1)
math_r6 = r6.createMath('k6f * C3')
r6_rate = r6.createRate(math_r6)

r7 = NewReaction(sbmlDoc.createNewReaction('r7',True,False))
sref7_E = r7.createNewReactant('E',False,1)
sref7_out = r7.createNewReactant('out',False,1)
sref7_C4 = r7.createNewProduct('C4',False,1)
math_r7 = r7.createMath('k7f * E * out - k7r * C4')
r7_rate = r7.createRate(math_r7)

r8 = NewReaction(sbmlDoc.createNewReaction('r8',False,False))
sref8_C4 = r8.createNewReactant('C4',False,1)
sref8_Xp = r8.createNewProduct('Xp',False,1)
sref8_E = r8.createNewProduct('E',False,1)
math_r8 = r8.createMath('k8f * C4')
r8_rate = r8.createRate(math_r8)

# Write to XML file 
writeSBML(sbmlDoc.getNewDocument(),'models/DP.xml')

# Simulate and plot using bioscrape
timepoints = np.linspace(0, 10, 1000)
plotSbmlWithBioscrape('models/DP.xml',0,timepoints,['inp','out'],'Time','Input/Output species',14,14)