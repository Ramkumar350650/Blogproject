from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):

	"""docstring for ClassName"""
	class Meta:
		model=Post
		abstract=True
		fileds='__all__'
		
class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model=Comment
		abstract=True
		fileds='__all__'
