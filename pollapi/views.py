from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Topic
from .serializers import TopicSerializer

@api_view(['GET', 'POST'])
def poll_list_create(request):
    if request.method == 'GET':
        polls = Topic.objects.all()
        serializer = TopicSerializer(polls, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def poll_detail(request, poll_id):
    try:
        poll = Topic.objects.get(pk=poll_id)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TopicSerializer(poll)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TopicSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def vote_agree(request, poll_id):
    try:
        poll = Topic.objects.get(pk=poll_id)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    poll.record_vote(is_agree=True)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def vote_disagree(request, poll_id):
    try:
        poll = Topic.objects.get(pk=poll_id)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    poll.record_vote(is_agree=False)
    return Response(status=status.HTTP_200_OK)
