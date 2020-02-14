import requests
import json
import sys
from lxml import html
from math import ceil


MAX_RECORDS_PER_REQUEST = 300


def fetch_all_reviews(lender_url):
    brand_id = retrieve_brand_id(lender_url)
    if not brand_id:
        return 'Could not retrieve brand_id.  Check the url you provided and try again.'
    all_reviews = iterate_reviews(brand_id)
    my_json = json.dumps(all_reviews)
    return my_json


def retrieve_brand_id(lender_url):
    try:
        r = requests.get(lender_url)
    except requests.exceptions.RequestException as err:
        print(f'error fetching url: {err}')
        sys.exit(1)
    html_tree = html.fromstring(r.content)
    review_button = html_tree.cssselect('a.reviewBtn')
    if not review_button:
        return
    brand_id = int(review_button[0].get('data-lenderreviewid'))
    return brand_id


def iterate_reviews(id):
    total_reviews = fetch_review_count(id)
    num_pages = ceil(total_reviews / MAX_RECORDS_PER_REQUEST) + 1

    final_array = []
    for i in range(0, num_pages):
        reviews = fetch_review_details(id, i)
        final_array.extend(reviews)

    return final_array


def fetch_review_details(id, page_number):
    url = ("https://www.lendingtree.com/content/mu-plugins/lt-review-api/review-api-proxy.php"
           f"?RequestType=&productType=&brandId={id}"
           f"&requestmode=reviews&page={page_number}"
           f"&sortby=reviewsubmitted&sortorder=desc&pagesize={MAX_RECORDS_PER_REQUEST}"
           f"&AuthorLocation=All&OverallRating=0&_t=1581561333869")

    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as err:
        print(f'error fetching url: {err}')
        sys.exit(1)
    response_json = r.json()
    review_data = response_json['result']['reviews']
    return review_data


def fetch_review_count(id):
    url = ("https://www.lendingtree.com/content/mu-plugins/lt-review-api/review-api-proxy.php"
           f"?RequestType=&productType=&brandId={id}"
           f"&requestmode=stats&page=0"
           f"&sortby=reviewsubmitted&sortorder=desc&pagesize={MAX_RECORDS_PER_REQUEST}"
           f"&AuthorLocation=All&OverallRating=0&_t=1581561333869")

    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as err:
        print(f'error fetching url: {err}')
        sys.exit(1)
    response_json = r.json()
    num_reviews = int(response_json['result']['statistics']['reviewCount'])
    return num_reviews

