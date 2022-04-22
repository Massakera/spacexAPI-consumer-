import io
from django.http import HttpResponse
from django.shortcuts import render
from xlsxwriter import Workbook
import requests
from django.core.cache import cache

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
    
    request.session['data'] = data

    return render(request,"main/launches.html", {"data":data})

def export_csv(request):
    """method for exporting data into a .xlsx file."""
    data = request.session.get('data')
    elements = [
        data['year_most_launches'],
        str(data['launch_sites']),
        data['launches_2019_2021']
    ]

    output = io.BytesIO() 
    workbook = Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    r = 0
    c = 0

    table_headers = [
        'year_most_launches',
        'launch_sites',
        'launches_2019_2021'
    ]

    for header in table_headers:
        worksheet.write(r, c, header)
        c += 1

    r += 1
    c = 0
    for element in elements:
        worksheet.write(r, c, element)
        c += 1

    workbook.close()
    output.seek(0)
    content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    response = HttpResponse(output.read(), content_type=content_type)
    file_name = ('results')
    response['Content-Disposition'] = "attachment; filename=" + file_name + ".xlsx"
    return response