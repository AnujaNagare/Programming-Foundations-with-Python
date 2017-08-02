import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)


avatar = media.Movie("Avatar",
						"epic science fiction film",
						"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=5PSNL1qE6VY")

Zootopia = media.Movie("Zootopia",
						"3D computer-animated buddy mystery comedy-adventure film",
						"https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
						"https://www.youtube.com/watch?v=jWM0ct-OLsM")


# print(toy_story.storyline)
# Zootopia.show_trailer()

movies = [toy_story, avatar, Zootopia]
fresh_tomatoes.open_movies_page(movies)