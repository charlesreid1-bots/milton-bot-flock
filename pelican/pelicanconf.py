import markdown

AUTHOR = 'charlesreid1'
SITENAME = 'paradise lost bot flock'
SITEURL = ''#b-milton'
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# --------------8<---------------------

THEME = 'scurvy-knave-theme'

LICENSE_URL = "https://opensource.org/licenses/MIT"
LICENSE_NAME = "MIT License"

# Pelican is designed for files => pages.
# Use variables (below) to set pieces of pages.

INTROCOLOR  = "#fff"
ACOLOR      = "#00edac"
AHOVERCOLOR = "#00b484"
BRIGHTCOLOR = "#1df1ca"
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}

INTROBKG='img/book3black.jpg'
LINKSBKG='img/book1.jpg'

# img/ should be in content/
# available at <url>/img
STATIC_PATHS = ['img']

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "paradise lost bot flock"
SITE_DESCRIPTION = "Tweeting John Milton's <i>Paradise Lost</i> forever"
GITEA_URL = "https://github.com/charlesreid1-bots/milton-bot-flock"

# ---

about_md = markdown.Markdown(extensions=['extra','codehilite'],
                             output_format='html4')

ABOUT_SHORT = "About"

ABOUT_TITLE = "about paradise lost bot flock"

ABOUT_TEXT = """

<br />

**What is the paradise lost bot flock?**

The paradise lost bot flock is a flock of 12 twitter bots that each tweet 
one book of John Milton's epic poem, _Paradise Lost_.

The flock is implemented in Python and uses the 
[rainbow mind machine](https://pages.charlesreid1.com/rainbow-mind-machine)
library.

Each bot is given the entire contents of one book of _Paradise Lost_, 
and tweets the entire contents one line at a time.

For more information about bots and bot flocks, see [bots.charlesreid1.com](https://bots.charlesreid1.com).

Find the bots on twitter at the [paradise lost bot flock twitter list](https://twitter.com/charlesreid1/lists/miltonbotflock)

[@milton_book1](https://twitter.com/milton_book1) &bull;
[@milton_book2](https://twitter.com/milton_book2) &bull;
[@milton_book3](https://twitter.com/milton_book3) &bull;
[@milton_book4](https://twitter.com/milton_book4) &bull;
[@milton_book5](https://twitter.com/milton_book5) &bull;
[@milton_book6](https://twitter.com/milton_book6) &bull;
[@milton_book7](https://twitter.com/milton_book7) &bull;
[@milton_book8](https://twitter.com/milton_book8) &bull;
[@milton_book9](https://twitter.com/milton_book9) &bull;
[@milton_book10](https://twitter.com/milton_book10) &bull;
[@milton_book11](https://twitter.com/milton_book11) &bull;
[@milton_book12](https://twitter.com/milton_book12)

<br />

**Why build the paradise lost bot flock?**

The paradise lost bot flock was built to help drown out some of the noise on Twitter,
and to provide a juxtaposition of classic 17th century English poetry about the fall 
of Satan and Original Sin with the latest goings-on in the Twitter timeline.

<br />
<br />

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">&quot;Whence and what art thou, execrable Shape,</p>&mdash; Paradise Lost Book 2 (@milton_book2) <a href="https://twitter.com/milton_book2/status/990385793666506752?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">That dar&#39;st, though grim and terrible, advance</p>&mdash; Paradise Lost Book 2 (@milton_book2) <a href="https://twitter.com/milton_book2/status/990386801700360192?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">Thy miscreated front athwart my way</p>&mdash; Paradise Lost Book 2 (@milton_book2) <a href="https://twitter.com/milton_book2/status/990387809717444608?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">To yonder gates? Through them I mean to pass,</p>&mdash; Paradise Lost Book 2 (@milton_book2) <a href="https://twitter.com/milton_book2/status/990388817700970496?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">That be assured, without leave asked of thee.</p>&mdash; Paradise Lost Book 2 (@milton_book2) <a href="https://twitter.com/milton_book2/status/990389825701216256?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<br />
<br />

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">From Chaos, and the inroad of Darkness old,</p>&mdash; Paradise Lost Book 3 (@milton_book3) <a href="https://twitter.com/milton_book3/status/990301854734008320?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">Satan alighted walks:  A globe far off</p>&mdash; Paradise Lost Book 3 (@milton_book3) <a href="https://twitter.com/milton_book3/status/990302862793060352?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">It seemed, now seems a boundless continent</p>&mdash; Paradise Lost Book 3 (@milton_book3) <a href="https://twitter.com/milton_book3/status/990303870709460992?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<br />
<br />

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">His arrows, from the fourfold-visaged Four</p>&mdash; Paradise Lost Book 6 (@milton_book6) <a href="https://twitter.com/milton_book6/status/990262814097866752?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">Distinct with eyes, and from the living wheels</p>&mdash; Paradise Lost Book 6 (@milton_book6) <a href="https://twitter.com/milton_book6/status/990263822110736384?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">Distinct alike with multitude of eyes;</p>&mdash; Paradise Lost Book 6 (@milton_book6) <a href="https://twitter.com/milton_book6/status/990264830194941952?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">One Spirit in them ruled; and every eye</p>&mdash; Paradise Lost Book 6 (@milton_book6) <a href="https://twitter.com/milton_book6/status/990265838245572609?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">Glared lightning, and shot forth pernicious fire</p>&mdash; Paradise Lost Book 6 (@milton_book6) <a href="https://twitter.com/milton_book6/status/990266846220771328?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<br />
<br />

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">From Man or Angel the great Architect</p>&mdash; Paradise Lost Book 8 (@milton_book8) <a href="https://twitter.com/milton_book8/status/990400620476612608?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">Did wisely to conceal, and not divulge</p>&mdash; Paradise Lost Book 8 (@milton_book8) <a href="https://twitter.com/milton_book8/status/990401628430745600?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">His secrets to be scanned by them who ought</p>&mdash; Paradise Lost Book 8 (@milton_book8) <a href="https://twitter.com/milton_book8/status/990402636468781056?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">Rather admire; or, if they list to try</p>&mdash; Paradise Lost Book 8 (@milton_book8) <a href="https://twitter.com/milton_book8/status/990403644548792320?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">Conjecture, he his fabrick of the Heavens</p>&mdash; Paradise Lost Book 8 (@milton_book8) <a href="https://twitter.com/milton_book8/status/990404652494606336?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">Hath left to their disputes, perhaps to move</p>&mdash; Paradise Lost Book 8 (@milton_book8) <a href="https://twitter.com/milton_book8/status/990405660473868289?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">His laughter at their quaint opinions wide</p>&mdash; Paradise Lost Book 8 (@milton_book8) <a href="https://twitter.com/milton_book8/status/990406668449021952?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<br />
<br />

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">From standing lake to tripping ebb, that stole</p>&mdash; Paradise Lost Book11 (@milton_book11) <a href="https://twitter.com/milton_book11/status/990243018551709696?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">With soft foot towards the deep; who now had stopt</p>&mdash; Paradise Lost Book11 (@milton_book11) <a href="https://twitter.com/milton_book11/status/990244027554398208?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet playfair" data-lang="en"><p lang="en" dir="ltr">His sluces, as the Heaven his windows shut.</p>&mdash; Paradise Lost Book11 (@milton_book11) <a href="https://twitter.com/milton_book11/status/990245035663806464?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

"""

