# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UP4si-Y5p5-bUEQjBpxjRQycKVOPnsSx
"""

pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz

import matplotlib.pyplot as plt

x =  np.arange(50,81,1)

slow = fuzz.trimf(x,[50,50,60])
medium = fuzz.trimf(x,[50,60,70])
medium_fast = fuzz.trimf(x,[60,70,80])
full_speed = fuzz.trimf(x,[70,80,80])
plt.figure()
plt.plot(x,slow,'b',linewidth = 1.5, label = 'slow')
plt.plot(x,medium,'y', linewidth = 1.5, label = 'medium' )
plt.plot(x,medium_fast, 'r', linewidth = 1.5, label = 'medium_fast')
plt.plot(x,full_speed, 'g', linewidth = 1.5, label = 'full_speed')

slow = fuzz.gaussmf(x,50,4)
medium = fuzz.gaussmf(x,60,4)
medium_fast = fuzz.gaussmf(x,70,4)
full_speed = fuzz.gaussmf(x,80,4)
plt.figure()
plt.plot(x,slow,'b',linewidth = 1.5, label = 'slow')
plt.plot(x,medium,'y', linewidth = 1.5, label = 'medium' )
plt.plot(x,medium_fast, 'r', linewidth = 1.5, label = 'medium_fast')
plt.plot(x,full_speed, 'g', linewidth = 1.5, label = 'full_speed')



slow = fuzz.trapmf(x,[50,50,60])
medium = fuzz.trapmf(x,[50,60,70])
medium_fast = fuzz.trapmf(x,[60,70,80])
full_speed = fuzz.trapmf(x,[70,80,80])
plt.figure()
plt.plot(x,slow,'b',linewidth = 1.5, label = 'slow')
plt.plot(x,medium,'y', linewidth = 1.5, label = 'medium' )
plt.plot(x,medium_fast, 'r', linewidth = 1.5, label = 'medium_fast')
plt.plot(x,full_speed, 'g', linewidth = 1.5, label = 'full_speed')

x =  np.arange(0,11,1)
poor = fuzz.trimf(x,[0,0,5])
average = fuzz.trimf(x,[0,5,10])
good = fuzz.trimf(x,[5,10,10])

plt.figure()
plt.plot(x,poor,'b',linewidth = 1.5, label = 'poor')
plt.plot(x,average,'y', linewidth = 1.5, label = 'average' )
plt.plot(x,good, 'r', linewidth = 1.5, label = 'good')

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
food= ctrl.Antecedent(np.arange(0,11,1),'food')
service= ctrl.Antecedent(np.arange(0,11,1),'service')
tip= ctrl.Consequent(np.arange(0,31,1),'tip')

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

food= ctrl.Antecedent(np.arange(0,11,1),'food')
service= ctrl.Antecedent(np.arange(0,11,1),'service')
tip= ctrl.Consequent(np.arange(0,31,1),'tip')

food['poor']= fuzz.trimf(food.universe,[0,0,5])
food['average']= fuzz.trimf(food.universe,[0,5,10])
food['good']= fuzz.trimf(food.universe,[5,10,10])

service['poor']= fuzz.trimf(service.universe,[0,0,5])
service['average']= fuzz.trimf(service.universe,[0,5,10])
service['good']= fuzz.trimf(service.universe,[5,10,10])

tip['less']= fuzz.trimf(tip.universe,[0,0,10])
tip['average']= fuzz.trimf(tip.universe,[0,0,20])
tip['much']= fuzz.trimf(tip.universe,[0,0,30])

food.view()
service.view()
tip.view()

rule1=ctrl.Rule(food['poor'] & service['poor'],tip['less'])
rule2=ctrl.Rule(food['poor'] & service['average'],tip['less'])
rule3=ctrl.Rule(food['average'] & service['poor'],tip['less'])
rule4=ctrl.Rule(food['average'] & service['average'],tip['average'])
rule5=ctrl.Rule(food['average'] & service['good'],tip['much'])
rule6=ctrl.Rule(food['good'] & service['average'],tip['much'])
rule7=ctrl.Rule(food['poor'] & service['good'],tip['average'])
rule8=ctrl.Rule(food['good'] & service['poor'],tip['average'])
rule9=ctrl.Rule(food['good'] & service['good'],tip['much'])

tipping_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9])
tipping=ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['food']=6.5
tipping.input['service']=5.8
tipping.compute()
print(tipping.output['tip'])
tip.view(sim=tipping)

rule1=ctrl.Rule(food['poor'] & service['poor'],tip['less'])
rule2=ctrl.Rule(food['poor'] & service['average'],tip['less'])
rule3=ctrl.Rule(food['average'] & service['poor'],tip['less'])
rule4=ctrl.Rule(food['average'] & service['average'],tip['average'])
rule5=ctrl.Rule(food['average'] & service['good'],tip['much'])
rule6=ctrl.Rule(food['good'] & service['average'],tip['much'])
rule7=ctrl.Rule(food['poor'] & service['good'],tip['average'])
rule8=ctrl.Rule(food['good'] & service['poor'],tip['average'])
rule9=ctrl.Rule(food['good'] & service['good'],tip['much'])

tipping_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9])
tipping=ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['food']=6.5
tipping.input['service']=5.8
tipping.compute()
print(tipping.output['tip'])
tip.view(sim=tipping)

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

time= ctrl.Antecedent(np.arange(10,181,1),'time')
rice= ctrl.Antecedent(np.arange(100,1501,1),'rice')
power= ctrl.Consequent(np.arange(0,101,1),'power')

time['very fast']= fuzz.trimf(time.universe,[10,15,20])
time['fast']= fuzz.trimf(time.universe,[20,25,30])
time['normal']= fuzz.trimf(time.universe,[30,40,50])
time['slow']= fuzz.trapmf(time.universe,[60,70,80,90])
time['very slow']= fuzz.trapmf(time.universe,[100,140,160,180])

rice['very much']= fuzz.trimf(rice.universe,[1300,1400,1500])
rice['much']= fuzz.trimf(rice.universe,[1000,1100,1200])
rice['average']= fuzz.trimf(rice.universe,[700,800,900])
rice['little']= fuzz.trimf(rice.universe,[300,400,500])
rice['least']= fuzz.trimf(rice.universe,[100,200,300])

power['very high']= fuzz.trimf(power.universe,[90,95,100])
power['high']= fuzz.trimf(power.universe,[70,75,80])
power['normal']= fuzz.trimf(power.universe,[50,55,60])
power['low']= fuzz.trimf(power.universe,[30,35,40])
power['very low']= fuzz.trimf(power.universe,[1,10,20])

time.view()
rice.view()
power.view()

rule1=ctrl.Rule(time['very fast'] & rice['very much'],power['very high'])
rule2=ctrl.Rule(time['very fast'] & rice['much'],power['very high'])
rule3=ctrl.Rule(time['very fast'] & rice['average'],power['very high'])
rule4=ctrl.Rule(time['very fast'] & rice['little'],power['normal'])
rule5=ctrl.Rule(time['very fast'] & rice['least'],power['normal'])
rule6=ctrl.Rule(time['fast'] & rice['very much'],power['very high'])
rule7=ctrl.Rule(time['fast'] & rice['much'],power['very high'])
rule8=ctrl.Rule(time['fast'] & rice['average'],power['high'])
rule9=ctrl.Rule(time['fast'] & rice['little'],power['normal'])
rule10=ctrl.Rule(time['fast'] & rice['least'],power['normal'])
rule11=ctrl.Rule(time['normal'] & rice['very much'],power['high'])
rule12=ctrl.Rule(time['normal'] & rice['much'],power['normal'])
rule13=ctrl.Rule(time['normal'] & rice['average'],power['normal'])
rule14=ctrl.Rule(time['normal'] & rice['little'],power['low'])
rule15=ctrl.Rule(time['normal'] & rice['least'],power['low'])
rule16=ctrl.Rule(time['slow'] & rice['very much'],power['normal'])
rule17=ctrl.Rule(time['slow'] & rice['much'],power['normal'])
rule18=ctrl.Rule(time['slow'] & rice['average'],power['low'])
rule19=ctrl.Rule(time['slow'] & rice['little'],power['very low'])
rule20=ctrl.Rule(time['slow'] & rice['least'],power['very low'])
rule21=ctrl.Rule(time['very slow'] & rice['very much'],power['normal'])
rule22=ctrl.Rule(time['very slow'] & rice['much'],power['normal'])
rule23=ctrl.Rule(time['very slow'] & rice['average'],power['low'])
rule24=ctrl.Rule(time['very slow'] & rice['little'],power['very low'])
rule25=ctrl.Rule(time['very slow'] & rice['least'],power['very low'])

powering_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25])
powering=ctrl.ControlSystemSimulation(powering_ctrl)
powering.input['time']= 60
powering.input['rice']= 400
powering.compute()
print(powering.output['power'])
power.view(sim=powering)

