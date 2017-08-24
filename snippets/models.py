from django.db import models

# Snippet model. Will have one-to-many relationship with Content
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ('created',)


# Snippet content model. Where code is actually stored
class File(models.Model):
    title = models.CharField(max_length=100, blank=True)
    snippet_id = models.ForeignKey(Snippet, related_name='files', on_delete=models.CASCADE) # Create relationship with Snippet, related name will be used in serializer
    description = models.CharField(max_length=250, blank=True)
    language = models.CharField(max_length=100, default='none')
    code = models.TextField(blank=True)

    class Meta:
        ordering = ('title',)