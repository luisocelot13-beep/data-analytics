import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100,75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

print('_Experimenting with a subset of integers 1-100:')
# add values inside the random salples
sample_sum = sum(vals_sample)

# print the total
print(f'Sum of 75 sample values from 1 to 100 :{sample_sum}')
# ----------------------------------------------------------------------
sample_avg = sample_sum / len(vals_sample)
# avg = total sum divided by number of values

print(f'Average of 75 sample values:{sample_avg}')
#-------------------------------------------------------------------------
# finding median

sample_median = statistics.median(vals_sample)

print(f'Median of 75 sample values:{sample_median}')
print('\n')
# ------------------------------------------------------------------------------------------------------
print('_Experimenting with a superset of 200 values, integers 1 - 100')
choices_sum = sum(vals_choices)

#calculate avg
choices_avg =  choices_sum / len(vals_choices)

print(f'Average of 200 values: {choices_avg}')
# ---------------------------------------------------------------------------
choices_median = statistics.median(vals_choices)
# find the middle value from the 200 random numbers

print(f'Median of 200 values: {choices_median}')
#--------------------------------------------------------------------------------

choices_mode = statistics.mode(vals_choices)
# find the value that appears most often

print(f'mode of 200 values: {choices_mode}')

# ---------------------------------------------------------------------------------
# Standard deviation of 200 values

choices_stdev = statistics.stdev(vals_choices)

# print standard deviation
print(f'Standard deviation of 200 values:{choices_stdev}')

#-------------------------------------------------------------------
#Variance of 200 values

choices_variance = statistics.variance(vals_choices)

print(f'Variance of 2000 values:{choices_variance}')
print('\n')
# ---------------------------------------------------------------------
print('_Modeling a random circle:')
radius = random.randint(3,10)

area = pi * radius **2
#calculate circle area

area_up = math.ceil(area)
# round area upward

print(f'radius = {radius},area = {area_up}(Round to the nearest integer)')
# ----------------------------------------------------------------------
#Modeling circle rounded down to the nearest integer

area_down = math.floor(area)

print(f'Radius = {radius}, area = {area_down}(Rounded down to the nearest integer)')
