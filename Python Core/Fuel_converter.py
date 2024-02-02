mpg = float(input())

m_to_km = 1.6
gal_to_l = 4.54

con_lpk_100 = (100 / (mpg * m_to_km / gal_to_l))

con_lpk_100 = int(con_lpk_100)

print(f"{con_lpk_100} litres per 100 km")
