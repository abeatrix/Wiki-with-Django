from django.shortcuts import render
import markdown2
from . import util


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
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    else:
        return search(request)


def edit(request):
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    else:
        return search(request)

def delete(request):
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    else:
        return search(request)


def random(request):
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    else:
        return search(request)
