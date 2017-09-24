import os


class Video:
    RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, genre, year, description):
        self.Title = title
        self.Duration = duration
        self.Genre = genre
        self.Year = year
        self.Description = description

    def show_video_info(self):
        print("Video Title is: "+ self.Title)
        print("Video Duration is: "+ self.Duration)
        print("Video Genre is: "+ self.Genre)
        print("Year of release: "+ self.Year)
        print("Description: "+ self.Description)


class Movie(Video):
    def __init__(self, movie_title, movie_duration, movie_genre, movie_year, movie_description,
                 movie_poster_image, movie_youtube_trailer):
        Video.__init__(self,movie_title,movie_duration,movie_genre,movie_year,movie_description)
        self.PosterImage = movie_poster_image
        self.YoutubeTrailer = movie_youtube_trailer

    def show_trailer(self):
        os.system("start chrome "+ self.YoutubeTrailer)


class Series(Video):
    def __init__(self,  series_title, series_duration, series_genre, series_year, series_description,
                 series_episode_number, series_season, series_poster_image, series_youtube_trailer):
        Video.__init__(self, series_title, series_duration, series_genre, series_year, series_description)
        self.EpisodeNumber = series_episode_number
        self.Season = series_season
        self.PosterImage = series_poster_image
        self.YoutubeTrailer = series_youtube_trailer

    def show_trailer(self):
        os.system("start chrome "+ self.YoutubeTrailer)

    def show_video_info(self):
        print("Video Title is: " + self.Title)
        print("Video Duration is: " + self.Duration)
        print("Video Genre is: " + self.Genre)
        print("Year of release: " + self.Year)
        print("Description: " + self.Description)
        print ("Episode Number: " + self.EpisodeNumber)
        print ("Season: " + self.Season)