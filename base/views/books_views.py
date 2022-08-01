import sys

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
    # user = request.user
    data = request.data


    try:
        published_at = data['published_at']
        published_at = datetime.strptime(published_at, "%Y-%m-%d").date()
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            body=data['body'],
            description=data['description'],
            genre=data['genre'],
            pages=data['pages'],
            published_at=published_at,
            is_available=data['is_available'],
        )
    except Exception as e:
        print(e, "Exeption")
        return Response({'detail': "This book already exists"}, status=status.HTTP_400_BAD_REQUEST)

    book.save()

    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_book(request, pk):
    data = request.data

    published_at = data['published_at']
    published_at = datetime.strptime(published_at, "%Y-%m-%d").date()

    try:
        Book.objects.filter(id=pk).update(
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
        book.save()
    except Exception as e:
        print(e, "Exeption")
        return Response({'error': "object not updated", 'message': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def upload_book_image(request, pk):
    data = request.FILES

    try:
        book = Book.objects.get(pk=pk)
        book.image = data['image']
        book.save()


        print(data['image'])
    except Exception as e:
        print(e, "Exeption")
        print('exeption in image')
        return Response({'detail': "Image not uploaded"}, status=status.HTTP_400_BAD_REQUEST)

    book = Book.objects.get(pk=pk)

    print(book.image)

    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_book(request, pk):

    try:
        book = Book.objects.get(id=pk)
        book.delete()
    except Exception as e:
        print(e, "Exeption")
        return Response({'detail': "Something went wrong. Book not deleted"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': "Book deleted correctly."})




