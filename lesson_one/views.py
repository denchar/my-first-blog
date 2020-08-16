from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect
from django.template import loader, Context, context
from django.template.loader import get_template
from .models import Article, Comment


def view(request):
    view = "template_two"
    view2 = " charden "
    html = get_template("myview.html").render({
        'name': view,
        'secondname': view2,
        "title": "My Title",
    })

    return HttpResponse(html)


def show(request):
    latest_articles_list = Article.objects.order_by("-pub_date")[:5]
    my_response = ""
    liston = ""
    for a in latest_articles_list:
        comment_list = a.comment_set.order_by("id")
        comments_list = " comments_list : ["
        for c in comment_list:
            comments_list += '{ author_name : \"' + c.author_name + '\", comment_text : \"' + c.comment_text + '\" },'

        comments_list = comments_list[0:-1]
        comments_list += ']'
        liston += '{ article_title :\"' + a.article_title + '\", ' + comments_list + '},'
    liston = liston[0:-1]
       # my_response += liston
       # my_response = my_response[0:-1]
    return HttpResponse(liston)


def show2(request):
    sname = "second name write"
    return HttpResponse(get_template("myview.html").render({"name": 0, "secondname": sname}))
