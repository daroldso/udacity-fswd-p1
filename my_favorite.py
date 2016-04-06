class Favorite_Movie():
    """Class to provide API for getting list of favorite movies"""
    def __init__(self):
        self.movies = [
        ('Toy Story',
        'Story Aout Toys',
        'http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450',
        'https://www.youtube.com/watch?v=KYz2wyBy3kc'),
        ('Ten Years',
        '5 short stories of Hong Kong after ten years',
        'https://cdn.thestandnews.com/media/photos/cache/C2ABE58D81E5B9B4C2BB2020TEN20YEARS202012376056_562681027217993_303987522533359407_n_1024_xnYjN_1200x0.jpg',
        'https://www.youtube.com/watch?v=M4zebygSaZE'),
        
        ]
    def get_favorite_movies(self):
        return self.movies