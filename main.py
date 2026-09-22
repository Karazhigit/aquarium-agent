def aquarium_agent(temperature, water_level):
    if water_level < 20:
        return "Суды шұғыл толтыру"
    elif temperature < 22:
        return "Жылытқышты қосу"
    elif temperature > 28:
        return "Салқындатуды қосу"
    elif water_level < 30:
        return "Сорғыны қосу"
    elif water_level > 90:
        return "Сорғыны өшіріп, ескерту беру"
    else:
        return "Еш әрекет жасамау"


# Температура — 20°C, су деңгейі — 80%
result = aquarium_agent(20, 80)
print(result)
