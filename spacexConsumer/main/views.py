from posixpath import split
from unittest import result
from django.shortcuts import render
import requests

from .utils import most_frequent, get_json_values, get_max_dict

def launches(request):
    """GET request to retrieve the year that occurred most launches."""
    response = requests.get('https://api.spacexdata.com/v3/launches?filter=launch_year')
    launches = response.json()
    launch_years = get_json_values('launch_year',launches)
    year = most_frequent(launch_years)
    return render(request, "main/launches.html", {"year_ocurred_most_launches": year})

def launch_sites(request):
    """GET request to retrieve the launch_site where occurred most launches."""
    response = requests.get('https://api.spacexdata.com/v3/launches?filter=launch_site')
    launches = response.json()
    launch_sites = get_json_values("launch_site", launches)
    result = get_max_dict(launch_sites,'site_id')
    return render(request,"main/launches.html", {"most_frequent_launch_site": result})