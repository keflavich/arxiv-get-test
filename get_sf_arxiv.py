import arxiv, datetime, json

papers = arxiv.query("cat:astro-ph", max_results=500)

fn = datetime.datetime.now().replace(" ","_")
 
with open(f"data/{fn}.json", "w") as fh:
    json.dump(papers, fh)
