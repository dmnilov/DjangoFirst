from django.shortcuts import render, HttpResponse, Http404

from MainApp.models import Item

from django.core.exceptions import ObjectDoesNotExist

name = "Дмитрий"
surname = "Нилов"
faname = "Алексеевич"
tel = "8-123-600-0102"
mail = "vasya@mail.ru"



def about(request):
    context = {
        "name": "Дмитрий",
        "surname": "Нилов",
        "faname": "Алексеевич",
        "tel": "8-123-600-0102",
        "mail": "vasya@mail.ru",

    }
    return render(request, "about.html", context)


def home(request):
    return render(request, "index.html")


def item_home(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items.html", context)

    # items_result = "<ol>"
    # for item in items:
    #     items_result += "<li>" + f"<a href='/item/{item['id']}'>" + item["name"] + "</a>" + "</li>"
    # items_result += "</ol>"
    # return HttpResponse({items_result})


def item_page(request, id):
    try:
        item = Item.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404(f"Товар с ID={id} не найден")
    context = {"item": item}
    return render(request, "item.html", context)


