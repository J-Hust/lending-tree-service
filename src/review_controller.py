from flask import Blueprint
from src.review_service import fetch_all_reviews
import re

reviews = Blueprint('reviews', __name__, url_prefix='/review')


@reviews.route('/<path:link>')
def get_reviews(link):
    if is_valid_url(link):
        lender_id = extract_lender_id_from_url(link)
        return fetch_all_reviews(lender_id)
    else:
        raise ValueError('url must begin with "https://www.lendingtree.com/" and end with a number')


def is_valid_url(url):
    matches_found = re.match(r'https://www\.lendingtree\.com.+/[0-9]+$', url)

    if matches_found is not None:
        return True
    return False


def extract_lender_id_from_url(url):
    return int(url[url.rfind('/') + 1::])
