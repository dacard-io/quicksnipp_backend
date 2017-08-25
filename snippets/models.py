from django.db import models

'''
Schema is as follows:
    Everything is pulled from user data
    User (One-to-Many) >> Group (One-to-Many) >> Snippet (One-to-Many) >> File
'''

# Code Group/collection model. Will have one-to-many relationship with Snippet
class Group(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=250, blank=True)
    label_color = models.CharField(max_length=7, blank=True) # Will hold hex value (7 characters including # pound symbol)!

    class Meta:
        ordering = ('title',)

# Snippet model. Will have one-to-many relationship with Content
class Snippet(models.Model):
    group_id = models.ForeignKey(Group, related_name='snippets', on_delete=models.CASCADE, null=True, blank=True) #I'm allowing blanks to allow uncategorized snippets
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