from flask import Blueprint
from src.review_service import review_flow
import re

reviews = Blueprint('reviews', __name__, url_prefix='review')

@reviews.route('/<path:link')
def get_reviews(link):
    if is_valid_url(link):
        lender_id = extract_lender_id_from_url(link)
        review_flow(lender_id)
    else:
        raise ValueError('url must begin with "https://www.lendingtree.com" and end with a number')


def is_valid_url(url):
    matches_regex = re.match(r'https://www\.lendingtree\.com.+/[0-9]+$', url)

    if not matches_regex is None:
        return True
    return False


def extract_lender_id_from_url(url):
    return url[url.rfind('/') + 1::]