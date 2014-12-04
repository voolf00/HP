from django.shortcuts import render, render_to_response
from models import Article
from django.core.paginator import Paginator
from django.http import HttpResponse, StreamingHttpResponse
from django.core import serializers
from  django.contrib import auth
# Create your views here.


def uArticles(request, page_number=1):
    text = {}

    all_obj = Article.objects.all()
    current_page = Paginator(all_obj.order_by("id"), 200)
    # text['objects'] = serializers.serialize('xml', current_page.page(page_number))
    text['articles'] = current_page.page(page_number)
    return render_to_response('article.html', text)


def uArticle(request, article_id):
    args = {}
    args['title'] = 'article'

    if auth.get_user(request).is_superuser:
        XMLSerializer = serializers.get_serializer("xml")
        xml_serializer = XMLSerializer()
        xml_serializer.serialize(Article.objects.all()[int(article_id) - 1:article_id])
        data = xml_serializer.getvalue()

        return StreamingHttpResponse(data)
    else:
        return StreamingHttpResponse("error")