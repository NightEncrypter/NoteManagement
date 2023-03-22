from rest_framework.response import Response
from accounts.models import Comment
from accounts.api.serializers import CommentSerializer
from rest_framework.decorators import api_view
def login(request):
    data=["manas","john"]
    return Response(data)

def comment(request):
    
    comment=Comment.objects.all()
    print(comment,"comment")
    serializer=CommentSerializer(instance=comment,data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    print(serializer.data)
    
    # serializer=Comment(data)
    return Response()

@api_view(["GET"])
def getComments(request):
    # comment=Comment()
    comment=Comment.objects.all()
    # print(comment,"comment")
    serializer=CommentSerializer(instance=comment,many=True)
    print(repr(serializer))
    # print(serializer.data)
    return Response(serializer.data)