ABOUT_DESCRIPTION = about_md.convert(ABOUT_TEXT)



# -----------


def make_pages():
    descr = ""

    # 
    # 
    # On The Web
    # 
    # 

    descr += "<h3>Paradise Lost Bot Flock On The Web</h3>"

    # items format:     [ button text,    href url,    fa-icon ]
    items  = [
                [
                    "github.com/charlesreid1-bots/milton-bot-flock",
                    "https://github.com/charlesreid1-bots/milton-bot-flock", 
                    "github"
                ],
                [
                    "pages.charlesreid1.com/b-milton",
                    "https://pages.charlesreid1.com/b-milton",
                    "globe"
                ],
            ]

    for item in items:
        button_text = item[0]
        button_link = item[1]
        button_icon = item[2]

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(button_link)
        descr += "<i class=\"fa fa-fw fa-2x fa-%s\"></i> %s"%(button_icon, button_text)
        descr += "</a></p>\n"

    descr += "\n"

    # 
    # 
    # On The Twitter
    # 
    # 

    descr += "<h3>Paradise Lost Bot Flock On Twitter</h3>"

    for i in range(1,12+1):
        handle = "milton_book%s"%(i)
        button_text = "@%s"%(handle)
        button_link = "https://twitter.com/%s"%(handle)
        button_icon = "twitter"

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(button_link)
        descr += "<i class=\"fa fa-fw fa-2x fa-%s\"></i> %s"%(button_icon, button_text)
        descr += "</a></p>\n"

    descr += "\n"



    return descr



LINKS_TITLE = ""

LINKS_DESCRIPTION = make_pages()



# ---


CONTACT_TITLE = "Contact charlesreid1"

CONTACT_DESCRIPTION = """<p>@charlesreid1 is a full-time data engineer and part-time bot-wrangler working on
the intersection of cloud computing and genomics at UC Santa Cruz.</p>
<p>Get in touch:</p>
<p><a href="mailto:twitter@charlesreid1.com">twitter (at) charlesreid1.com</a></p>
"""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
