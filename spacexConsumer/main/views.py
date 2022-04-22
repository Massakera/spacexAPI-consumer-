from django.shortcuts import render
import requests

from .utils import most_frequent, get_json_values, get_max_dict

def launches(request):
    """main request. Retrieve the year that had most launches"""
    response_launches = requests.get('https://api.spacexdata.com/v3/launches?filter=launch_year')
    launches = response_launches.json()
    launch_years = get_json_values('launch_year',launches)
    result_launches = most_frequent(launch_years)

    """retrieve the launch site most used for launches """
    response_sites = requests.get('https://api.spacexdata.com/v3/launches?filter=launch_site')
    sites = response_sites.json()
    launch_sites = get_json_values("launch_site", sites)
    result_sites = get_max_dict(launch_sites,'site_id')

    """retrieve the number of launches between 2019 and 2021"""
    response_2019_2021 = requests.get('https://api.spacexdata.com/v3/launches?start=2019&end=2021')
    launches_2019_2021 = response_2019_2021.json()
    result_2019_2021 = len(launches_2019_2021)

    data = {
        "year_most_launches": str(result_launches),
        "launch_sites":result_sites,
        "launches_2019_2021":str(result_2019_2021)
        }

    return render(request,"main/launches.html", {"data":data})