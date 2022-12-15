
from dishes.models import  items

#


item_names=[item.get("name") for item in items ]
# print(item_names)

# print categories

catgories=set([item.get("category") for item in items])
# print(catgories)

# veg items
# for item in items:
#     if(item.get("category")=="veg"):
#         print(item.get("name"))

veg_items=[i.get("name") for i in items if i.get("category")=="veg"]
# print(veg_items)

# veg items vaialble in range 100-300

veg_filter=[i.get("name") for i in items if i.get("category")=="veg" and i.get("price") in range(200,301)]


best_item=max(items,key=lambda i:i.get("rating"))
print("best",best_item)

costly_item=max(items,key=lambda i:i.get("price"))
print("costly",costly_item)

chep_pro=min(items,key=lambda i:i.get("price"))
print("lo",chep_pro)


sorted_products=sorted(items,key=lambda i:i.get("price"),reverse=True)
print(sorted_products)