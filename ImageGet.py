import io
import requests
import json
from PIL import Image
import random
import xml.etree.ElementTree as ET
# To do list:
# Add option of Booru
#   Danbooru - Done
#   Gelbooru - Done
#   Safebooru - Done
# Add exception check if page isn't found
# Find way to get number of pages from results
# Check if tag is not returning any results, loop back to input
#
# Current limitations
#   Randomly selects from pages 1 - 3
#


def dansearch(searchedtag):
    randpage = random.randint(1, 3)
    dansearchresult = requests.get("https://danbooru.donmai.us/posts.json?tags=" + searchedtag + "&only=name,large_file_url&limit=200" + "&page=" + str(randpage))
    global xvar
    xvar = json.loads(dansearchresult.content)
    urllist = []
    for i in xvar:
        for key in i:
            urllist.append(i[key])
    if not urllist:
        dansearch(searchedtag)
    url = random.choice(urllist)
    urlreq = requests.get(url)
    url_bit = io.BytesIO(urlreq.content)
    img = Image.open(url_bit)
    img.show()
    quit()


def safesearch(searchedtag):
    randpage = random.randint(1, 3)
    safesearchresult = requests.get("https://safebooru.org/index.php?page=dapi&s=post&q=index&tags=" + searchedtag + "&pid=" + str(randpage))
    tree = ET.parse(io.BytesIO(safesearchresult.content))
    root = tree.getroot()
    urllist = []
    for item in root.findall('post'):
        urllist.append(item.attrib['file_url'])
    if not urllist:
        safesearch(searchedtag)
    url = random.choice(urllist)
    urlreq = requests.get(url)
    url_bit = io.BytesIO(urlreq.content)
    img = Image.open(url_bit)
    img.show()
    quit()


def gelsearch(searchedtag):
    randpage = random.randint(1, 3)
    gelsearchresult = requests.get("https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=" + searchedtag + "&pid=" + str(randpage))
    tree = ET.parse(io.BytesIO(gelsearchresult.content))
    root = tree.getroot()
    urllist = []
    for item in root.findall('post'):
        urllist.append(item.attrib['file_url'])
    if not urllist:
        gelsearch(searchedtag)
    url = random.choice(urllist)
    urlreq = requests.get(url)
    url_bit = io.BytesIO(urlreq.content)
    img = Image.open(url_bit)
    img.show()
    quit()


def mainmenu():
    print("Random Anime girl image")
    print("------Please select a booru to search------")
    print("1. Danbooru" + "\n" +
          "2. Gelbooru" + "\n" +
          "3. Safebooru" + "\n" +
          "4. Random" + "\n" +
          "5. Exit" + "\n")
    menuselect()


def menuselect():
    selectedinput = input("Please select: ")
    try:
        menuchoice = int(selectedinput)
    except ValueError:
        print("\n" + "Only numbers please" + "\n")
        mainmenu()
    if menuchoice == int(1):
        taginput = input("Please type a tag to search: ")
        dansearch(taginput)
    elif menuchoice == int(2):
        taginput = input("Please type a tag to search: ")
        gelsearch(taginput)
    elif menuchoice == int(3):
        taginput = input("Please type a tag to search: ")
        safesearch(taginput)
    elif menuchoice == int(4):
        taginput = input("Please type a tag to search: ")
        search = random.randint(1, 3)
        if search == 1:
            dansearch(taginput)
        elif search == 2:
            gelsearch(taginput)
        elif search == 3:
            safesearch(taginput)
    elif menuchoice == int(5):
        quit()
    elif menuchoice > int(5):
        print("\n" + "Only 1 through 5" + "\n")
        mainmenu()
    elif menuchoice < int(0):
        print("\n" + "No negatives" + "\n")
        mainmenu()


mainmenu()
