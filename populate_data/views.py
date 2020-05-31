from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import User, ActivityPeriod
from datetime import datetime
import ujson


def show_json(request):
    latest_name_list = User.objects.values_list()
    output = []
    for name in latest_name_list:
        output_json = {}
        period_activity = []
        output_json['id'] = name[0]
        output_json['real_name'] = name[1]
        output_json['tz'] = name[2]
        period_query = ActivityPeriod.objects.filter(real_name_id=name[0]).values('start_time', 'end_time')
        for period in period_query:
            period['start_time'] = period['start_time'].strftime("%b %d %Y %H:%M%p")
            period['end_time'] = period['end_time'].strftime("%b %d %Y %H:%M%p")
            period_activity.append(period)
        output_json['activity_periods'] = period_activity
        output.append(output_json)
    return HttpResponse(ujson.encode({"ok": True,
                                      "members": output}, indent=4, sort_keys=False), content_type="application/json")
