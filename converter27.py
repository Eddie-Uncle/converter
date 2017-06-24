##RUNS in puython 2.7 ###
# Program to convert meters to feets and viceversa
 
print ('\n       Feet - Meter converter\n\n')
 
meter_or_feet =  str(raw_input ('You know your height in meters or feets?: '))
 
if meter_or_feet == str('meters'):
        height_meters = float(raw_input ('Enter your height in meters: '))
        print 'Your height in feets is ',(height_meters / 0.3048 ),'feets'
else:
        height_feets = float(raw_input ('Enter your height in feets: '))
        print 'Your height in meters is ',(height_feets * 0.3048 ),'meters'