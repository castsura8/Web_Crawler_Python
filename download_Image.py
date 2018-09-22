

#importing image from online : using modules and functions
import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


download_web_image("https://images.unsplash.com/photo-1536770494015-01837601cbd4?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=923dc616ffd0fa46ecdd0d7977f867dd&auto=format&fit=crop&w=800&q=60")