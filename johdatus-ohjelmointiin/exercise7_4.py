movies = [
    {"name": "Komisario Palmun erehdys", "year": 1960},
    {"name": "Kauas pilvet karkaavat", "year": 1996},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Inception", "year": 2010},
    {"name": "The Dark Knight", "year": 2008},
    {"name": "Parasite", "year": 2019}
]

# Kaksi erillistä listaa elokuville
old_movies = []
new_movies = []

# Silmukka, joka käy läpi elokuvat ja jaottelee ne eri listoilta
for movie in movies:
    if movie["year"] >= 2000:
        new_movies.append(movie)
    else:
        old_movies.append(movie)

# Tulostetaan elokuvat eri listoilta
print("Seuraavat elokuvat on julkaistu 2000-luvulla: ")
print(", ".join([movie["name"] for movie in new_movies]))

print("\nSeuraavat elokuvat on julkaistu ennen 2000-lukua: ")
print(", ".join([movie["name"] for movie in old_movies]))
