from haystack import indexes
from myapp.models import Course


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    code = indexes.CharField(model_attr='code')

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
