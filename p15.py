# p15.py
# Kyle Garcia
# 6/11/2020
# Python 3.8
# Description: Program which uses a while loop to display a conversion table for kilograms and pounds.

print('\nKilograms:     |     Pounds: ')
print('======================================', end = '\n')

kg = 0

while kg < 199: # loops... until 199
    kg += 1 # increment by 1
    odd = kg%2; # finds if there is a remainder
    
    if odd != 0: # if the number is odd, then...
        lb = kg * 2.2; # convert kg to lb
        print(' {:<5.1f} kg            {:>5.1f} lb      '.format(kg,lb)); # print the weights
        
'''
>>>
 
Kilograms:     |     Pounds: 
======================================
 1.0   kg              2.2 lb      
 3.0   kg              6.6 lb      
 5.0   kg             11.0 lb      
 7.0   kg             15.4 lb      
 9.0   kg             19.8 lb      
 11.0  kg             24.2 lb      
 13.0  kg             28.6 lb      
 15.0  kg             33.0 lb      
 17.0  kg             37.4 lb      
 19.0  kg             41.8 lb      
 21.0  kg             46.2 lb      
 23.0  kg             50.6 lb      
 25.0  kg             55.0 lb      
 27.0  kg             59.4 lb      
 29.0  kg             63.8 lb      
 31.0  kg             68.2 lb      
 33.0  kg             72.6 lb      
 35.0  kg             77.0 lb      
 37.0  kg             81.4 lb      
 39.0  kg             85.8 lb      
 41.0  kg             90.2 lb      
 43.0  kg             94.6 lb      
 45.0  kg             99.0 lb      
 47.0  kg            103.4 lb      
 49.0  kg            107.8 lb      
 51.0  kg            112.2 lb      
 53.0  kg            116.6 lb      
 55.0  kg            121.0 lb      
 57.0  kg            125.4 lb      
 59.0  kg            129.8 lb      
 61.0  kg            134.2 lb      
 63.0  kg            138.6 lb      
 65.0  kg            143.0 lb      
 67.0  kg            147.4 lb      
 69.0  kg            151.8 lb      
 71.0  kg            156.2 lb      
 73.0  kg            160.6 lb      
 75.0  kg            165.0 lb      
 77.0  kg            169.4 lb      
 79.0  kg            173.8 lb      
 81.0  kg            178.2 lb      
 83.0  kg            182.6 lb      
 85.0  kg            187.0 lb      
 87.0  kg            191.4 lb      
 89.0  kg            195.8 lb      
 91.0  kg            200.2 lb      
 93.0  kg            204.6 lb      
 95.0  kg            209.0 lb      
 97.0  kg            213.4 lb      
 99.0  kg            217.8 lb      
 101.0 kg            222.2 lb      
 103.0 kg            226.6 lb      
 105.0 kg            231.0 lb      
 107.0 kg            235.4 lb      
 109.0 kg            239.8 lb      
 111.0 kg            244.2 lb      
 113.0 kg            248.6 lb      
 115.0 kg            253.0 lb      
 117.0 kg            257.4 lb      
 119.0 kg            261.8 lb      
 121.0 kg            266.2 lb      
 123.0 kg            270.6 lb      
 125.0 kg            275.0 lb      
 127.0 kg            279.4 lb      
 129.0 kg            283.8 lb      
 131.0 kg            288.2 lb      
 133.0 kg            292.6 lb      
 135.0 kg            297.0 lb      
 137.0 kg            301.4 lb      
 139.0 kg            305.8 lb      
 141.0 kg            310.2 lb      
 143.0 kg            314.6 lb      
 145.0 kg            319.0 lb      
 147.0 kg            323.4 lb      
 149.0 kg            327.8 lb      
 151.0 kg            332.2 lb      
 153.0 kg            336.6 lb      
 155.0 kg            341.0 lb      
 157.0 kg            345.4 lb      
 159.0 kg            349.8 lb      
 161.0 kg            354.2 lb      
 163.0 kg            358.6 lb      
 165.0 kg            363.0 lb      
 167.0 kg            367.4 lb      
 169.0 kg            371.8 lb      
 171.0 kg            376.2 lb      
 173.0 kg            380.6 lb      
 175.0 kg            385.0 lb      
 177.0 kg            389.4 lb      
 179.0 kg            393.8 lb      
 181.0 kg            398.2 lb      
 183.0 kg            402.6 lb      
 185.0 kg            407.0 lb      
 187.0 kg            411.4 lb      
 189.0 kg            415.8 lb      
 191.0 kg            420.2 lb      
 193.0 kg            424.6 lb      
 195.0 kg            429.0 lb      
 197.0 kg            433.4 lb      
 199.0 kg            437.8 lb
 
>>> 
'''
