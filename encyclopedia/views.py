from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })




def entry(request, Title):
    entry_data = util.get_entry(Title)

    if entry_data == None:
        return render(request, "encyclopedia/error.html", {
            "error_msg": "This encyclopedia name is Invalid, Please Check the encyclopedia name ."
        })
    return render(request, "encyclopedia/entry.html", {
        "entry_data": entry_data,
        "entry_title": Title
    })



def random_entry(request):
    r_entry = util.list_entries()
    entr = random.choice(r_entry)

    return HttpResponseRedirect(f'/entry/{entr}')



def search(request):
    e_name = request.GET["e_name"]
    all_e = util.list_entries()

    if e_name in all_e:
        return HttpResponseRedirect(f'/entry/{e_name}')
    return render(request, "encyclopedia/error.html", {
        "error_msg" : "this entry name is invalid."
    })


def new(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/new.html")

    title = request.POST["title-a"]
    content = request.POST["entry-d"]

    if title and content :
        util.save_entry(title, content)
        return HttpResponseRedirect('/')
    return render(request, "encyclopedia/error.html", {
        "error_msg" : "Please Make sure that filled the title and content feilds"
    })


def edit(request, title):
    if request.method == "GET":
        cont = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "content" : cont,
            "title": title
        })
    e_content = request.POST.get("edit_content")
    util.save_entry(title, e_content)
    return HttpResponseRedirect(f'/entry/{title}')
















###
