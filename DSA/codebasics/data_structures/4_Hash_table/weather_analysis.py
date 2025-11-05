arr = []
weather_dict = {}
with open(r'C:\Users\ketans\OneDrive - DRCHOKSEY FINSERV PRIVATE LIMITED\Documents\Workspace\DSA\codebasics\4_Hash_table\nyc_weather.csv','r') as f:
    for row in f:
        token = row.split(",")
        try:
            temperature = int(token[1])
            day = token[0]
            arr.append(temperature)
            weather_dict[day] = temperature
        except:
            print("Invalid temparature. Ignore row")

averg_temp_in_1_week = sum(arr[:7])/len(arr[:7])

max_temp_in_week = max(arr)

print("Problem 1.")
print("i.", averg_temp_in_1_week)
print("ii.", max_temp_in_week)

print("Problem 2.")
print("i.", weather_dict['Jan 9'])
print("ii.", weather_dict['Jan 4'])
