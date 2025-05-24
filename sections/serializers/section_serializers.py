from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from sections.models import Section, Content
from sections.serializers.content_serializers import SectionContentSerializer


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SectionListSerializer(ModelSerializer):
    sections_content_title = SerializerMethodField()

    def get_sections_content_title(self, section):
        return SectionContentSerializer(Content.object.filter(section=section), many=True).data

    class Meta:
        model = Section
        fields = ('id', 'title', 'sections_content_title')