from rest_framework import serializers

from .models import Event, Category, Comment, Artist


class CategoryList(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, чтобы выводились только parent"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ArtistListSerializer(serializers.ModelSerializer):
    """Вывод списка артистов и организаторов"""

    class Meta:
        model = Artist
        fields = ('id', 'nickname', 'image')


class ArtistDetailSerializer(serializers.ModelSerializer):
    """Вывод детализации артиста или организатора"""

    class Meta:
        model = Artist
        fields = "__all__"


class EventListSerializer(serializers.ModelSerializer):
    category = CategoryList()

    class Meta:
        model = Event
        fields = ('title', 'descrtption', 'category', 'event_date')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ('name', 'text', 'children')


class EventDetailSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    organizer = ArtistListSerializer(read_only=True, many=True)
    artists = ArtistListSerializer(read_only=True, many=True)
    place = serializers.SlugRelatedField(slug_field='title', read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Event
        exclude = ('is_draft', 'is_past')
