import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from jinja2 import Template


from Functions.RunMap import Run, AddNewCrime
from Functions.BuildMap import GoogleMaps, FMap
from Styles.Map_Page import MapStyle
from Styles.Login_Page import LoginStyle
from Styles.Form_Page import CrimeForm


app = FastAPI()
run_instance = Run()
map_style = MapStyle()
login_style = LoginStyle()
crime_form = CrimeForm()
add_crime = AddNewCrime()


@app.get("/", response_class=HTMLResponse)
async def login():
    template = login_style.login_template()
    return template.render()

@app.get("/map", response_class=HTMLResponse)
async def show_map():
    template = map_style.map_template()
    folium_map_html = run_instance.run()
    return template.render(folium_map_html=folium_map_html)

@app.get("/crime_form", response_class=HTMLResponse)
async def show_crime_form():
    template = crime_form.crime_form_template()
    return template.render()

@app.post("/", response_class=HTMLResponse)
async def post_form(city: str = Form(...), neighborhood: str = Form(...), street: str = Form(...), period: str = Form(...), crime_type: str = Form(...)):
    add_crime.add_to_csv(street, neighborhood, city, crime_type, period)
    return RedirectResponse(url="/crime_form", status_code=303)  

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("SPECTRA:app" ,reload=True)
