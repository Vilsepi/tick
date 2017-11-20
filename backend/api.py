#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./vendored"))
import requests

def get_stock(instrument_id):
    url = "http://www.nasdaqomxnordic.com/webproxy/DataFeedProxy.aspx"
    url_params = {
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
    response = requests.get(url, params=url_params)
    return response.json()

def handler_stock(event, context):
    data = get_stock(os.environ.get("INSTRUMENT_ID"))
    return {
        "statusCode": 200,
        "body": json.dumps(data, indent=1),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }
