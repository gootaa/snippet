from django.db import models
from accounts.models import User
from .languages import languages
from django.core.urlresolvers import reverse


class Snippet(models.Model):
	LANGUAGES = languages
	EXPOSURE = (
		('public','Public'),
		('private','Private'),
	)

	author = models.ForeignKey(User, related_name='snippets')
	raw_text = models.TextField()
	title = models.CharField(max_length=150, blank=True)
	time_added = models.DateTimeField(auto_now_add=True)
	time_updated = models.DateTimeField(auto_now=True)
	syntax_highlighting = models.CharField(max_length=50,
											choices=LANGUAGES,
											default='none')
	exposure = models.CharField(max_length=20,
								choices=EXPOSURE,
								default='public')

	class Meta:
		ordering = ('-time_updated',)

	def __str__(self):
		return self.title + ' by ' + self.author.username

	def get_absolute_url(self):
		return reverse('snippet_detail', args=[self.id,])
