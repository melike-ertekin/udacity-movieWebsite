import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story 3",
            "A story of a boy and his toys that come to life.",
            "https://images-na.ssl-images-amazon.com/images/I/519fFTj6QnL._SY450_.jpg",
            "https://www.youtube.com/watch?v=TNMpa5yBf5o")


"""interstellar = media.Movie("Interstellar",
            "This is a placeholder for storyline.",
            "https://cdn.shopify.com/s/files/1/1416/8662/products/interstellar_2014_original_film_art_2000x.jpg?v=1521741534",
            "hhttps://www.youtube.com/watch?v=zSWdZVtXT7E")"""


harry_potter = media.Movie("Harry Potter and the Deathly Hallows",
            "This is a placeholder for storyline.",
            "https://images-na.ssl-images-amazon.com/images/I/51IWlffOs%2BL.jpg",
            "https://www.youtube.com/watch?v=9hXH0Ackz6w")

book_thief = media.Movie("The Book Thief",
            "AThis is a placeholder for storyline.",
            "http://img.moviepostershop.com/the-book-thief-movie-poster-2013-1020768819.jpg",
            "https://www.youtube.com/watch?v=6dRuGwS1gWU")

movies = [toy_story, harry_potter, book_thief]
fresh_tomatoes.open_movies_page(movies)
