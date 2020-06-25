from django.shortcuts import render

from articles.models import Article, FieldScope, ArticleField


def data_prepare(articles, fields, articles_fields):
    for item in articles:
        item.update(field_name=[])
        for article_field in articles_fields:
            for field in fields:
                if (item['id'] == article_field['article_id']) and (field['id'] == article_field['field_id']):
                    item['field_name'].append(dict(topic=field['name'], is_main=article_field['is_main_bool']))
    return articles


def articles_list(request):
    template = 'articles/news.html'
    context = {
        'object_list': data_prepare(Article.objects.values().order_by('-published_at').all(),
                                    FieldScope.objects.values().all(),
                                    ArticleField.objects.order_by('-is_main_bool').values().all()),
    }
    return render(request, template, context)
