from django.shortcuts import render
import requests

from .utils import most_frequent

def launches(request):
    response = requests.get('https://api.spacexdata.com/v3/launches?filter=launch_year')
    launches = response.json()
    """separating the years from the launch occurrencies and returning the year that had the most launches."""
    get_values = lambda key,input_data: [sub_val[key] for sub_val in input_data if key in sub_val]
    launch_years = get_values('launch_year',launches)
    year = most_frequent(launch_years)
    return render(request, "main/launches.html", {"year_ocurred_most_launches": year})

# Create your views here.
