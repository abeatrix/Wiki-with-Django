from django.shortcuts import render, redirect
import markdown2
from . import util
from random import shuffle

def index(request):
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    else:
        return search(request)


def entry(request, title):
    if request.method == "GET":
        try:
            content = util.get_entry(title)
            data = {"title": title.strip(), "content": markdown2.markdown(content).strip()}
            return render(request, "encyclopedia/entry.html", data)
        except TypeError:
            data = {"errors": "title not found"}
            return render(request, "encyclopedia/error.html", data)
    else:
        return search(request)


def search(request):
    query = request.POST["q"].lower()
    warning = ""
    if util.get_entry(query):
        data = {"title": query,"content": markdown2.markdown(util.get_entry(query))}
        return render(request, "encyclopedia/entry.html", data)
    else :
        entries = util.list_entries()
        results = list(filter(lambda e: query in e.lower(), entries))
        if not results:
            warning = "0 search result for: "
        data = {"query": query, "results": results, "warning": warning}
        return render(request, "encyclopedia/search.html", data)



def create(request):
    if request.method == "GET":
        data = { "entries": util.list_entries() }
        return render(request, "encyclopedia/create.html", data)
    else:
        title_form = request.POST.get('title')
        content_form = request.POST.get('content')
        if not util.get_entry(title_form):
            util.save_entry(title_form, content_form)
            return redirect("entry", title=title_form)
        else:
            data = {"errors": "Entry with the same name exists"}
            return render(request, "encyclopedia/error.html", data)


def edit(request, title):
    if request.method == "GET":
        content = util.get_entry(title)
        data = {"title": title.strip(), "content": markdown2.markdown(content).strip()}
        return render(request, "encyclopedia/edit.html", data)
    else:
        content_form = request.POST.get('content')
        util.save_entry(title, content_form)
        return redirect("entry", title)


def random(request):
    entries = util.list_entries()
    if entries:
        print(shuffle(entries))
        ran = entries[0]
        return redirect("entry", title=ran)
    else:
        data = {"errors": "this wiki is empty"}
        return render(request, "encyclopedia/error.html", data)
