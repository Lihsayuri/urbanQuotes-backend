from django.shortcuts import render, redirect
import requests
from .models import Quote
from .models import Tag
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import QuoteSerializer, TagSerializer
from django.http import JsonResponse
import json

@api_view(['GET', 'POST'])
def api_quotes(request):
    if request.method == 'POST':
        print("ENTREI")
        new_quote_data = request.data
        quote = Quote()
        # quote.id = new_quote_data['id']
        quote.frase = new_quote_data['frase']
        quote.autor = new_quote_data['autor']
        # quote.tag = new_quote_data['tags']
        quote.save()

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    querystring = {"language_code":"pt"}

    headers = {
        'x-rapidapi-host': "quotes15.p.rapidapi.com",
        'x-rapidapi-key': "4a3bce6d8cmsh044349ed231bf95p15f17ajsn846aa4e94d98"
    }

    r = requests.get(url , querystring, headers=headers)
    quote_json = r.json()

    print(quote_json)
    # id = quote_json['id']
    frase = quote_json['content']
    autor = quote_json['originator']['name']
    tags = quote_json['tags'] #LISTA de tags, os números não aparecem
    
    dictFrase = {"frase":frase, "autor": autor, "tags":tags}

    # jsonFrase = json.dumps(dictFrase, ensure_ascii=False)
    # print("ESSE É O DICT: ", jsonFrase)

    return JsonResponse(dictFrase)


@api_view(['GET', 'POST'])
def api_minhasQuotes(request):
    if request.method == 'POST':
        new_quote_data = request.data
        new_tag_data = request.data
        quote = Quote()
        tag = Tag()
        tags = new_quote_data['tags']
        lista_de_tags = tags.split(",")
        quote.frase = new_quote_data['frase']
        quote.autor = new_quote_data['autor']
        quote.save()

        for i in range(len(lista_de_tags)):
            elemento = Tag(tag=lista_de_tags[i])
            elemento.save()
            quote.tags.add(elemento)
            
        print("QUOTE.TAGS", quote.tags)

   
        # quote.tags.set(lista_de_tags)
        quote.save()

    quotes = Quote.objects.all()
    serialized_quote = QuoteSerializer(quotes, many=True)
    return Response(serialized_quote.data)


def index(request):
    if request.method == 'POST':
        frase = request.POST.get('frase')
        autor = request.POST.get('autor')
        # tagNome = request.POST.get('tags')

        # request.add(tagNome)
        quote = Quote(frase = frase, autor = autor)
        quote.save()
        return redirect('index')
    else:
        all_quotes = Quote.objects.all()
        all_tags = Tag.objects.all()
        print(all_quotes)
        return render(request, 'quotes/index.html', {'quotes': all_quotes, 'tags': all_tags})


# print(tags)

    # new_quote = Quote()
    # new_tag = Tag()

    # new_quote.id = id
    # new_quote.frase = frase
    # new_quote.autor = autor
    # new_tag.tag = tags

    # print(new_tag)
  
    # quotes = Quote.objects.all()
    # serialized_quote = QuoteSerializer(new_quote)
    # return Response(serialized_quote.data)