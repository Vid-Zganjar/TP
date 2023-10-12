d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}


keys_with_r = {key: value for key, value in d.items() if 'R' in value or 'r' in value}

print("Ključi, katerih vrednost vsebuje črko r ali veliko tiskano črko R:")
for key in keys_with_r:
    print(key)
