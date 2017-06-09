import json

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse

graphite_api = 'http://192.168.199.61:8080'
aac_api = 'http://192.168.199.178:9090/api/v1.0'
aac_headers = {'X-AUTH-TOKEN': 'd14b7042a2af18a9ffe15a0da343497f'}


# Create your views here.
@login_required
def find_metrics(request):
    try:
        query = str(request.GET.get('query'))
    except:
        data = dict(errcode=400, errmsg='Missing required parameter "query"')
        return HttpResponse(json.dumps(data))

    url = '%s/metrics/find/?format=completer&query=%s' % (graphite_api, query)
    try:
        resp = requests.get(url)
        metrics = resp.json()
        data = dict(errcode=0, errmsg='ok', metrics=metrics)
    except Exception as e:
        data = dict(errcode=500, errmsg=str(e))

    return HttpResponse(json.dumps(data), content_type='application/json')


@login_required
def project_view(request):
    aac_url = '%s/projects' % aac_api
    resp = requests.get(aac_url, headers=aac_headers)
    data = resp.json()
    return render(request, 'alert_project_index.html', data)


@login_required
def project_add(request):
    print request.GET, request.POST
    aac_url = '%s/projects' % aac_api
    resp = requests.post(aac_url, headers=aac_headers, data=request.POST)
    data = resp.json()
    return HttpResponse(json.dumps(data), content_type='application/json')


@login_required
def project_edit(request):
    pid = request.GET.get('pid')

    aac_url = '%s/projects/%s' % (aac_api, pid)
    resp = requests.put(aac_url, headers=aac_headers, data=request.POST)
    data = resp.json()
    return HttpResponse(json.dumps(data), content_type='application/json')


@login_required
def item_view(request):
    pid = request.GET.get('pid')

    aac_url = '%s/items' % aac_api
    resp = requests.get(aac_url, headers=aac_headers, params=dict(pid=pid))
    data = resp.json()
    data['pid'] = pid
    return render(request, 'alert_item_index.html', data)


@login_required
def item_add(request):
    aac_url = '%s/items' % aac_api
    resp = requests.post(aac_url, headers=aac_headers, data=request.POST)
    data = resp.json()
    return HttpResponse(json.dumps(data), content_type='application/json')


@login_required
def item_edit(request):
    item_id = request.GET.get('item_id')

    aac_url = '%s/items/%s' % (aac_api, item_id)
    resp = requests.put(aac_url, headers=aac_headers, data=request.POST)
    data = resp.json()
    return HttpResponse(json.dumps(data), content_type='application/json')
