import arxiv, datetime, json

papers = arxiv.query("cat:astro-ph", max_results=500)

fn = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%s")

with open(f"data/{fn}.json", "w") as fh:
    json.dump(papers, fh)

import requests

# TODO: log in...

bentyfield_request = requests.get('https://www.benty-fields.com/jc_json/484')

bentyfield_json = bentyfield_request.json()


