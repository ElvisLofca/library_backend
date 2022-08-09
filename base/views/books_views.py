from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.models import Book
from base.serializers import BookSerializer
from rest_framework import status
from datetime import datetime


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_book(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_book(request):
    data = request.data
    if Book.objects.filter(title=data['title']).exists():
        print('Book with this name already exists')
        return Response({'detail': 'Book with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

    del data['image']
    published_at = data['published_at']
    published_at = datetime.strptime(published_at, "%Y-%m-%d").date()
    try:
        serializer = BookSerializer(data=data, many=False)
        if serializer.is_valid():
            book = Book(
                title=data['title'],
                author=data['author'],
                body=data['body'],
                description=data['description'],
                genre=data['genre'],
                pages=data['pages'],
                published_at=published_at,
                is_available=data['is_available']
            )
            book.save()
            serializer = BookSerializer(book, many=False)
            return Response(serializer.data)
        print(serializer.errors, 'ERROR')
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(e, 'EXCEPTION')
        return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_book(request, pk):
    data = request.data

    del data['image']
    published_at = data['published_at']
    published_at = datetime.strptime(published_at, "%Y-%m-%d").date()

    try:
        serializer = BookSerializer(data=request.data, many=False)
        if serializer.is_valid():
            Book.objects.filter(pk=pk).update(
                    title=data['title'],
                    author=data['author'],
                    body=data['body'],
                    description=data['description'],
                    genre=data['genre'],
                    pages=data['pages'],
                    published_at=published_at,
                    is_available=data['is_available'],
                )
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({'error': "object not updated"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(e)
        return Response({'error': "object not updated", 'message': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def upload_book_image(request, pk):
    data = request.FILES
    try:
        if data['image']:
            book = Book.objects.get(pk=pk)
            book.image = data['image']
            book.save()
            serializer = BookSerializer(book, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': "Format not supported"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e, "Exception")
        return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_book(request, pk):

    try:
        book = Book.objects.get(id=pk)
        book.delete()
    except Exception as e:
        print(e, "Exception")
        return Response({'detail': "Something went wrong. Book not deleted"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': "Book deleted correctly."})
