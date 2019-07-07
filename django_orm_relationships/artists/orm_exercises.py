from django.shortcuts import get_object_or_404

from artists.models import Artist, Song


def task_1_artist_exists():
    """Should return True if there's any artist called Eric Clapton, or False otherwise"""
    return Artist.objects.filter(artistic_name__iexact='eric clapton').exists()


def task_2_first_song_ordered():
    """Should return the first Song ordered by title"""
    return Song.objects.order_by('title').first()


def task_3_last_artist_ordered():
    """Should return the last Artist ordered by artistic_name"""
    return Artist.objects.order_by('artistic_name').last()


def task_4_artist_songs_contains():
    """Should return all songs from artist whose artistic names contains the letter K"""
    return Song.objects.filter(artist__artistic_name__icontains='k')


def task_5_songs_exclude():
    """Should return all songs excluding the ones that contains the word 'Thrill' in its title"""
    return Song.objects.exclude(title__icontains='thrill')


def task_6_artist_name_starts_with():
    """Should return the amount of artists whose artistic name starts with the pattern 'Ji'"""
    return Artist.objects.filter(artistic_name__startswith='Ji').count()


def task_7_get_or_create_artist():
    """
        Should check if Artist 'Eric Clapton' exists in the DB and create it if
        it doesn't. Return True if you had to create, or False otherwise.
    """
    return Artist.objects.get_or_create(artistic_name__iexact='Eric Clapton', 
                                        defaults={'artistic_name': 'Eric Clapton', 'popularity': 60})[1]


def task_8_artist_songs_reverse_relationship():
    """Should return all songs from artist Stevie Wonders using reverse relationships"""
    # step 1: get Artist "Stevie Wonders"
    artist = get_object_or_404(Artist, artistic_name__iexact='stevie wonders')

    # step 2: return all songs from that artist using .song_set reverse relationship
    return artist.song_set.all()


def task_9_update_song_artist():
    """Should create a new Artist and assign it as the owner of the song called Superstition"""
    # step 1: create the artist
    artist = Artist.objects.create(artistic_name='Dude', popularity=99)
    artist.save()

    # step 2: get the song called 'Superstition'
    song = get_object_or_404(Song, title__iexact='superstition')

    # step 3: assign created artist to the song and save() the song model
    song.artist = artist
    song.save()
