class Movie():
    """Class for favorite movies"""
    def __init__(self, movie_title, movie_desc, movie_poster_image_url,
                 movie_trailer_youtube_url, movie_year):
        self.title = movie_title
        self.desc = movie_desc
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
        self.year = movie_year
