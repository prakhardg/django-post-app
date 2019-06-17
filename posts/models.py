from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add= False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)



    def __str__(self):
        return self.title

    def get_abs_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
        # return "/posts/%s" %(self.id)

    def edit_post(self):
        return reverse("posts:update", kwargs={"id":self.id})

    def return_to_list(self):
        return reverse("posts:list")

    def delete_post(self):
        return reverse("posts:delete", kwargs={"id":self.id})