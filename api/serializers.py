from rest_framework import serializers
from api.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Post
        fields= ["post_title", "body", "results","upvotes","downvotes","boast_or_roast", "date", "id"]

    
    

    