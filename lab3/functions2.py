# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# exercise 1
def isMovieCool(name):
    for movie in movies:
        if movie.get("name") == name:
           if int(movie.get("imdb")) > 5.5:
               return True
    return False

# exercise 2
def getCoolMovies():
    result = []
    for movie in movies:
        if isMovieCool(movie.get('name')):
            result.append(movie)
    return result

# exercise 3
def returnSameCategory(category):
    result = []
    for movie in movies:
        if movie.get('category') == category:
            result.append(movie)
    return result

# exercise 4
def calcAverageScore():
    sum = 0
    count = 0
    for movie in movies:
        sum += float(movie.get('imdb'))
        count += 1
    return (sum / count)

# exercise 5
def sameCategoryAverageScore(category):
    listSameCategory = returnSameCategory(category)
    return calcAverageScore(listSameCategory)