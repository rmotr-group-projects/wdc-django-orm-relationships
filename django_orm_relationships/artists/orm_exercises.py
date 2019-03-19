from artists.models import Artist, Song


def task_1_artist_exists():
    """Should return True if there's any artist called Eric Clapton, or False otherwise"""
    # HINT: Use .exists() function
    if_real = Artist.objects.filter(artistic_name='Eric Clapton').exists()
    if if_real:
        return True
    return False


def task_2_first_song_ordered():
    """Should return the first Song ordered by title"""
    # HINT: Use .first() function
    first_song = Song.objects.all().order_by('title').first()
    return first_song


def task_3_last_artist_ordered():
    """Should return the last Artist ordered by artistic_name"""
    # HINT: Use .last() function
    last_song = Artist.objects.all().order_by('artistic_name').last()
    return last_song


def task_4_artist_songs_contains():
    """Should return all songs from artist whose artistic names contains the letter K"""
    # HINT: use double underscores "__" to navigate through model's FKs and fields
    songs_with_k = Song.objects.filter(artist__artistic_name__icontains = 'k')
    return songs_with_k

def task_5_songs_exclude():
    """Should return all songs excluding the ones that contains the word 'Thrill' in its title"""
    # HINT: Use .exclude() function
    songs_without_thrill = Song.objects.exclude(title__icontains="thrill")
    return songs_without_thrill


def task_6_artist_name_starts_with():
    """Should return the amount of artists whose artistic name starts with the pattern 'Ji'"""
    # HINT: Use __startswith field lookup and .count() function
    return Artist.objects.filter(artistic_name__istartswith = 'Ji').count()


def task_7_get_or_create_artist():
    """
        Should check if Artist 'Eric Clapton' exists in the DB and create it if
        it doesn't. Return True if you had to create, or False otherwise.
    """
    # HINT: Use django `get_or_create()` function
    obj, created = Artist.objects.get_or_create(
        artistic_name='Eric Clapton',
        first_name = "Eric",
        last_name = "Clapton",
        popularity = 5,
        )
    return created

def task_8_artist_songs_reverse_relationship():
    """Should return all songs from artist Stevie Wonders using reverse relationships"""
    # step 1: get Artist "Stevie Wonders"
    artist = Artist.objects.get(artistic_name = 'Stevie Wonders')

    # step 2: return all songs from that artist using .song_set reverse relationship
    return artist.song_set.all()


def task_9_update_song_artist():
    """Should create a new Artist and assign it as the owner of the song called Superstition"""
    # step 1: create the artist
    new_artist = Artist.objects.create(
        artistic_name='Jon Flow',
        first_name = "Jon",
        last_name = "Flow",
        popularity = 5,
        )
    superstition = Song.objects.get(title='Superstition')
    superstition.artist = new_artist
    superstition.save()
