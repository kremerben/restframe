from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight =

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')



    # pk = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False,
    #                               allow_blank=True,
    #                               max_length=100)
    # code = serializers.CharField(style={'type': 'textarea'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
    #                                    default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES,
    #                                 default='friendly')
    #
    # def create(self, validated_attrs):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_attrs)
    #
    # def update(self, instance, validated_attrs):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_attrs.get('title', instance.title)
    #     instance.code = validated_attrs.get('code', instance.code)
    #     instance.linenos = validated_attrs.get('linenos', instance.linenos)
    #     instance.language = validated_attrs.get('language', instance.language)
    #     instance.style = validated_attrs.get('style', instance.style)
    #     instance.save()
    #     return instance