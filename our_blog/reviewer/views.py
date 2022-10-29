from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from reviewer.models import reviewer

# Create your views here.

def create_reviewer(request, name: str, last_name: str):

    template = loader.get_template("template_reviewer.html")

    reviewer = reviewer(name=name, last_name=last_name)
    reviewer.save()  # save into the DB

    context_dict = {"reviewer": reviewer}
    render = template.render(context_dict)
    return HttpResponse(render)


def reviewers(request):
    reviewers = reviewer.objects.all()

    context_dict = {"reviewers": reviewers}

    return render(
        request=request,
        context=context_dict,
        template_name="reviewer/reviewer_list.html",
    )
