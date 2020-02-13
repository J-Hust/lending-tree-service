import requests
import json
from lxml import html
from math import ceil


def hi():
    print('hello')


def review_flow(lender_id):
    brand_id = retrieve_brand_id(lender_id)
    las_revistas = retrieve_reviews(brand_id)
    return 'a json object of reviews from id {}'.format(brand_id)

def retrieve_brand_id(lender_id):
    r = requests.get('https://www.lendingtree.com/reviews/personal/cashnetusa/{}'.format(lender_id))
    html_tree = html.fromstring(r.content)
    review_button = html_tree.cssselect('a.reviewBtn')
    brand_id = review_button[0].get('data-lenderreviewid')
    return brand_id

def retrieve_reviews(id):
    MAX_RECORDS_PER_REQUEST = 300
    url = 'https://www.lendingtree.com/content/mu-plugins/lt-review-api/review-api-proxy.php?RequestType=&productType=&brandId=42825&requestmode=reviews,stats,ratingconfig,propertyconfig&page=0&sortby=reviewsubmitted&sortorder=desc&pagesize=300&AuthorLocation=All&OverallRating=0&_t=1581561333869'

    r = requests.get(url)
    response_json = r.json()
    total_reviews = int(response_json['total'])
    num_pages = ceil(total_reviews/MAX_RECORDS_PER_REQUEST)

    final_array = []
    for i in range(0, num_pages + 1):
        reviews = fetch_review_list(id, i)
        final_array.extend(reviews)

    return final_array
    
def fetch_review_list(id, page_number):
    # formatted url
    url = 'https://www.lendingtree.com/content/mu-plugins/lt-review-api/review-api-proxy.php?RequestType=&productType=&brandId={}&requestmode=reviews,stats,ratingconfig,propertyconfig&page={}&sortby=reviewsubmitted&sortorder=desc&pagesize=300&AuthorLocation=All&OverallRating=0&_t=1581561333869'.format(id, page_number)
    r = requests.get(url)
    response_json = r.json()
    review_data = response_json['result']['reviews']
    return review_data