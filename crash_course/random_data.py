import random

rand = random.randrange(1,30)
movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']

# pick a random element from a list of strings.
movie = random.choice(movie_list)
print(movie)
print(rand)