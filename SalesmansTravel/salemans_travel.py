def travel(r, zipcode):
    clients = []
    streets = ""
    numbers = ""
    addresses = r.split(',')

    for address in addresses:
        if address[-8:] == zipcode:
            clients.append(address)

    for client in clients:
        words = client[:-8].split(" ")
        numbers += words[0] + ","
        streets += " ".join(words[1:])
        streets = streets[:-1] + ","

    return zipcode + ":" + streets[:-1] + "/" + numbers[:-1]