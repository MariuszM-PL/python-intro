# Importujemy moduł random do losowego wyboru filmu
import random  # Dokumentacja: https://docs.python.org/3/library/random.html

# Inicjalizujemy listy na filmy i oceny
fav_movies = []
movie_rating = []

print("Podaj TOP10 ulubionych filmów:")

# Pobieramy od użytkownika listę filmów
for x in range(10):
    movie = input()
    fav_movies.append(movie)

# Pobieramy od użytkownika oceny filmów
for movie in fav_movies:
    while True:  # Pętla do poprawnego wprowadzania danych
        try:
            rate = int(input(f"Podaj ocenę [1-10] dla filmu '{movie}': "))  # Prośba o ocenę konkretnego filmu
            if rate < 1 or rate > 10:
                raise ValueError("Ocena musi być w przedziale 1-10.")  # Obsługa błędu, jeśli ocena jest poza zakresem
            movie_rating.append(rate)
            break  # Jeśli wszystko jest poprawne, przerywamy pętlę
        except ValueError as e:  # Dokumentacja: https://docs.python.org/3/library/exceptions.html#ValueError
            print(f"Błąd: {e}. Podaj poprawną liczbę.")  # Komunikat błędu i ponowna próba

# Łączymy listy filmów i ocen w pary
top_ranking = list(zip(fav_movies, movie_rating))  # Dokumentacja: https://docs.python.org/3/library/functions.html#zip

# Filtrowanie filmów z oceną większą niż 5
filtered_movies = [movie for movie, rating in top_ranking if rating > 5]

if filtered_movies:
    # Wybieramy losowy film z przefiltrowanej listy
    recommended_movie = random.choice(filtered_movies) # Dokumentacja: https://docs.python.org/3/library/random.html#random.choice
    print(f"\nPolecany film do obejrzenia to: {recommended_movie}")
else:
    print("\nBrak filmów z oceną większą niż 5 do polecenia.")
