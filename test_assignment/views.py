from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
import json, os

def home(request):
    name = ''
    f_name=''
    l_name=''
    result=0
    rs = 0
    email=''
    sub = []
    if request.method == "POST":
        name = request.POST.get("n")
        #print(name)
        js_data=None
        a=5

        with open(os.path.dirname(os.path.dirname(__file__))+"/test_assignment/students_classes.json") as tweetfile:
            files = json.load(tweetfile)
            #print(files)
            for i in files["students"]:
                if name == i["first"] or name == i["last"] or name == (i["first"]+" "+i["last"]):
                    f_name = i['first']
                    l_name = i['last']

                    for r in i['studentClasses']:
                        result += r['grade']

                        for c in files['classes']:
                            if r['id'] == int(c):
                                sub.append(files['classes'][c] +", GRADE:   "+ str(r['grade']))

                    rs = result/6


        return render_to_response("home.html",{'f_name': f_name, 'l_name': l_name, 'rs': rs, 'sub': sub},
        context_instance=RequestContext(request))

    return render_to_response("home.html",
    context_instance=RequestContext(request))
