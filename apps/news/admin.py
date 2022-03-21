from django import forms
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from news.models import NewsPost, WhatWeAreReadingLink


class NewsPostForm(forms.ModelForm):
    model = NewsPost
    fields = [
        'title',
        'body',
        'source',
        'is_cover_story',
        'publish_date',
        'topics',
        'active',
    ]


class NewsPostAdmin(SummernoteModelAdmin):
    form = NewsPostForm
    list_display = ['title', 'site', 'is_cover_story', 'active', 'has_topics']
    list_editable = ['is_cover_story', 'active']
    readonly_fields = ['site', ]
    summernote_fields = ['body', ]
    
    
class WhatWeAreReadingLinkForm(forms.ModelForm):
    model = WhatWeAreReadingLink
    fields = [
        'title',
        'source',
        'link',
        'publish_date',
    ]


class WhatWeAreReadingLinkAdmin(SummernoteModelAdmin):
    form = WhatWeAreReadingLinkForm
    list_display = ['title', 'site', 'is_cover_story', 'active', 'has_topics']
    list_editable = ['is_cover_story', 'active']
    readonly_fields = ['site', ]
    summernote_fields = ['body', ]
    

admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(WhatWeAreReadingLink, WhatWeAreReadingLinkAdmin)
