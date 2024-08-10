from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from app.models import JobPost 
#from django.template import loader


# Create your views here.

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First job description",
    "Second Job description",
    "Third Job description"
]

class TempClasss:
    x = 10

def hello(request):
    #template = loader.get_template("app/hello.html")
    #context = {}
    #return HttpResponse(template.render(context, request))
    #template_name = "app/hello.html"
    list_object = ['Mango', 'Jackfruit', 'Grape',]
    temp_object = TempClasss()
    is_authenticated = True
    
    
    context = {
        "name": "Md Nadim, self-taught programmer",
        "age" : 20,
        "Course_name": "Learning Django",
        "list": list_object,
        "temp": temp_object,
        "is_authenticated": is_authenticated, 
    }
    
    return render(request, "app/hello.html", context)
    

    
    

#def hello(request):
#    return HttpResponse("<h3>Hello #viewers---exigency!!!<h3>")
def job_list(request):
    # list_of_job = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('jobs_detail', args=(job_id,))
        
    #     list_of_job += f"<li><a href='{detail_url}'>{j}</a></li>"
    # list_of_job += "</ul>"    
    # return HttpResponse(list_of_job)
    
    #context = {"job_title_list": job_title}
    jobs = JobPost.objects.all()
    
    context = {"jobs": jobs}
    return render(request, "app/index.html", context)


    
def job_detail(request, id):
    
    try:   
        if id == 0:
            return redirect(reverse('jobs_home'))
        
        #context = {"job_title": job_title[id], "job_description": job_description[id]}
        job = JobPost.objects.get(id=id)
        context = {"job": job}
        
        return render(request, "app/job_detail.html", context)
    

    #return HttpResponse(f"<h2>JOB DETAIL PAGE!!! {id}<h2>")
    #site = "https//:google.com"
    
    #return HttpResponse(f"visit here<a href={site}> Google</a>")
        # return_html = f"<h1>{job_title [id]}</h1> <h3>{job_description[id]}</h3>"
        #return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("Not Found")
     


