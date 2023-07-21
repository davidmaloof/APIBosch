import pandas as pd
import fastapi
from typing import Optional

app = fastapi.FastAPI()
df = pd.read_csv("data/data.csv")
df = df.astype(str)  # Convert entire dataframe to string type for serialization


@app.get("/search/")
def search_jobs(title: Optional[str] = None, requirements: Optional[str] = None):
    results = df
    if title:
        results = results[results["title"].str.contains(title, case=False)]
    if requirements:
        results = results[
            results["requirements"].str.contains(requirements, case=False)
        ]
    return results.to_dict("records")
