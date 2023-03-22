from rest_framework import serializers

from accounts.models import Comment

class CommentSerializer(serializers.Serializer):
    content=serializers.CharField()
    # email=serializers.EmailField()
    created=serializers.DateTimeField()
    
    # class Meta:
    #   model=Comment
    #   fields=["id","content"]    
