from artists.models import Artist, Song


def task_1_artist_exists():
    return True if Artist.objects.filter(artistic_name__icontains = 'Eric Clapton').exists() else False 

def task_2_first_song_ordered(): 
    return Song.objects.all().order_by('title').first()

def task_3_last_artist_ordered():
    return Artist.objects.all().order_by('-artistic_name').first()
  
def task_4_artist_songs_contains():
    return Song.objects.filter(artist__artistic_name__icontains = 'K')
    
def task_5_songs_exclude():
    return Song.objects.exclude(title__icontains = 'Thrill')
   
def task_6_artist_name_starts_with():
    return Artist.objects.filter(artistic_name__startswith = 'Ji').count()
   

def task_7_get_or_create_artist():
    
    if Artist.objects.filter(artistic_name__icontains='Eric Clapton').exists():
        return False
    
    else:
        Artist.objects.create(first_name = 'Eric',
                            last_name = 'Clapton',
                             artistic_name = 'Eric Clapton',
                              picture_url = 'http://Eric_Clapton.com',
                              popularity = 10,
                              genre = 'Rock'
                             )
        return True 
       

def task_8_artist_songs_reverse_relationship():
    """Should return all songs from artist Stevie Wonders using reverse relationships"""
    # step 1: get Artist "Stevie Wonders"
    artist = Artist.objects.get(artistic_name = 'Stevie Wonders')

    return artist.song_set.all()


def task_9_update_song_artist():
    """Should create a new Artist and assign it as the owner of the song called Superstition"""
    # step 1: create the artist
    artist = Artist.objects.create(first_name = 'Tom',
                            last_name = 'King',
                             artistic_name = 'Tom King',
                              picture_url = 'http://Tom_King.com',
                              popularity = 10,
                              genre = 'Blues'
                             )

    # step 2: get the song called 'Superstition'
    song = Song.objects.get(title = 'Superstition')

    # step 3: assign created artist to the song and save() the song model
    
    
    song.artist = artist
    song.save()
   
                                   
