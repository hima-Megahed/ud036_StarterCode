import Backend
import fresh_tomatoes


# IT Movie: movie title, duration, genre, release year, story line,
# poster image, movie trailer
IT = Backend.Movie(
    "IT",
    "2 HR 15 MIN",
    "Horror",
    2017,
    "New Line Cinema's horror thriller IT",
    "https://pre00.deviantart.net/370c/th/pre/i/2017/221/c/3/it_poster_fanart_by_sixfrid-dbjiauq.jpg",  # NOQA
    "https://www.youtube.com/watch?v=7no56Zw1e20"
                   )


# Despicable Me 3 Movie: movie title, duration, genre, release year,
# story line, poster image, movie trailer
Despicable_Me_3 = Backend.Movie(
    "Despicable Me 3",
    "50 MIN",
    "Animation",
    2017,
    "The mischievous Minions hope that Gru will return to a life",
    "https://cdn.traileraddict.com/content/universal-pictures/despicable-me-3-7.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6DBi41reeF0"
                                )
# Game Of Thrones Series: series title, duration, genre, release year,
# story line, episode number, season number, poster image, series trailer
GOT_s1_ep1 = Backend.Series(
    "Game of Thrones",
    "40 MIN",
    "History-Fantasy-Drama",
    2011,
    "Game of Thrones is an American fantasy drama television series"
    " created by David Benioff",
    1,
    1,
    "https://i.pinimg.com/originals/44/d1/12/44d11294463706317b9abc620e8c7c4b.jpg",  # NOQA
    "https://www.youtube.com/watch?v=522l0YE9hRQ"
                            )

# DunKirk Movie: movie title, duration, genre, release year,
# story line, poster image, movie trailer
DunKirk = Backend.Movie(
    "DunKirk",
    "1 HR 46 MIN",
    "Drama",
    2017,
    "DUNKIRK opens as hundreds of thousands of British and Allied troops"
    " are surrounded by enemy forces.",
    "http://www.shockmansion.com/wp-content/myimages/2016/12/fy.jpg",
    "https://www.youtube.com/watch?v=F-eMt3SrfFU"
                        )


# Spider-Man: Homecoming (2017) Movie: movie title, duration, genre,
# release year, story line, poster image, movie trailer
Spider_Man_Homecoming = Backend.Movie(
    "Spider-Man: Homecoming (2017)",
    "2 HR 21 MIN",
    "Action - Adventure - Sci-Fi",
    2017,
    "Peter Parker tries to balance his "
    "life as an ordinary high school student in Queens with his superhero"
    " alter-ego Spider-Man, and must confront a new menace prowling the "
    "skies of New York City.",
    "https://cdn.flickeringmyth.com/wp-content/uploads/2017/07/819BtiNYaHL._SL1500_-600x600.jpg",  # NOQA
    "https://www.youtube.com/watch?v=U0D3AOldjMU"

                                      )

# Leap! (2016) Movie: movie title, duration, genre,
# release year, story line, poster image, movie trailer
Leap = Backend.Movie(
    "Leap! (2016)",
    "1 HR 48 MIN",
    "Animation - Comedy - Family",
    2017,
    "An orphan girl dreams of becoming a ballerina and flees"
    " her rural Brittany for Paris, where she"
    " passes for someone else and accedes to the position"
    " of pupil at the Grand Opera house.",
    "http://i1.wp.com/www.wearemoviegeeks.com/wp-content/uploads/LEAP_TEASER_27x40_R5212.jpg?resize=560%2C830",  # NOQA
    "https://www.youtube.com/watch?v=h-huA2o6OOY"
                     )

Movies = [
    IT,
    Despicable_Me_3,
    GOT_s1_ep1,
    DunKirk,
    Spider_Man_Homecoming,
    Leap]
fresh_tomatoes.open_movies_page(Movies)
