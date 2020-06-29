import arxiv, datetime, json

papers = arxiv.query("cat:astro-ph", max_results=500)

fn = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%s")
 
with open(f"data/{fn}.json", "w") as fh:
    json.dump(papers, fh)
