import requests
from lxml import html


def hi():
    print('hello')


def get_everything(id):
    # do a bunch of stuff
    other_id = get_that_other_id(id)
    return 'a json object of reviews'

def get_that_other_id(id):
    r = requests.get('https://www.lendingtree.com/reviews/personal/cashnetusa/81638970')
    stuff = html.fromstring(r.content)
    butt = stuff.cssselect('a.reviewBtn')
    my_id = butt[0].get('data-lenderreviewid')




def loop_through_reviews(new_id):
    pass