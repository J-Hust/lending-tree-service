import json
import sys
from math import ceil
import requests
from lxml import html


MAX_RECORDS_PER_REQUEST = 300

def fetch_all_reviews(lender_url):
    """
    Orchestrate the process of getting all reviews for a particular lender, and return them as JSON.

    Parameters:
    lender_url (str): the lender's url

    Returns:
    string: a JSON string of all reviews for a lender
    """

    brand_id = retrieve_brand_id(lender_url)
    if brand_id < 0:
        return 'Could not retrieve brand_id.  Check the url you provided and try again.'
    all_reviews = iterate_reviews(brand_id)
    my_json = json.dumps(all_reviews)
    return my_json


def retrieve_brand_id(lender_url):
    """
    From the lender url passed in to this service, fetch and return the corresponding brand_id used by Lending Tree's API.

    Parameters:
    lender_url (str): the lender's url

    Returns:
    int: the brand_id that corresponds to the lender
    """

    try:
        req = requests.get(lender_url)
    except requests.exceptions.RequestException as err:
        print(f'error fetching url: {err}')
        return -1
    html_tree = html.fromstring(req.content)
    review_button = html_tree.cssselect('a.reviewBtn')
    if not review_button:
        return -1
    brand_id = int(review_button[0].get('data-lenderreviewid'))
    return brand_id


def iterate_reviews(brand_id):
    """
    Loop over response pages from Lending Tree's API, building up, and finally returning, a list of all reviews.

    Parameters:
    brand_id (int): the lender's brand_id

    Returns:
    list: the list of all reviews for a given lender
    """

    total_reviews = fetch_review_count(brand_id)
    num_pages = ceil(total_reviews / MAX_RECORDS_PER_REQUEST) + 1

    final_list = []
    for i in range(0, num_pages):
        reviews = fetch_review_details(brand_id, i)
        final_list.extend(reviews)

    return final_list


def fetch_review_count(brand_id):
    """
    Return the total count of reviews for a particular lender.

    Parameters:
    id (int): the lender's brand_id

    Returns:
    int: total count of reviews for a particular lender.
    """

    url = ("https://www.lendingtree.com/content/mu-plugins/lt-review-api/review-api-proxy.php"
           f"?RequestType=&productType=&brandId={brand_id}"
           f"&requestmode=stats&page=0"
           f"&sortby=reviewsubmitted&sortorder=desc&pagesize={MAX_RECORDS_PER_REQUEST}"
           f"&AuthorLocation=All&OverallRating=0&_t=1581561333869")

    try:
        req = requests.get(url)
    except requests.exceptions.RequestException as err:
        print(f'error fetching url: {err}')
        sys.exit(1)
    response_json = req.json()
    num_reviews = int(response_json['result']['statistics']['reviewCount'])
    return num_reviews


def fetch_review_details(brand_id, page_number):
    """
    For a given review page, load the JSON and return the relevant part.

    Parameters:
    id (int): the lender's brand_id
    page_number (int): the current page number

    Returns:
    dict: the review details
    """

    url = ("https://www.lendingtree.com/content/mu-plugins/lt-review-api/review-api-proxy.php"
           f"?RequestType=&productType=&brandId={brand_id}"
           f"&requestmode=reviews&page={page_number}"
           f"&sortby=reviewsubmitted&sortorder=desc&pagesize={MAX_RECORDS_PER_REQUEST}"
           f"&AuthorLocation=All&OverallRating=0&_t=1581561333869")

    try:
        req = requests.get(url)
    except requests.exceptions.RequestException as err:
        print(f'error fetching url: {err}')
        sys.exit(1)
    response_json = req.json()
    review_data = response_json['result']['reviews']
    return review_data
