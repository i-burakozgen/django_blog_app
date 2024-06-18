from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    # one to many relation one user can have multiple posts but post can have one user
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    # for print post with title on table 
    def __str__(self):
        return self.title

# CREATE TABLE "blog_post"
# (
#     "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
#     "title" varchar(150) NOT NULL, "content" text NOT NULL,
#     "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
#     );
# CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
# COMMIT