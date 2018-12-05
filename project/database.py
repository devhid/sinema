from .movie_data import get_movie_info
from .models import person, movie, actors, writers, directors, genres
import time

imdb_ids = "tt0120663,tt0062622,tt4912910,tt3532216,tt2345759,\
            tt3393786,tt1631867,tt1229238,tt0325710,tt4881806,\
            tt4154756,tt3896198,tt1355644,tt2404435,tt0369610,\
            tt2015381,tt0493464,tt0901476,tt1078885,tt5523010,\
            tt3110958,tt3300542,tt2637276,tt1490017,tt2872732,\
            tt2302755,tt1345836,tt1057500,tt0468569,tt0493464,\
            tt0499603,tt0315327,tt2250912,tt3498820,tt2395427,\
            tt1300854,tt0848228,tt1515091,tt1228705,tt0371746,\
            tt0069049,tt0099381,tt0192528,tt0193747,tt0253093,\
            tt0258112,tt0276568,tt0360556,tt0365545,tt0427543,\
            tt0108052,tt0083866,tt0082971,tt3778644,tt3748528,\
            tt0319343,tt1386588,tt0838283,tt1772341,tt0371746,\
            tt1228705,tt1300854,tt0443453,tt2582846,tt0989757,\
            tt1099212,tt1702439,tt0468569,tt1375666,tt0172495,\
            tt0120815,tt1345836,tt0133093,tt0499549,tt0988045,\
            tt5215952,tt0289043,tt1139797,tt5700672,tt1457767,\
            tt6644200,tt3235888,tt1591095,tt0088247,tt0096754,\
            tt0120338,tt0082910,tt0111503,tt0103064,tt6019206,\
            tt3460252,tt0361748,tt1853728,tt1028528,tt0108399,\
            tt0490215,tt0993846,tt1130884,tt0970179,tt0407887,\
            tt0338751,tt0217505,tt0163988,tt0081505,tt0093058,\
            tt0432010,tt0825334,tt0859635,tt0862930,tt0933876,\
            tt0972544,tt1034415,tt1072748,tt1127881,tt1137450,\
            tt1213641,tt1226837,tt1235187,tt1259528,tt1270797,\
            tt1273221,tt1285009,tt1289403,tt1308728,tt1310655,\
            tt1318517,tt1319706,tt1326219,tt1329350,tt1337180,\
            tt1352771,tt1365519,tt1389098,tt1413492,tt1458902,\
            tt1464763,tt1477834,tt1493881,tt1502407,tt1508012,\
            tt1517451,tt1524931,tt1525916,tt1537408,tt1563742,\
            tt1590193,tt1592253,tt1620680,tt1662546,tt1677720,\
            tt1682886,tt1682956,tt1690967,tt1703123,tt1713991,\
            tt1727254,tt1727824,tt1737110,tt1739287,tt1754316,\
            tt1754650,tt1754700,tt1759744,tt1765679,tt1772399,\
            tt1773753,tt1780790,tt1787907,tt1794951,tt1799516,\
            tt1801552,tt1825683,tt1826956,tt1838708,tt1842422,\
            tt1843303,tt1846589,tt1849772,tt1851941,tt1855144,\
            tt1858788,tt1859618,tt1884378,tt1885322,tt1885325,\
            tt1922544,tt1934372,tt1934452,tt1937340,tt1954426,\
            tt1971310,tt1977094,tt1986097,tt1999130,tt1999890,\
            tt2006291,tt2006291,tt2011311,tt2018069,tt2034176,\
            tt2035623,tt2043993,tt2050452,tt2051958,tt2060503,\
            tt2069797,tt2071462,tt2081306,tt2091245,tt2098669,\
            tt2119543,tt2126357,tt2137471,tt2139845,tt2140629,\
            tt2150177,tt2160105,tt2179171,tt2179231,tt2180583,\
            tt2181791,tt2200866,tt2201211,tt2205762,tt2211054,\
            tt2221755,tt2226440,tt2231461,tt2233979,tt2237324,\
            tt2239876,tt2243900,tt2262044,tt2265630,tt2268018,\
            tt2278050,tt2281442,tt2290597,tt2294755,tt2296777,\
            tt2312748,tt2315596,tt2316329,tt2316479,tt2319991,\
            tt2328900,tt2348330,tt2354065,tt2368254,tt2371900,\
            tt2372251,tt2377752,tt2386237,tt2388629,tt2392748,\
            tt2395271,tt2397617,tt2399430,tt2400382,tt2401814,\
            tt2401825,tt2402114,tt2402578,tt2404639,tt2413014,\
            tt2445568,tt2448130,tt2459244,tt2463842,tt2470060,\
            tt2478478,tt2482856,tt2488250,tt2488550,tt2488666,\
            tt2490148,tt2530316,tt2531120,tt2531344,tt2534642,\
            tt2548396,tt2549556,tt2551330,tt2556640,tt2557478,\
            tt2564088,tt2570500,tt2577636,tt2578538,tt2606314,\
            tt2615132,tt2619512,tt2639336,tt2647424,tt2651724".split(',')


