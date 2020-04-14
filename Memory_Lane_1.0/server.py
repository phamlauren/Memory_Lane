from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 30
tracks = [ 
    {
        "id": 1,
        "title": "Take A Chance On Me",
        "artist":  [
                {
                    "name": "ABBA",
                    "mark_as_deleted": False,
                },
            ],
        "album": "The Album",
        "year_released": 1977,
        "description": "My mother has always loved ABBA and has played their music for me ever since I was little. However, the group took on a new, personal meaning for me when my friends and I watched the movie Mamma Mia for my fourth grade birthday party. Unfortunately my immigrant mother did not know that Mamma Mia was not quite appropriate for fourth graders. Now I love staying in and getting wine drunk while singing ABBA with my gal pals and anyone who thinks Mamma Mia 2 was't good can fight me.",
        "category": "Songs to dance to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/2/2a/Take_a_Chance_on_Me_%28Abba_single%29_coverart.jpg",  
    },
    {
        "id": 2,
        "title": "I Don't Wanna See You Cryin' Anymore",
        "artist": [
                {
                    "name": "Adam Melchor",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Plan On You",
        "year_released": 2019,
        "description": "One of my best friends Uwa introduced me to Adam Melchor. He's a dreamy New Jersey native, former Brooklyn transplant and now a budding artist living his dream in LA, like we'd all like to do if we were talented and lucky enough. This song reminds me of a love story I once read and is more normal to play for people than another track on Adam's album called Cryin' Interlude. Otherwise I probably would have put Cryin' Interlude in this list.",
        "category": "Songs to cry to", 
        "media_link": "https://images.genius.com/3b26b10c24c0965ce197017d237b6353.1000x1000x1.jpg",
    },
    {
        "id": 3,
        "title": "Cherry Blossom",
        "artist": [
                {
                    "name": "ALA.NI",
                    "mark_as_deleted": False,
                },
            ],
        "album": "You & I",
        "year_released": 2017,
        "description": "My roommate Saskia sent me this song the other day. It's super dreamy, reminiscient of twentieth century jazz like Jane Morgan and Ella Fitzgerald. Unfortunately the rest of ALA.NI's album is not as good as Cherry Blossoms, or it is at least too different from Cherry Blossoms.",
        "category": "Songs to fall in love to", 
        "media_link": "https://media.npr.org/assets/img/2017/05/26/Ala.Ni_CVR_sq-e89c7023497964eac10dde6651a092dd4f04c48a-s800-c85.jpg",
    },
    {
        "id": 4,
        "title": "Strange Land",
        "artist":  [
                {
                    "name": "88rising",
                    "mark_as_deleted": False,
                },
                {
                    "name": "NIKI",
                    "mark_as_deleted": False,
                },
                {
                    "name": "Phum Viphurit",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Head In the Clouds II",
        "year_released": 2019,
        "description": "I made some new friends earlier this year who are way too cool to be my friends. They're mostly Asian-Americans who are from Cali, which is where all the cool Asian-Americans are from. I think it is because there are enough Asian-Americans there that they have created an Asian-American culture and identity. Anyways, this song began my journey into Asian and Asian-American R&B and hip hop, and I love it.",
        "category": "Songs to dream to", 
        "media_link": "https://images.genius.com/c13ed8e93bdcda79933c75eba9a5a544.696x696x1.png",
    },
    {
        "id": 5,
        "title": "We Don't Deserve Love",
        "artist": [
                {
                    "name": "Arcade Fire",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Everything Now",
        "year_released": 2017,
        "description": "I've known this song ever since Everything Now came out and I haven't really been listening to it recently, but I chose it because I wanted to demonstrate how to use the category data sort of like a playlist. And who doesn't have a playlist of angsty music, and whose angsty playlist music doesn't include Arcade Fire? No one's, because if Arcade Fire isn't there, then it's not really angsty.",
        "category": "Songs to feel angst to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/0/0e/Everything_Now_Arcade_Fire.jpg",
    },
    {
        "id": 6,
        "title": "Goodmorning",
        "artist": [
                {
                    "name": "Bleachers",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Gone Now",
        "year_released": 2017,
        "description": "I really clung onto Bleachers' first album when I was in Berkeley for a summer, and eagerly awaited this ablum. Jack Antonoff is a New Jersey native, so it was really special to experience this album while moving to New York. Now it's sort of a ritual for me to listen to Gone Now in order and from start to finish every time I get onto the M60 SBS at LaGuardia and head back to Morningside Heights.",
        "category": "Songs to drive out west to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/5/51/Bleachers-gone-now-cover.jpg",
    },
        {
        "id": 7,
        "title": "You Might Be Sleeping",
        "artist": [
                {
                    "name": "Clairo",
                    "mark_as_deleted": False,
                },
                {
                    "name": "Jakob Ogawa",
                    "mark_as_deleted": False,
                }
            ],
        "album": "Bedroom Tapes",
        "year_released": 2017,
        "description": "I have been doing a lot of traveling ever since moving to New York, and I found this song on one of Spotify's Release Radios for me a few months ago. One morning I was flying early from somewhere and I landed in Newark, and it was so early and everyone else was still in bed or waking up for their 840 class that I thought of this song while waiting for the Air Train at Newark Airport and decided to blast this song. It felt right.",
        "category": "Songs to dream to", 
        "media_link": "https://images.genius.com/58ba5e06b932b5a68e1f0b3da51e0137.600x600x1.jpg",
    },
    {
        "id": 8,
        "title": "Changes",
        "artist": [
                {
                    "name": "David Bowie",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Hunky Dory",
        "year_released": 1971,
        "description": "Are you really going to admit that you heard this song from Shrek 2, Lauren? I mean, come on. Do you even know yourself? Of course you will. Because you love Shreak 2.", ## This song is one of my favorites of all time. If we're being honest my parents were immigrants and I didn't know much about Bowie until I got older and started exploring music for myself. The first time I heard this song was covered by some chick in the Shrek 2 soundtrack. But the lyrics and the buildup of the song stuck to me from childhood and a few years ago I found out it was really Bowie's song. The last few weeks of my sophomore spring I was listening to this song on repeat with pep in my step and ready to get out of New York for the summer.
        "category": "Songs to drive out west to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/4/40/David_Bowie_-_Hunky_Dory.jpg",
    },
    {
        "id": 9,
        "title": "Heart Killer",
        "artist": [
                {
                    "name": "Dr. Dog",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Critical Equation",
        "year_released": 2018,
        "description": "My senior year of high school I started getting into music that was more like Dr. Dog, Shakey Graves, etc. - really dreaming about driving out west. The first song I loved by Dr. Dog was called Nellie and I played it for my family on the speaker on our boat on Lake Michigan. This song is so good for a drive up to Traverse City, and I'm sure it will be just as good when I finally make that drive out west some day.",
        "category": "Songs to drive out west to", 
        "media_link": "https://images-na.ssl-images-amazon.com/images/I/71hZZu%2Ba8AL._SL1500_.jpg",
    },
    {
        "id": 10,
        "title": "Dollar",
        "artist": [
                {
                    "name": "Electric Guest",
                    "mark_as_deleted": False,
                },
            ],
        "album": "KIN",
        "year_released": 2019,
        "description": "My older brother introduced me to Electric Guest with the song Waves in 2014. Since then I've grown to love them more than he did. I even saw them and briefly fell into infatuation with Asa Taccone at the Music Hall of Williamsburg my freshman year. I was also offered an alcoholic drink without being ID'd for the first time ever at that concert.",
        "category": "Songs to dance to", 
        "media_link": "https://i2.wp.com/cornellsun.com/wp-content/uploads/2019/10/4e24dc6fad18bdc4f7145be139d663e8.750x750x1.jpg?w=750",
    },
    {
        "id": 11,
        "title": "Super Rich Kids",
        "artist": [
                {
                    "name": "Frank Ocean",
                    "mark_as_deleted": False,
                },
                {
                    "name": "Earl Sweatshirt",
                    "mark_as_deleted": False,
                }
            ],
        "album": "channel ORANGE",
        "year_released": 2012,
        "description": "I hadn't listened to this song in awhile but while looking for songs decided it would fit well into the angst playlist. One of my best friends from high school named Frankie got me hooked on Frank Ocean - although my friends Evan and Maya from middle school had listened to him before then. In eleventh grade I moved to boarding school after spending my whole life in public school and my first week at boarding shcool I listened to this song on repeat.",
        "category": "Songs to feel angst to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/2/28/Channel_ORANGE.jpg",
    },
    {
        "id": 12,
        "title": "The Beautiful Dream",
        "artist": [
                {
                    "name": "George Ezra",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Staying at Tamara's",
        "year_released": 2018,
        "description": "I found George Ezra just like everyone else did through his hit single Budapest, but I love him beyond that now. I went to Ireland in July of 2018 and as I traveled through Ireland I listened to George sing me into adventure. Ireland was such a beautiful dream - and indeed I have so many more beautiful dreams listening to him.",
        "category": "Songs to dream to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/2/2c/Staying_at_Tamara%27s_%28album%29.png",
    },
    {
        "id": 13,
        "title": "Suitcase Full of Sparks",
        "artist": [
                {
                    "name": "Gregory Alan Isakov",
                    "mark_as_deleted": False,
                },
            ],
        "album": "The Weatherman",
        "year_released": 2013,
        "description": "Gregory Alan Isakov is my artist of the decade according to Spotify and I would have put a million dollars on him if I had to guess that it would be him. His music breathes life into my soul. One of the best nights of my life was going to see him at Warsaw in Brooklyn. Saskia and I went early so that we were at the very front of the audience, and we were - just leaning over the railing. One day I'll listen to him play near his home in Colorado.",
        "category": "Songs to drive out west to", 
        "media_link": "https://m.media-amazon.com/images/I/71L4-sL9MsL._SS500_.jpg",
    },
    {
        "id": 14,
        "title": "Canyon Moon",
        "artist": [
                {
                    "name": "Harry Styles",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Fine Line",
        "year_released": 2019,
        "description": "I am not ashamed to like things that are popular, even though I will say that I think some of my artistic taste is not average. I went to the Grand Canyon for the first time earlier this year and took a video there for my Instagram story. I stole the idea to use this song as the background from my friend Astrid who was also there. I almost entertained the idea of going to the Today Show early before 5am last week to see Harry's performance, but that moment disappeared real quick.",
        "category": "Songs to drive out west to", 
        "media_link": "https://media.pitchfork.com/photos/5df3f10129131e0008fbae41/1:1/w_320/Harry-Styles.jpg",
    },
    {
        "id": 15,
        "title": "Bambi",
        "artist": [
                {
                    "name": "Hippo Campus",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Bambi",
        "year_released": 2018,
        "description": "Sophomore year was tough. That was the year of my greatest angst, the year I felt the most like a teenager, like a lost girl. That this song was most played for my sophomore year really tells you what I was like - \"I haven't been much myself and I feel like my friends are being put through this hell I'm feeling I think that I'm living, if you could call it living - so brash and unforgiving ruled by this vibe I'm bringing, serving myself.\" YIKES.",
        "category": "Songs to feel angst to", 
        "media_link": "https://imagescdn.juno.co.uk/full/CS707607-01A-BIG.jpg",
    },
    {
        "id": 16,
        "title": "Honey Slider",
        "artist": [
                {
                    "name": "Houndmouth",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Little Neon Limelight",
        "year_released": 2016,
        "description": "I needed to make my drive playlist longer so this song definitely came to mind. One of my best friends with whom I had a falling out shared the song Darlin' by Houndmouth with me, and I loved the sound but needed something different so quick. I immediately came to love this song. Imagine a 17-year-old girl driving her 1998 Acura RL through the beautiful state of Michigan accompanied by this song and the fresh breeze.",
        "category": "Songs to drive out west to", 
        "media_link": "https://images-na.ssl-images-amazon.com/images/I/71ikShYQQXL._SL1200_.jpg",
    },
    {
        "id": 17,
        "title": "Stormi",
        "artist": [
                {
                    "name": "Isonouncane",
                    "mark_as_deleted": False,
                },
            ],
        "album": "DIE",
        "year_released": 2016,
        "description": "I actually kind of think I might replace this song with one that is more meaningful to me but I feel like it doesn't have that much meaning yet because I was just introduced to this song. They're Italian. And it does represent more of me in that I love listening to music from different countries or with words in languages other than English - Icelandic music like Sigur Ros and Kaleo, Brazilian music like Rodrigo Amarante (featured later), etc. This is a beach song for sure.",
        "category": "Songs to dance to", 
        "media_link": "https://images-na.ssl-images-amazon.com/images/I/61xdIhmS3qL._SX342_QL70_.jpg",
    },
    {
        "id": 18,
        "title": "ATTENTION",
        "artist": [
                {
                    "name": "JOJI",
                    "mark_as_deleted": False,
                },
            ],
        "album": "BALLADS 1",
        "year_released": 2018,
        "description": "JOJI is almost too popular for me to love, so it's a good thing that I admitted earlier that I have no problem with loving what's popular. He's Australian-Japanese who went to NYU and lives probably in LA now. This song describes how I feel so many times. And honestly I understand why sometimes guys tell me that I'm unapproachable. A lot of the times I just don't want to be approached. \"When you cry you waste your time over boys you never liked.\" Gosh, how obnoxious can I be?",
        "category": "Songs to feel angst to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/thumb/6/6a/Joji_–_Ballads_1.png/220px-Joji_–_Ballads_1.png",
    },
    {
        "id": 19,
        "title": "Healah Dancing (feat. Ren Ford)",
        "artist": [
                {
                    "name": "Keaton Henson",
                    "mark_as_deleted": False,
                },
                {
                    "name": "Ren Ford",
                    "mark_as_deleted": False,
                }
            ],
        "album": "Romantic Works",
        "year_released": 2014,
        "description": "I fell in love with this song while walking through Cranbrook Kingswood's campus. Surpisingly enough I met a girl in one of my classes named Sarah who also loves Keaton Henson. This song is one of my favorites of all time, and listening to it always makes me feel like myself. I like sad music. Surprise there.",
        "category": "Songs to fall in love to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/c/c3/Romantic_works.jpg",
    },
    {
        "id": 20,
        "title": "Paris 12",
        "artist": [
                {
                    "name": "Linying",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Paris 12",
        "year_released": 2016,
        "description": "I'm happy with the number of Asian and Asian-American songs that are making it on this small list of 30. Linying is from Singapore and I love her voice. She also recently did a cover of Frank Ocean's Self-Control which was beautiful. I've been to Paris and this song doesn't really feel like Paris to me, but it feels like a place that I've been to and in other than Paris and that's an interesting place for me. So I listen to this song and I go there and it feels like silk and marble.",
        "category": "Songs to dream to", 
        "media_link": "https://images.genius.com/4388cee7ae305ef7c00685b0864212c0.619x619x1.png",
    },
    {
        "id": 21,
        "title": "With Strangers",
        "artist": [
                {
                    "name": "Little Joy",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Little Joy",
        "year_released": 2008,
        "description": "The song Brand New Start by Little Joy was recommended to me by Spotify at some point and that's a great song too, but it's so different from this one and I was obsessed with this one at the end of my sophomore year. Little Joy was just a side project of Rodrigo Amarante's and some of his friends so unfortunately I can't get more of this song, but some of Rodrigo's solo stuff is good too.",
        "category": "Songs to cry to", 
        "media_link": "https://media.pitchfork.com/photos/5929bddcea9e61561daa77c8/1:1/w_320/33bc5796.jpg",
    },
    {
        "id": 22,
        "title": "Another Wave From You",
        "artist": [
                {
                    "name": "M83",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Hurry Up, We're Dreaming",
        "year_released": 2011,
        "description": "My favorite memory of listening to M83 is in the car with my father who came to pick me up from boarding school and was driving me home for break. He briefly had a nice car, some sort of BMW, which he needed for work and later returned deciding that it wasn't really something we could afford. But that was the trip that I realized that I had missed the sound of my father's voice which had been background to most of my life since he was always on the phone for work. Anyways, M83 has transported me to so many places deep in my soul and I will always love and return to this album.",
        "category": "Songs to dream to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/4/46/M83-Hurry-Up-Were-Dreaming.jpg",
    },
    {
        "id": 23,
        "title": "Funky Duck",
        "artist": [
                {
                    "name": "Vulfpeck",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Thrill of the Arts",
        "year_released": 2015,
        "description": "Vulfpeck was also unsurprisingly my artist of the year. I've known them in their hit single Back Pocket which I heard on a trip with some earth science kids to Death Valley National Park during spring break of my freshman year and didn't really start to love them until this year. I loved Rango II randomly next and then really got into them through my friend Uwa.",
        "category": "Songs to dance to", 
        "media_link": "https://f4.bcbits.com/img/a2234708408_16.jpg",
    },
    {
        "id": 24,
        "title": "Love Is a Beautiful Thing",
        "artist": [
                {
                    "name": "Vulfpeck",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Hill Climber",
        "year_released": 2018,
        "description": "Uwa and I went to see Vulfpeck at Madison Square Garden off of some tickets I bought from another Barnard student on Buy Sell Trade. The seats were in the Chase sky bridge so super far away, but I did not stop dancing for a single moment. Those boys know how to put on a show. Also I found out that the electric bassist is from Michigan like me, and I was briefly obsessed with every live video I could find of him performing. Since then I've had a new appreciation and ear for hearing the baseline of any song.",
        "category": "Songs to cry to", 
        "media_link": "https://f4.bcbits.com/img/a0869185133_10.jpg",
    },
    {
        "id": 25,
        "title": "Vespers, Op. 37: Nunc dimitis",
        "artist": [
                {
                    "name": "Sergei Rachmaninoff",
                    "mark_as_deleted": False,
                },
                {
                    "name": "Franck Krawczyk",
                    "mark_as_deleted": False,
                },
                {
                    "name": "Sinfonia Varsovia",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Chants d'est (Sur le sentier recouvert)",
        "year_released": 2009,
        "description": "Saskia is big on classical music and I just was never really exposed to it. We have a collaborative playlist now on Spotify called Good Tunes and this is one of my favorites on there. It was also one of my top 5 most played songs of 2019. I love classical music and it has an added level of meaning for me, since a lot of classical music was commissioned by the Catholic Church. I love to pray vespers and this song so beautifully draws me into my soul.",
        "category": "Songs to fall in love to", 
        "media_link": "https://m.media-amazon.com/images/I/81NRbqGuunL._SS500_.jpg",
    },
    {
        "id": 26,
        "title": "Call It Fate, Call It Karma",
        "artist":[
                {
                    "name": "The Strokes",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Comedown Machine",
        "year_released": 2013,
        "description": "Uwa has a great taste in music and she also introduced me to this song. I have it in a playlist with Albert Hammond Jr. and the like. This song is so dreamy and super intimate. It's intimate in a way that I haven't really known before, so it feels strange and exciting and dangerous. Another one of my top songs from 2019.",
        "category": "Songs to dream to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/9/91/The_Strokes_-_Comedown_Machine.jpg",
    },
    {
        "id": 27,
        "title": "Irene",
        "artist": [
                {
                    "name": "Rodrigo Amarante",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Cavalo",
        "year_released": 2014,
        "description": "This song is pure silver. It is so beautiful. I don't really know what the words mean since they're in Portuguese but it's obviously a love song. I love Rodrigo's singing style, and the technique with the microphone is something Gregory Alan also does. I think of sitting on the street patio of some coffee shop in Europe, drinking coffee or smoking a cigarette (even though I definitely don't and really wouldn't smoke).",
        "category": "Songs to fall in love to", 
        "media_link": "https://upload.wikimedia.org/wikipedia/en/4/4b/Cavalo_Rodrigo_Amarante.jpg",
    },
    {
        "id": 28,
        "title": "Tuxedo Junction",
        "artist": [
                {
                    "name": "Glenn Miller",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Pure Gold",
        "year_released": 1980,
        "description": "I went through a phase during my senior year of high shcool of listening only to early twentieth century big band jazz and stuff like that. Like everyone I love Glenn Miller's In the Mood but I more recently heard Tuxedo Junction in an episode of Discovery of witches, which I briefly loved even though I knew the plot and writing were pretty bad.",
        "category": "Songs to fall in love to", 
        "media_link": "https://images-na.ssl-images-amazon.com/images/I/81a6imW9TtL._SL1500_.jpg",
    },
    {
        "id": 29,
        "title": "Don't Wanna Be Without Ya",
        "artist": [
                {
                    "name": "Penny and Sparrow",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Finch",
        "year_released": 2019,
        "description": "I have loved some of Penny and Sparrows sadder stuff, but this song came up on Release Radio and I immediately liked it. I've been going to it more recently on the warmer and sunnier days in the past few weeks, and it's making me really excited for the spring and for summertime. I thought I might be in Denver this summer (although that looks like it's changing) and started daydreaming about it to this song.",
        "category": "Songs to drive out west to", 
        "media_link": "https://storage.googleapis.com/afs-prod/media/c37c9bddbecb43d586551c0d49277752/800.jpeg",
    },
    {
        "id": 30,
        "title": "Le Festin",
        "artist": [
                {
                    "name": "Camille",
                    "mark_as_deleted": False,
                },
            ],
        "album": "Ratatouille (Original Motion Picture Soundtrack)",
        "year_released": 2007,
        "description": "I had to add this song to top off my playlist of songs to fall in love to, because it's Paris and there's an accordian and it starts off slow and soft and then launches into the great adventure of falling in love in Paris. Not to mention that this is one of the greatest movies of all time and I generally love movie soundtracks and scores - this is one of more normal/relateable ones of the movies scores that I like, and it fits perfectly into my playlist.",
        "category": "Songs to fall in love to", 
        "media_link": "https://images-na.ssl-images-amazon.com/images/I/412ZM3S1SpL.jpg",
    },
]


@app.route('/')
def search():
    global tracks

    latest_tracks = tracks[-10:]
    latest_tracks.reverse()

    return render_template('home.html', latest_tracks=latest_tracks)

@app.route('/search_results/')
def display_all():
    counter = len(tracks)

    return render_template('search_results.html', matching_tracks=tracks, search_string="All", number_results=counter)

@app.route('/search_results/<search_string>')
def search_results(search_string=None):
    global tracks

    matches = []

    counter = 0

    for track in tracks:
        for each_artist in track["artist"]:
            if search_string.lower() in each_artist["name"].lower():
                if track not in matches:
                    matches.append(track)
                    counter = counter + 1

        if search_string.lower() in track["title"].lower():
            if track not in matches:
                matches.append(track)
                counter = counter + 1

        elif search_string.lower() in track["category"].lower():
            if track not in matches:
                matches.append(track)
                counter= counter + 1
                
    return render_template('search_results.html', matching_tracks=matches, search_string=search_string, number_results=counter)

@app.route('/view/<id>', methods=['GET', 'POST'])
def track_view(id=None):

    try:
        id = int(id)
    except:
        pass
    for track in tracks:
        track_id = track.get("id")
        try:
            track_id = int(track_id)
        except: 
            pass
        if(track_id == id):
            track_to_view = track

    return render_template('view.html', track=track_to_view)

@app.route('/create')
def create_track():
    return render_template('create.html')

@app.route('/save_track', methods=['Get', 'POST'])
def save_track():
    global current_id
    global tracks

    json_data = request.get_json()
    title = json_data["title"]
    album = json_data["album"] 
    year_released = json_data["year_released"]
    description = json_data["description"]
    category = json_data["category"]
    media_link = json_data["media_link"]

    artist_list = []
    artist1 = json_data["artist1"]
    artist2 = json_data["artist2"]
    artist3 = json_data["artist3"]
    if artist1:
        artist_list.append({
            "name": artist1,
            "mark_as_deleted": False})
    if artist2:
        artist_list.append({
            "name": artist2,
            "mark_as_deleted": False})
    if artist3:
        artist_list.append({
            "name": artist3,
            "mark_as_deleted": False})
    
    current_id += 1
    new_track = {
        "title": title,
        "artist": artist_list,
        "album": album,
        "year_released": year_released,
        "description": description,
        "category": category,
        "media_link": media_link,
        "id":  current_id
    }

    tracks.append(new_track)
    
    return jsonify(new_track_id=current_id)

@app.route('/delete', methods=['GET', 'POST'])
def delete_track():
    global current_id
    global tracks 

    json_data = request.get_json()   
    delete_id = json_data["id"]
    int_id = int(delete_id)

    counter = 0
    for track in tracks:
        track_id = track.get("id")

        if(int(track_id) == int_id):
            del tracks[counter]
        counter += 1
    

    return jsonify(id=delete_id) ## To do this will need to store id in div metadata

@app.route('/save_description', methods=['GET', 'POST'])
def save_description():

    json_data = request.get_json()
    edit_id = json_data["id"]
    new_description = json_data["description"]

    for track in tracks:
        track_id = track.get("id")
        if(int(track_id) == int(edit_id)):
            edited_track = track

    edited_track["description"] = new_description

    return jsonify(description=new_description)

@app.route('/save_category', methods=['GET', 'POST'])
def save_category():

    json_data = request.get_json()
    edit_id = json_data["id"]
    new_category = json_data["category"]

    for track in tracks:
        track_id = track.get("id")
        if(int(track_id) == int(edit_id)):
            edited_track = track

    edited_track["category"] = new_category

    return jsonify(category=new_category)


@app.route('/remove_artist1', methods=['GET', 'POST'])
def remove_artist1():

    json_data = request.get_json()
    edit_id = json_data["id"]

    for track in tracks:
        track_id = track.get("id")
        if(int(track_id) == int(edit_id)):
            edited_track = track

    edited_track["artist"][0]["mark_as_deleted"] = True

    return jsonify()

@app.route('/recover_artist1', methods=['GET', 'POST'])
def recover_artist1():

    json_data = request.get_json()
    edit_id = json_data["id"]

    for track in tracks:
        track_id = track.get("id")
        if(int(track_id) == int(edit_id)):
            edited_track = track

    edited_track["artist"][0]["mark_as_deleted"] = False

    return jsonify()

@app.route('/remove_artist2', methods=['GET', 'POST'])
def remove_artist2():

    json_data = request.get_json()
    edit_id = json_data["id"]

    for track in tracks:
        track_id = track.get("id")
        if(int(track_id) == int(edit_id)):
            edited_track = track

    edited_track["artist"][1]["mark_as_deleted"] = True

    return jsonify()

@app.route('/recover_artist2', methods=['GET', 'POST'])
def recover_artist2():

    json_data = request.get_json()
    edit_id = json_data["id"]

    for track in tracks:
        track_id = track.get("id")
        if(int(track_id) == int(edit_id)):
            edited_track = track

    edited_track["artist"][1]["mark_as_deleted"] = False

    return jsonify()

@app.route('/remove_artist3', methods=['GET', 'POST'])
def remove_artist3():

    json_data = request.get_json()
    edit_id = json_data["id"]

    for track in tracks:
        track_id = track.get("id")
        if(int(track_id) == int(edit_id)):
            edited_track = track

    edited_track["artist"][2]["mark_as_deleted"] = True


    return jsonify()

@app.route('/recover_artist3', methods=['GET', 'POST'])
def recover_artist3():

    json_data = request.get_json()
    edit_id = json_data["id"]

    for track in tracks:
        track_id = track.get("id")
        if(int(track_id) == int(edit_id)):
            edited_track = track

    edited_track["artist"][2]["mark_as_deleted"] = False

    return jsonify()

if __name__ == '__main__':
   app.run(debug = True)