from django.urls import reverse,reverse_lazy
from django.views.generic import (
ListView,
CreateView,
UpdateView,
DeleteView
)
from .models import Item, List
class ListListView(ListView):
    model = List
    template_name = "core/index.html"
    
class ItemListView(ListView):
    model = Item
    template_name = "core/todo_list.html"
    def get_queryset(self):
        return Item.objects.filter(list_id=self.kwargs["list_id"])
    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = List.objects.get(id=self.kwargs["list_id"])
        return context
class ListCreate(CreateView):
    model = List
    fields = ["title"]
    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context
    def get_success_url(self):
        return reverse("index")
class ItemCreate(CreateView):
    model = Item
    fields = [
    "list",
    "title",
    "description",
    "due_date",
    ]
    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = List.objects.get(id=self.kwargs["list_id"])
        initial_data["list"] = todo_list
        return initial_data
    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = List.objects.get(id=self.kwargs["list_id"])
        context["list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.list_id])
class ItemUpdate(UpdateView):
    model = Item
    fields = [
        "list",
    "title",
    "description",
    "due_date",
    ]
    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["list"] = self.object.list
        context["title"] = "Edit item"
        return context
    def get_success_url(self):
        return reverse("list", args=[self.object.list_id])
    
class ItemDelete(DeleteView):
    model = Item
    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.list_id])
class ListDelete(DeleteView):
    model = List
    def get_success_url(self) -> str:
        return reverse_lazy("index")

    