def populate_database(db):
    for imdbid in set(imdb_ids):
        movie_info = get_movie_info(imdbid=imdbid)

        if not movie_info: continue

        m_movie = add_movie(db, movie_info)
        movie_id = m_movie.movie_id

        for genre in movie_info['genres']:
            add_genre(db, genre, movie_id)
        
        all_people = movie_info['actors'] + movie_info['writers'] + [movie_info['director']]

        for p in all_people:
            person_sql = person.Person.query.filter_by(first_name=p[0], last_name=p[1])

            if(person_sql.count() >= 1):
                person_sql = person_sql.first()
            else:
                person_sql = add_person(db, p[0], p[1])
            
            person_id = person_sql.person_id

            if p in movie_info['actors']:
                person_sql.is_actor = True

                if actors.Actors.query.filter_by(actor_id=person_id, movie_id=movie_id).count() == 0:
                    add_actor(db, person_id, movie_id)
            
            if p in movie_info['writers']:
                person_sql.is_writer = True

                if writers.Writers.query.filter_by(writer_id=person_id, movie_id=movie_id).count() == 0:
                    add_writer(db, person_id, movie_id)
            
            if p[0] == movie_info['director'][0] and p[1] == movie_info['director'][1]:
                person_sql.is_director = True

                if directors.Directors.query.filter_by(director_id=person_id, movie_id=movie_id).count() == 0:
                    add_director(db, person_id, movie_id)

def add_movie(db, movie_info):
    new_movie = movie.Movie(
        movie_name=movie_info['movie_name'],
        synopsis=movie_info['synopsis'],
        rating=movie_info['rating'],
        minutes_duration=movie_info['duration'],
        release_date=movie_info['release_date'],
        maturity_rating=movie_info['maturity_rating'],
        movie_art_url=movie_info['movie_art_url']
    )

    db.session.add(new_movie)
    db.session.commit()

    return new_movie

def add_genre(db, genre, movie_id):
    if not validate_genre(genre): return

    new_genre = genres.Genres(
        movie_id=movie_id,
        genre=genre
    )

    db.session.add(new_genre)
    db.session.commit()

    return new_genre

def add_person(db, first_name, last_name):
    new_person = person.Person(
        first_name=first_name,
        last_name=last_name
    )

    db.session.add(new_person)
    db.session.commit()

    return new_person

def add_actor(db, person_id, movie_id):
    new_actor = actors.Actors(
        actor_id=person_id,
        movie_id=movie_id
    )

    db.session.add(new_actor)
    db.session.commit()

    return new_actor

def add_director(db, person_id, movie_id):
    new_director = directors.Directors(
        director_id=person_id,
        movie_id=movie_id
    )

    db.session.add(new_director)
    db.session.commit()

    return new_director

def add_writer(db, person_id, movie_id):
    new_writer = writers.Writers(
        writer_id=person_id,
        movie_id=movie_id
    )

    db.session.add(new_writer)
    db.session.commit()

    return new_writer

def validate_genre(genre):
    return genre in genres.get_genres()