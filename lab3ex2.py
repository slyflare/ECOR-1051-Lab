

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg):
    return (mpg*KMS_PER_MILE)/(LITRES_PER_GALLON*100)

lp100km = convert_to_litres_per_100_km(32)
print(lp100km)
lp100km = convert_to_litres_per_100_km(0)
print(lp100km)
lp100km = convert_to_litres_per_100_km(32.0)
print(lp100km)