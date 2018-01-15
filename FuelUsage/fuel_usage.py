def total_kilometers(cons, petrol):
    return round(float(petrol) / float(cons) * 100, 2)

def check_distance(distance, cons, petrol):
    reports = []
    kilometers_driven = 0
    if total_kilometers(cons, petrol) < distance:
        return "You will need to refuel"
    while True:
        reports.append([kilometers_driven, distance, petrol])
        kilometers_driven += 100
        distance -= 100
        petrol = round(petrol - cons, 2)
        if distance < 0:
            return reports