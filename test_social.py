import urllib.request
import random

def banner():
    print("\n")
    print("                   01      //\\\        //\\\      10                   ")
    print("                     10   //  \\\      //  \\\    01                    ")
    print("                       01//====\\\    //====\\\ 10                      ")
    print("                     10 //      \\\  //      \\\  01                    ")
    print("                  01   //        \\\//        \\\   10                  ")
    print("                            contact info                                ")
    print("          this app is for collecting information from a person          ")
    print("                @kavak9003 @xeroos \"uniApp\" \"zerOne\"                ")

def banner1():
    print("\n")
    print("                     =====    01   =====")
    print("         ||  //       //\\\          //\\\      ||  //      ")
    print("         || //       //  \\\        //  \\\     || //      ")
    print("         ||//       //====\\\      //====\\\    ||//      ")
    print("         ||\\\      //      \\\    //      \\\   ||\\\       ")
    print("         || \\\    //        \\\  //        \\\  || \\\      ")
    print("         ||  \\\  //          \\\//          \\\ ||  \\\         ")
    print("                ===         =====          === ")
    print("                            contact info           ")
    print("          this app is for collecting information from a person        ")
    print("                @kavak9003 @xeroos \"uniApp\" \"zerOne\"     ")

# blogspot link
def blogspot(usr_name):
    blog_link = "https://" + usr_name + ".blogspot.com"
    try:
        code = urllib.request.urlopen(blog_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("blogspot" + arrow_ic+ "    " + blog_link + end_no)
    elif code == 200:
        file_write(1)
        print("blogspot"+ arrow_ic+ blog_link+end_ok)
        file_user_name.write("blogspot" + arrow_ic + blog_link + "\n")


# google_plus link
def googleplus(usr_name):
    google_link = "https://plus.google.com/" + usr_name + "/posts"
    try:
        code = urllib.request.urlopen(google_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("google plus" + arrow_ic+ "    " + google_link + end_no)
    elif code == 200:
        file_write(1)
        print("google plus"+ arrow_ic+ google_link+end_ok)
        file_user_name.write("google plus" + arrow_ic+ google_link + "\n")


# wordpress link
def wordpress(usr_name):
    wordpress_link = "https://" + usr_name + ".wordpress.com"
    try:
        code = urllib.request.urlopen(wordpress_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("wordpress" + arrow_ic+ "    " + wordpress_link + end_no)
    elif code == 200:
        file_write(1)
        print("wordpress"+ arrow_ic+ wordpress_link+end_ok)
        file_user_name.write("wordpress" + arrow_ic+ wordpress_link + "\n")


# tumblr link
def tumblr(usr_name):
    tumblr_link = "https://" + usr_name + ".tumblr.com"
    try:
        code = urllib.request.urlopen(tumblr_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("tumbr"+ arrow_ic + "    " + tumblr_link +end_no)
    elif code == 200:
        file_write(1)
        print("tumblr"+ arrow_ic+ tumblr_link+end_ok)
        file_user_name.write("tumblr"+ arrow_ic + tumblr_link + "\n")


# deviantart link
def deviantart(usr_name):
    deviantart_link = "https://" + usr_name + ".deviantart.com"
    try:
        code = urllib.request.urlopen(deviantart_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("deviantart"+ arrow_ic + "    " + deviantart_link + end_no)
    elif code == 200:
        file_write(1)
        print("deviantart"+ arrow_ic+ deviantart_link+end_ok)
        file_user_name.write("deviantart"+ arrow_ic + deviantart_link + "\n")


# livejournal link
def livejournal(usr_name):
    livejournal_link = "https://" + usr_name + ".livejournal.com"
    try:
        code = urllib.request.urlopen(livejournal_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("livejournal"+ arrow_ic + "    " + livejournal_link + end_no)
    elif code == 200:
        file_write(1)
        print("livejournal"+ arrow_ic+ livejournal_link+ end_ok)
        file_user_name.write("livejournal"+ arrow_ic + livejournal_link + "\n")

# newgrounds link
def newgrounds(usr_name):
    newgrounds_link = "https://" + usr_name + ".newgrounds.com"
    try:
        code = urllib.request.urlopen(newgrounds_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("Newgrounds" + arrow_ic+ "    " + newgrounds_link + end_no)
    elif code == 200:
        file_write(1)
        print("Newgroundsl"+ arrow_ic+ newgrounds_link+end_ok)
        file_user_name.write("Newgroundsl"+ arrow_ic + newgrounds_link + "\n")


# HubPages link
def hubPages(usr_name):
    HubPages_link = "https://" + usr_name + ".hubpages.com"
    try:
        code = urllib.request.urlopen(HubPages_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("HubPages"+ arrow_ic + "    " + HubPages_link + end_no)
    elif code == 200:
        file_write(1)
        print("HubPages"+ arrow_ic+ HubPages_link +end_ok)
        file_user_name.write("HubPages" + arrow_ic+ HubPages_link + "\n")


# Contently link
def contently(usr_name):
    contently_link = "https://" + usr_name + ".contently.com"
    try:
        code = urllib.request.urlopen(contently_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("Contently" + arrow_ic+ "    " + contently_link + end_no)
    elif code == 200:
        file_write(1)
        print("Contently"+ arrow_ic+ contently_link+end_ok)
        file_user_name.write("Contently" + arrow_ic+ contently_link + "\n")


# Slack link
def slack(usr_name):
    slack_link = "https://" + usr_name + ".slack.com"
    try:
        code = urllib.request.urlopen(slack_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("Slack" + arrow_ic+ "    " + slack_link + end_no)
    elif code == 200:
        file_write(1)
        print("Slack"+ arrow_ic+ slack_link+end_ok)
        file_user_name.write("Slack" + arrow_ic+ slack_link + "\n")

# tripit link
def tripit(usr_name):
    tripit_link = "https://www.tripit.com/people/" + usr_name + "#/profile/basic-info"
    try:
        code = urllib.request.urlopen(tripit_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("tripit"+ arrow_ic + "    " + tripit_link + end_no)
    elif code == 200:
        file_write(1)
        print("tripit"+ arrow_ic+ v_link+end_ok)
        file_user_name.write("tripit" + arrow_ic+ v_link + "\n")


# basecamphq link
def basecamphq(usr_name):
    basecamphq_link = "https://" + usr_name + ".basecamphq.com/login"
    try:
        code = urllib.request.urlopen(basecamphq_link).getcode()
    except OSError:
        code = 404
    if code == 404:
        file_write(0)
        print("basecamphq" + arrow_ic+ "    " + basecamphq_link + end_no)
    elif code == 200:
        file_write(1)
        print("basecamphq"+ arrow_ic + basecamphq_link +end_ok)
        file_user_name.write("basecamphq" + arrow_ic+ basecamphq_link +"\n")


def start_scan():
    for name in user_name_full:
        blogspot(name)
        googleplus(name)
        wordpress(name)
        tumblr(name)
        deviantart(name)
        livejournal(name)
        newgrounds(name)
        hubPages(name)
        contently(name)
        slack(name)
        tripit(name)
        basecamphq(name)

def start_scan_list():
    for i in range(0, len(url_list)):
        for name in user_name_full:
            usr_link = url_list[i] + name
            try:
                cod = urllib.request.urlopen(usr_link).getcode()
            except OSError:
                cod = 404

            if cod == 200:
                file_write(1)
                m = file_user_name.write(name_list[i]+ arrow_ic + usr_link + "\n")
                print(name_list[i]+ arrow_ic + usr_link + end_ok + str(m))
            else:
                file_write(0)
                print(name_list[i] + arrow_ic + usr_link + end_no)

def file_write(i):
    global file_user_name
    if i == 0:
        file_user_name.close()
    else:
        file_user_name = open(usr_name+"_"+usr_fam+".txt", "a")


def create_user_name():

    user_name_full.append(usr_name + "_" + usr_fam)  # kavak_9003

    user_name_full.append(usr_fam + "_" + usr_num)  # kavak_9003_8985

    user_name_full.append(usr_fam + usr_num)  # kavak_90038985

    user_name_full.append(usr_name + usr_fam)  # kavak9003

    user_name_full.append(usr_name + usr_fam + usr_num)  # kavak90038985

    user_name_full.append(usr_name[0] + "_" + usr_fam[0])  # k_9

    user_name_full.append(usr_name[0] + "_" + usr_fam[0] + usr_num)  # k_94420

    user_name_full.append(usr_name[0] + "_" + usr_fam[0] + "_")  # k_9_4420

    user_name_full.append(usr_fam + usr_name)  # 9003kavak

    user_name_full.append(usr_fam + usr_name + usr_num)  # 9003kavak8985

    user_name_full.append(usr_fam + "_" + usr_name)  # 9003_kavak

    user_name_full.append(usr_fam + "_" + usr_name + usr_num)  # 9003_kavak8985

    user_name_full.append(usr_fam + "_" + usr_name + "_" + usr_num)  # 9003_kavak_8985

    user_name_full.append(usr_name + "." + usr_fam)  # kavak.9003

    user_name_full.append(usr_name + "." + usr_fam + "." + usr_num)  # kavak.9003.8985

    user_name_full.append(usr_name + "." + usr_fam + usr_num)  # kavak.90038985

    user_name_full.append(usr_fam + "." + usr_name)  # 9003.kavak

    user_name_full.append(usr_fam + "." + usr_name + usr_num)  # 9003.kavak8985

    user_name_full.append(usr_fam + "." + usr_name + "." + usr_num)  # 9003.kavak.8985

    user_name_full.append(usr_name[0] + "." + usr_fam)  # k.9003

    user_name_full.append(usr_name[0] + usr_fam)  # k9003

    user_name_full.append(usr_name[0] + "." + usr_fam + usr_num)  # k.90038985

    user_name_full.append(usr_name[0] + usr_fam + usr_num)  # k90038985

    user_name_full.append(usr_name[0] + "." + usr_fam + "." + usr_num)  # k.9003.8985

    user_name_full.append(usr_fam[0] + usr_name)  # 9kavak

    user_name_full.append(usr_fam[0] + usr_name + usr_num)  # 9kavak8985

    user_name_full.append(usr_fam[0] + "." + usr_name)  # 9.kavak

    user_name_full.append(usr_fam[0] + "." + usr_name + usr_num)  # 9.kavak8985

    user_name_full.append(usr_fam[0] + "." + usr_name + "." + usr_num)  # 9.kavak.8985

    user_name_full.append(id_social)


url_list = ["https://www.instagram.com/",
            "https://sapp.ir/",
            "https://www.facebook.com/",
            "https://www.twitter.com/",
            "https://www.youtube.com/",
            "https://www.reddit.com/user/",
            "https://www.pinterest.com/",
            "https://www.github.com/",
            "https://www.flickr.com/people/",
            "https://steamcommunity.com/id/",
            "https://vimeo.com/",
            "https://soundcloud.com/",
            "https://disqus.com/",
            "https://medium.com/@",
            "https://vk.com/",
            "https://about.me/",
            "https://imgur.com/user/",
            "https://flipboard.com/@",
            "https://slideshare.net/",
            "https://fotolog.com/",
            "https://open.spotify.com/user/",
            "https://www.mixcloud.com/",
            "https://www.scribd.com/",
            "https://www.badoo.com/en/",
            "https://www.patreon.com/",
            "https://bitbucket.org/",
            "https://www.dailymotion.com/",
            "https://www.etsy.com/shop/",
            "https://cash.me/",
            "https://www.behance.net/",
            "https://www.goodreads.com/",
            "https://www.instructables.com/member/",
            "https://keybase.io/",
            "https://kongregate.com/accounts/",
            "https://angel.co/",
            "https://last.fm/user/",
            "https://dribbble.com/",
            "https://www.codecademy.com/",
            "https://en.gravatar.com/",
            "https://pastebin.com/u/",
            "https://foursquare.com/",
            "https://www.roblox.com/user.aspx?username=",
            "https://www.gumroad.com/",
            "https://www.wattpad.com/user/",
            "https://www.canva.com/",
            "https://www.creativemarket.com/",
            "https://www.trakt.tv/users/",
            "https://500px.com/",
            "https://buzzfeed.com/",
            "https://tripadvisor.com/members/",
            "https://houzz.com/user/",
            "https://blip.fm/",
            "https://www.wikipedia.org/wiki/User:",
            "https://news.ycombinator.com/user?id=",
            "https://www.codementor.io/",
            "https://www.reverbnation.com/",
            "https://www.designspiration.net/",
            "https://www.bandcamp.com/",
            "https://www.colourlovers.com/love/",
            "https://www.ifttt.com/p/",
            "https://www.ebay.com/usr/",
            "https://www.okcupid.com/profile/",
            "https://www.trip.skyscanner.com/user/",
            "https://ello.co/",
            "https://tracky.com/user/"]

name_list = ["instagram", "soroush", "facebook", "twitter", "youtube", "reddit",
             "pinterest", "github", 'flickr', "steam", "vimeo", 'soundcloud', "disqus",
             "medium", "vk", "about.me", "imgur", "flipboard", "slideshare", "fotolog",
             "spotify", "mixcloud", "scribd", "badoo", "patreon", "bitbucket",
             "dailymotion", "etsy", "cash", "behance", "goodreads",
             "instructables", "keybase", "kongregate",
             "AngelList", "Last.fm", "Dribbble", "Codecademy",
             "Gravatar", "Pastebin", "Foursquare", "Roblox", "Gumroad", "Wattpad", "Canva",
             "Creativemarket", "Trakt", "500px", "Buzzfeed", "Tripadvisor", "Houzz", "Blip",
             "Wikipedia", "ycombinator", "codementor", "reverbnation", "designspiration",
             "bandcamp", "colourlovers", "ifttt", "ebay", "okcupid", "skyscanner", "ello", "tracky"]

num = random.randint(0,1)
if num == 0:
    banner()
elif num == 1:
    banner1()
print("\n")
user_name_full = []
usr_name = input("\t pleasE enteR targeT firstnamE => ")
usr_fam = input("\t pleasE enteR targeT familiY => ")
phone_number = input("\t pleasE enteR targeT phonE number => ")
number_start = len(phone_number) - 4
number_end = len(phone_number)
usr_num = phone_number[len(phone_number)-4] + phone_number[len(phone_number)-3] + phone_number[len(phone_number)-2] + phone_number[len(phone_number)-1]
id_social = input("\t pleasE enteR exmplE iD in sociaL networK => ")


file_user_name = open(usr_name+"_"+usr_fam+".txt", "a")
file_user_name.write("\n"
                     "                  01      //\\\        //\\\      10                  \n"
                     "                    10   //  \\\      //  \\\    01                   \n"
                     "                      01//====\\\    //====\\\ 10                     \n"
                     "                    10 //      \\\  //      \\\  01                   \n"
                     "                  01  //        \\\//        \\\   10                 \n"
                     "                           contact info                               \n"
                     "         this app is for collecting information from a person         \n"
                     "               @kavak9003 @xeroos \"uniApp\" \"zerOne\"               \n\n")
end_ok = "\t ok :)"
end_no = "\t this account not found :("
arrow_ic = " => "
# start class
# detail      usr_name= kavak      usr_fam=9003         usr_num=4420
create_user_name()
start_scan_list()
start_scan()

usr_name = input("\t finisH")
