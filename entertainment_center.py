import fresh_tomatoes
import media

the_dark_knight = media.Movie("The Dark Knight", "You either die a hero or live long enough to see yourself become the villain.",
                            "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=EXeTwQWrcwY","2008",
                            "Christopher Nolan",
                            "Christian Bale, Heath Ledger, Michael Caine, Aaron Eckhart")

kungfu_panda = media.Movie("KungFu Panda", "There is no secret ingredient to become a master.",
                           "http://ia.media-imdb.com/images/M/MV5BMTIxOTY1NjUyN15BMl5BanBnXkFtZTcwMjMxMDk1MQ@@._V1_.jpg",
                           "https://www.youtube.com/watch?v=PXi3Mv6KMzY","2008",
                           "Mark Osborne, John Stevenson",
                           "Jack Black, Ian McShane, Angelina Jolie Pitt")


Enchanted = media.Movie("Enchanted", "Even a fantasy princess is slapped awake by reality.",
                        "http://ia.media-imdb.com/images/M/MV5BMjE4NDQ2Mjc0OF5BMl5BanBnXkFtZTcwNzQ2NDE1MQ@@._V1_.jpg",
                        "https://www.youtube.com/watch?v=uW6dNiOIOhA","2007",
                        "Kevin Lima",
                        "Amy Adams,Susan Sarandon,James Marsden")

mean_girls = media.Movie("Mean Girls", "An all-time classic movie.",
                         "http://ia.media-imdb.com/images/M/MV5BMjE1MDQ4MjI1OV5BMl5BanBnXkFtZTcwNzcwODAzMw@@._V1_SY1000_CR0,0,706,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=KAOmTMCtGkI","2004",
                         "Mark Waters",
                         "Rachel McAdams,Lindsay Lohan,Lizzy Caplan,Amanda Seyfried,Lacey Chebert")

lotr_trilogy = media.Movie("The Lord of the Rings", "One trilogy to rule them all.",
                           "http://vignette1.wikia.nocookie.net/lotr/images/8/87/Ringstrilogyposter.jpg/revision/latest?cb=20070806215413",
                           "https://www.youtube.com/watch?v=ddmcFDoCAq8","2001",
                           "Peter Jackson",
                           "My childhood")

avengers = media.Movie("The Avengers", "The unofficial Iron Man 3.",
                       "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8","2012",
                       "Joss Whedon",
                       "Robert Downey Jr,Scarlett Johannsson, Hulk-smash, Puny God")

movies = [the_dark_knight, kungfu_panda, Enchanted, mean_girls, lotr_trilogy, avengers]
fresh_tomatoes.open_movies_page(movies)

