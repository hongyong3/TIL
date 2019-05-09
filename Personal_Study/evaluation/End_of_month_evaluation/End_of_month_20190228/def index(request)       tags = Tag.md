```python
def index(request):
       tags = Tag.objects.all()
       return render(request, 'web/index.html', {'tags':tags})
   
   def create(request):
       title = request.POST.get('title')
       content = request.POST.get('content')
       
       tag = Tag(title=title, content=content)
       tag.save()
       
       return redirect(index)
       
   def delete(request, pk):
       tag = Tag.objects.get(pk=pk)
       tag.delete()
       return redirect(index)
```

