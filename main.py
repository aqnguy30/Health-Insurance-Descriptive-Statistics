#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:23:11 2020

@author: anhnguyen
"""
#bmi
import numpy as np
import pandas as pd
from scipy import stats
arr = np.loadtxt('insurance.txt', dtype = {'names': ('age', 'sex', 'bmi', 'children', 'smoker', 'region', 'expenses' ), 'formats':[np.float,'S100',np.float,np.float,'S100','S100',np.float]}, skiprows = 1)
print(arr)
print(np.shape(arr))

#Compute 'age'
print('Age')
print(np.mean(arr['age']))
print(np.std(arr['age']))
print(np.median(arr['age']))
age_mean = np.array([np.round(np.mean(arr['age']),2)])
age_std = np.array([np.round(np.std(arr['age']),2)])
age_median = np.array([np.round(np.median(arr['age']),2)])

#Compute 'bmi'
print('BMI')
print(np.mean(arr['bmi']))
print(np.std(arr['bmi']))
print(np.median(arr['bmi']))
bmi_mean = np.array([np.round(np.mean(arr['bmi']),2)])
bmi_std = np.array([np.round(np.std(arr['bmi']),2)])
bmi_median = np.array([np.round(np.median(arr['bmi']),2)])

#Compute 'bmi' grouped by sex
bmi1 = arr['bmi']
sex1 = arr['sex']
all_sex = np.unique(arr['sex'])
bmi_sex_mean = [(i, np.mean(bmi1[sex1==i])) for i in all_sex]
bmi_sex_std = [(i, np.std(bmi1[sex1==i])) for i in all_sex]
bmi_sex_median = [(i, np.median(bmi1[sex1==i])) for i in all_sex]
print(bmi_sex_mean)
print(bmi_sex_std)
print(bmi_sex_median)

#Compute 'bmi' grouped by smoker
bmi1 = arr['bmi']
smoker1 = arr['smoker']
all_smoker = np.unique(arr['smoker'])
bmi_smoker_mean = [(i, np.mean(bmi1[smoker1==i])) for i in all_smoker]
bmi_smoker_std = [(i, np.std(bmi1[smoker1==i])) for i in all_smoker]
bmi_smoker_median = [(i, np.median(bmi1[smoker1==i])) for i in all_smoker]
print(bmi_smoker_mean)
print(bmi_smoker_std)
print(bmi_smoker_median)


#Compute 'bmi' grouped by region
bmi1 = arr['bmi']
region1 = arr['region']
all_region = np.unique(arr['region'])
bmi_region_mean = [(i, np.mean(bmi1[region1==i])) for i in all_region]
bmi_region_std = [(i, np.std(bmi1[region1==i])) for i in all_region]
bmi_region_median = [(i, np.median(bmi1[region1==i])) for i in all_region]
print(bmi_region_mean)
print(bmi_region_std)
print(bmi_region_median)

#Compute 'bmi' grouped by children
bmi1 = arr['bmi']
children1 = arr['children']
all_children = np.unique(arr['children'])
all_children_more2 = np.unique([x for x in arr['children'] if x > 2])
print(np.unique(all_children_more2))
print(all_children)

bmi_children_more2 = np.array([bmi1[children1==i] for i in all_children_more2])
print(np.shape(bmi_children_more2))
a = np.hstack(bmi_children_more2)
print(np.mean(a))
print(np.std(a))
print(np.median(a))
bmi_children_mean = np.array([np.round(np.mean(a),2)])
bmi_children_std = np.array([np.round(np.std(a),2)])
bmi_children_median = np.array([np.round(np.median(a),2)])
#Bonus for each group:
bmi_children_mean1 = [(i, np.mean(bmi1[children1==i])) for i in all_children_more2]
bmi_children_std1 = [(i, np.std(bmi1[children1==i])) for i in all_children_more2]
bmi_children_median1 = [(i, np.median(bmi1[children1==i])) for i in all_children_more2]
print(bmi_children_mean1)
print(bmi_children_std1)
print(bmi_children_median1)

# mean and standard deviation of BMI for the top 20% and ~20
df = pd.read_csv('insurance.txt',sep="\t" ) 
df2 = df.sort_values(by=['expenses'], ascending=False) 
top_20_expenses = df2[:268]
non_top_20 = df2[268:]

mean_20 = (np.mean(top_20_expenses['bmi']))
std_20 = (np.std(top_20_expenses['bmi']))

mean_non20 = (np.mean(non_top_20['bmi']))
std_non20 = (np.std(non_top_20['bmi']))

# mode of smoker and region of top 20% and ~20%
mode_20_smokers = (stats.mode(top_20_expenses['smoker']))
mode_20_regions = (stats.mode(top_20_expenses['region']))
print('The mode of smoker for the top 20% of the expenses:')
print(mode_20_smokers)
print('The mode of region for the top 20% of the expenses:')
print(mode_20_regions)

mode_non20_smokers = (stats.mode(non_top_20['smoker']))
mode_non20_regions = (stats.mode(non_top_20['region']))
print('The mode of smoker for the rest 80% of the expenses:')
print(mode_non20_smokers)
print('The mode of region for the rest 80% of the expenses:')
print(mode_non20_regions)

print('The top 20% by expenses average bmi is: {:.2f}, standard deviation: {:.2f}, they tend to be smokers and from the SE'
      .format(mean_20, std_20))
print('The rest 80% by expenses average bmi is: {:.2f}, standard deviation: {:.2f}, they tend to be nonsmokers, also from the SE'
      .format(mean_non20, std_non20))
print(''' \t The primary reasons for expense according to the data seems to be 
smokers, who tend to be considered obese from the Southeast region but it does
seem like most of the data is collect on obese people from the Southeast region.
''')

#Display the result:
f=open('hw5_output.txt','a')
np.savetxt(f, age_mean, fmt='%s', newline='\n', header='The mean of age:')
f.write("\n")
np.savetxt(f, age_std, fmt='%s', newline='\n', header='The standard deviation of age:')
f.write("\n")
np.savetxt(f, age_median, fmt='%s', newline='\n', header='The median of age:')
f.write("\n")

np.savetxt(f, bmi_mean, fmt='%s', newline='\n', header='The mean of BMI:')
f.write("\n")
np.savetxt(f, bmi_std, fmt='%s', newline='\n', header='The standard deviation of BMI:')
f.write("\n")
np.savetxt(f, bmi_median, fmt='%s', newline='\n', header='The median of BMI:')
f.write("\n")

np.savetxt(f, bmi_sex_mean, fmt='%s', newline='\n', header='The mean of BMI grouped by sex:')
f.write("\n")
np.savetxt(f, bmi_sex_std, fmt='%s', newline='\n', header='The standard deviation of BMI grouped by sex:')
f.write("\n")
np.savetxt(f, bmi_sex_median, fmt='%s', newline='\n', header='The median of BMI grouped by sex:')
f.write("\n")
np.savetxt(f, bmi_smoker_mean, fmt='%s', newline='\n', header='The mean of BMI for non-smokers NO and smokers YES:')
f.write("\n")
np.savetxt(f, bmi_smoker_std, fmt='%s', newline='\n', header='The standard deviation of BMI for non-smokers NO and smokers YES:')
f.write("\n")
np.savetxt(f, bmi_smoker_median, fmt='%s', newline='\n', header='The median of BMI for non-smokers NO and smokers YES:')
f.write("\n")
np.savetxt(f, bmi_region_mean, fmt='%s', newline='\n', header='The mean of BMI grouped by region:')
f.write("\n")
np.savetxt(f, bmi_region_std, fmt='%s', newline='\n', header='The standard deviation of BMI grouped by region:')
f.write("\n")
np.savetxt(f, bmi_region_median, fmt='%s', newline='\n', header='The median of BMI grouped by region:')
f.write("\n")
np.savetxt(f, bmi_children_mean, fmt='%s', newline='\n', header='The mean of BMI of those who have more than 2 children:')
f.write("\n")
np.savetxt(f, bmi_children_std, fmt='%s', newline='\n', header='The standard deviation of BMI of those who have more than 2 children:')
f.write("\n")
np.savetxt(f, bmi_children_median, fmt='%s', newline='\n', header='The median of BMI of those who have more than 2 children:')
f.write("\n")

f.close()
    
