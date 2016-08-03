import webbrowser

class Movie():
    VALID_RATINGS = ["G", "PG", "R", "PG-13"]
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube, year, director, actors):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = year
        self.movie_director = director
        self.movie_actors = actors
        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
