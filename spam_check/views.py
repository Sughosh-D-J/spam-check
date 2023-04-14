from django.shortcuts import render, redirect
import requests
import re
import json

# Create your views here.
def check_email(request):
    
    return render(request,'home.html')


def output(request):
    if request.method=='POST':
        url = "https://mailcheck.p.rapidapi.com/"
        email = request.POST.get('Email')
        querystring = {"domain":email}

        headers = {
	                "X-RapidAPI-Key": "f285daf82fmsh31dd9b56d1c8a7ap10e25ejsn64681f76ab06",
	                "X-RapidAPI-Host": "mailcheck.p.rapidapi.com"
                    }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = re.findall(r'(\{[^{}]+\})',response.text)
        print(dict(json.loads(response[0])))
        context1 = dict(json.loads(response[0]))
        return render(request,'output.html',{'content':context1})
    

def details(request):
    content = {
        'valid: true / false':'The "valid" boolean indicates if the requested domain or e-mail is valid. Non-existing domains or invalid data will set this flag as false. Please note that disposable e-mail domains are still valid to receive e-mails, so they also have this value set to true.',
        'block: true / false':'The "block" boolean is the most important part of the response. This indicates if the API suggests you should block this e-mail / sign-up. Block is set to "true" for invalid domains, disposable domains, or domains / e-mails by spam bots or automated signups. This is usually the only flag you need to look at.',
        'disposable: true / false':"The 'disposable' boolean indicates if we suspect this to be a disposable or temporary e-mail address. Some new domains are blocked based on their anomalies before we know if it's disposable or not.",
        'text: string':'The "text" string response contains a description of the result of the API lookup. The "text" and "reason" results are meant for manual analysis, and are not fit to present to end users directly.',
        'reason: string':'The "reason" string response contains a slightly more technical indication of why this result was reached. The "text" and "reason" results are meant for manual analysis, and are not fit to present to end users directly.',
        'risk: integer 0-100':'This API combines many heuristic analyses and threat feeds into a single result. The "risk" integer is a numerical representation of the anomalies detected. Regular domains usually have a risk score of 0-30.',
        'possible_typo: array of strings':'This variable can contain an array of strings with possible domains that the user really meant to type. "exaample.com" could have "example.com" listed as a possibly typo string.',
        'mx_host: string':'The "mx_host" value represents the detected MX host for the domain. It can be either a domain name or IP-address or null.',
        'mx_ip: string':'The "mx_ip" value is the IP address of the detected MX host. It can be null if no valid MX is detected.',
        'mx_info: string':'The "mx_info" value contains details about how the MX host was detected or chosen.',
        'last_changed_at: string':"The 'last_changed_at' string contains a ISO 8601 formatted date and time for when the risk score, or block suggestion was last changed for this domain or e-mail. If a domain was previously okay, but we notice that it's being used with malicious intent, the 'block' flag will be set to true, and the last_changed_at updated. If this domain or e-mail didn't previously have a risk score calculated, it is set to the current date and time of the API request."

    }

    return render(request,'details.html',{'content':content})
