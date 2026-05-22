from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

def item_list(request):
    item_type = request.GET.get('type')

    if item_type:
        items = Item.objects.filter(item_type=item_type)
    else:
        items = Item.objects.all()

    items = items.order_by('-date_posted')

    return render(request, 'board/item_list.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        item_type = request.POST['item_type']
        location = request.POST['location']
        contact = request.POST['contact']

        Item.objects.create(
            title=title,
            description=description,
            item_type=item_type,
            location=location,
            contact=contact
        )
        return redirect('item_list')

    return render(request, 'board/add_item.html')


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'board/item_detail.html', {'item': item})

def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('item_list')