# Lending Tree Reviews Service

A simple service that allows a user to pass in a Lending Tree lender's url, and returns all the reviews for that lender.
Built in python3 with Flask.

### Installation
This service requires python3 to be installed on your machine.
1. Clone this repo
2. Create a virtual environment for packages:
    ```shell script
    python3 -m venv venv
    ```
3. Activate your virtual environment
    ```shell script
    . ./venv/bin/activate
   ```
4. Install the requirements
    ```shell script
    pip install requirements.txt
    ```
   
### Usage
Start the application with
```shell script
python3 -m app
```
The server runs on `localhost:5000`.
   
#### Making Requests
1. Find your desired lender's URL on Lending Tree's website.  https://www.lendingtree.com/reviews/personal/ has the list of available lenders.
2. Make a `GET` request to `localhost:5000/review/{lender_url}`

#### Response
Responses are JSON formatted.
```json
{
  "key1": true,
  "key2": [
    {
      "subkey1": "hi",
      "subkey2": 22
    }
  ]
}
```

### Future Considerations
* Persistent storage would likely be the most impactful addition to this project.  After a lender is looked up once, we could store the brand_id that is used by Lending Tree's API.  Then, for future lookups, we would not need to scrape that value from the webpage.
* After storage is in place, a cron job could be run to keep the database of reviews and lenders up to date.
* Docker would be a welcome addition to bundle the service.
* Flask on it's own is not production-ready.  Adding `waitress` would be a simple way to get the app ready for production.
* As the API grows, Sphinx can be added to generate documentation.  As there's only one route currently, a GitHub readme will suffice.