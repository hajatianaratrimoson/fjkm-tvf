from django.urls import path 
from mpandraharaha.views import index

app_name = "mpandraharaha"

urlpatterns = [
    
    #Homepage
    path("", index, name="index"),
    
    #  #category
    # path("product/", product_list_view, name="product-list"),
    # path("product/<pid>/", product_detail_view, name="product-detail"),
    
    # #category
    # path("category/", category_list_view, name="category-list"),
    # path("category/<cid>/", category_product_list_view, name="category-product-list"),
    
    # # vendor 
    # path("vendors/", vendor_list_view, name="vendor-list"),
    
    # #tag
    # path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),
    
    # # Add Review
    # path("ajax-add-review/<int:pid>/", ajax_add_review, name="ajax-add-review")
]