import os


class Video:
    """Parent class used to hold information about any generic video"""

    RATINGS = ["G", "PG", "PG-13", "R"]   # valid ratings

    def __init__(self, title, duration, genre, year, description):
        """Constructor method for video class initialize a new instance of
        this class Parameters: video title, duration, genre, year,
        description """
        self.Title = title
        self.Duration = duration
        self.Genre = genre
        self.Year = year
        self.Description = description

    def show_video_info(self):
        """this function is responsible about displaying video information like :
        video title, duration, genre, release year, story line"""
        print("Video Title is: " + self.Title)
        print("Video Duration is: " + self.Duration)
        print("Video Genre is: " + self.Genre)
        print("Year of release: " + self.Year)
        print("Description: " + self.Description)


class Movie(Video):
    """Movie Class Used to express a movie object,
     holds attributes of movies"""

    def __init__(self, movie_title, movie_duration, movie_genre, movie_year,
                 movie_description,
                 movie_poster_image, movie_youtube_trailer):
        """Constructor method for Movie class initialize a new instance of
        this class, Parameters: Movie title, duration, genre, year,
        description, poster image, youtube trailer """
        Video.__init__(self, movie_title, movie_duration, movie_genre,
                       movie_year, movie_description)
        self.PosterImage = movie_poster_image
        self.YoutubeTrailer = movie_youtube_trailer

    def show_trailer(self):
        """this function is responsible about showing the movie trailer"""
        os.system("start chrome " + self.YoutubeTrailer)


class Series(Video):
    """Class Series Used to express series,
    holds information about the series. """
    def __init__(self,  series_title, series_duration, series_genre,
                 series_year, series_description,
                 series_episode_number, series_season,
                 series_poster_image, series_youtube_trailer):
        """Constructor method for Series class initialize a new instance of
                this class, Parameters: series title, duration, genre, year,
                description, episode number, season number,
                poster image, youtube trailer"""
        Video.__init__(self, series_title, series_duration,
                       series_genre, series_year, series_description)
        self.EpisodeNumber = series_episode_number
        self.Season = series_season
        self.PosterImage = series_poster_image
        self.YoutubeTrailer = series_youtube_trailer

    def show_trailer(self):
        """this function is responsible about showing the Series trailer"""
        os.system("start chrome " + self.YoutubeTrailer)

    def show_video_info(self):
        """this function is responsible about showing the Series information
        such that series title, duration, genre, release year, story line,
        episode number and season number"""
        print("series Title is: " + self.Title)
        print("series Duration is: " + self.Duration)
        print("series Genre is: " + self.Genre)
        print("Year of release: " + self.Year)
        print("Description: " + self.Description)
        print ("Episode Number: " + self.EpisodeNumber)
        print ("Season: " + self.Season)
