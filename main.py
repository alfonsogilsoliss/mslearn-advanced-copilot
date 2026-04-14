import json
from os.path import dirname, abspath, join
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


current_dir = dirname(abspath(__file__))
wellknown_path = join(current_dir, ".well-known")
historical_data = join(current_dir, "weather.json")

app = FastAPI()
app.mount("/.well-known", StaticFiles(directory=wellknown_path), name="static")


# load historical json data and serialize it:
with open(historical_data, "r") as f:
    data = json.load(f)

@app.get('/')
def root():
    """
    Allows to open the API documentation in the browser directly instead of
    requiring to open the /docs path.
    """
    return RedirectResponse(url='/docs', status_code=301)


@app.get('/countries')
def countries():
    return list(data.keys())


@app.get('/countries/{country}')
def cities_by_country(country: str):
    if country not in data:
        raise HTTPException(status_code=404, detail='Country not found')

    return list(data[country].keys())


@app.get('/countries/{country}/{city}/{month}')
def monthly_average(country: str, city: str, month: str):
    """
    Return the average high/low temperatures for a given country, city, and month.

    Raises:
        HTTPException (404): If the country, city, or month is not found in the data.
    """
    if country not in data:
        raise HTTPException(status_code=404, detail='Country not found')
    if city not in data[country]:
        raise HTTPException(status_code=404, detail='City not found')
    if month not in data[country][city]:
        raise HTTPException(status_code=404, detail='Month not found')
    return data[country][city][month]

# Generate the OpenAPI schema:
openapi_schema = app.openapi()
with open(join(wellknown_path, "openapi.json"), "w") as f:
    json.dump(openapi_schema, f)