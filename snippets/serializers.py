from django.forms import widgets
from rest_framework import serializers
from rest_framework.response import Response
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    def to_representation(self, value):
        # print value
        # print value.title
        # print value.code
        return value.title
        # return Snippet.objects.get(pk=value.pk)

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')




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