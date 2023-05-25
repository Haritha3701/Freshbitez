from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from product.models import products
from django.urls import reverse

class newproducts(Feed):
    title="Freshbitez"
    link="/latestproducts/"
    description="New Products in FreshBitez"
    def items(self):
        return products.objects.all()[:5]
    
    def item_title(self,data):
        return data.orgprice
    
    def item_description(self,data):
        return truncatewords(data.desc,10)
    
    def item_link(self):
        return reverse("homepage")