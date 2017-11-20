#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./vendored"))
import requests

def get_stock(instrument_id):
    url = "http://www.nasdaqomxnordic.com/webproxy/DataFeedProxy.aspx"
    params = {
        "SubSystem": "History",
        "Action": "GetChartData",
        "inst.an": "id,nm,fnm,isin,tp,chp,ycp",
        "FromDate": "2017-01-01",
        "ToDate": "2100-01-01",
        "json": "true",
        "showAdjusted": "true",
        "app": "/aktier/microsite-MicrositeChart-history",
        "timezone": "CET",
        "DefaultDecimals": "false",
        "Instrument": instrument_id
    }
    response = requests.get(url, params=params)
    return response.json()

def handler_stock(event, context):
    data = get_stock(os.environ.get("INSTRUMENT_ID"))
    return {
        "statusCode": 200,
        "body": json.dumps(data, indent=1),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }

def get_beer():
    url = f"https://api.untappd.com/v4/user/checkins/{os.environ.get('UNTAPPD_USERNAME')}"
    params = {
        "client_id": os.environ.get("UNTAPPD_APIKEY_ID"),
        "client_secret": os.environ.get("UNTAPPD_APIKEY_SECRET")
    }
    response = requests.get(url, params=params)
    print(f"Ratelimit remaining: {response.headers.get('x-ratelimit-remaining')}")
    return response.json()

def handler_beer(event, context):
    beers = get_beer()
    response = [
        {
            "created_at": item["created_at"],
            "score": item["rating_score"],
            "beer": item["beer"]["beer_name"]
        } for item in beers["response"]["checkins"]["items"]
    ]
    return {
        "statusCode": 200,
        "body": json.dumps(response, indent=1),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }
