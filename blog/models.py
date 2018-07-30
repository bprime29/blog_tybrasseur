from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# POST

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

# RECETTES

class Recette(models.Model):
    user = models.ForeignKey(User, default=1, editable=False)
    type = models.ForeignKey('Methode', null=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    real_date = models.DateField(null=True)
    volume = models.IntegerField(null=True)
    dens_init = models.IntegerField(null=True)
    dens_final = models.IntegerField(null=True)
    color = models.IntegerField(null=True)
    amertume = models.IntegerField(null=True)
    alcool = models.IntegerField(null=True)

    def __str__(self):
        return self.titre


class Photo(models.Model):
    recette = models.ForeignKey('Recette', null=True, editable=False)
    image = models.ImageField(
        upload_to="photos_brassins",
        max_length=100
    )
    thumbnail = models.ImageField(
        upload_to="photos_brassins",
        max_length=500,
        null=True,
        blank=True
    )

    def create_thumbnail(self):
        if not self.image:
            return

        from PIL import Image
        from io import BytesIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os

        THUMBNAIL_SIZE = (346, 195)

        DJANGO_TYPE = self.image.file.content_type

        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
        image = Image.open(BytesIO(self.image.read()))

        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = BytesIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
        self.thumbnail.save(
            '%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION),
            suf,
            save=False
        )

    def save(self, *args, **kwargs):

        self.create_thumbnail()

        force_update = False

        # If the instance already has been saved, it has an id and we set
        # force_update to True
        if self.id:
            force_update = True

        # Force an UPDATE SQL query if we're editing the image to avoid integrity exception
        super(Photo, self).save(force_update=force_update)



class Ingredient(models.Model):
    recette = models.ForeignKey('Recette', null=True,editable=False)
    nom = models.CharField(max_length=100)
    quantite = models.CharField(max_length=100)
    typ = models.CharField(max_length=100)
    caracteristique = models.CharField(max_length=100)


class Etape(models.Model):
    recette = models.ForeignKey('Recette', null=True, editable=False)
    detail = models.CharField(max_length=150)


class Empatage(models.Model):
    recette = models.ForeignKey('Recette', null=True, editable=False)
    emp_tag = models.ForeignKey('Etape_empatage', null=True)
    emp_detail = models.CharField(max_length=150)


class Etape_empatage(models.Model):
    title_empatage = models.CharField(max_length=256)
    label_empatage = models.CharField(max_length=100,default='Label')
    detail_empatage = models.TextField()

    def __str__(self):
        return self.title_empatage

class Ebullition(models.Model):
    recette = models.ForeignKey('Recette', null=True, editable=False)
    ebu_tag = models.ForeignKey('Etape_ebullition', null=True)
    ebu_detail = models.CharField(max_length=150)


class Etape_ebullition(models.Model):
    title_ebullition = models.CharField(max_length=256)
    label_ebullition = models.CharField(max_length=100,default='Label')
    detail_ebullition = models.TextField()

    def __str__(self):
        return self.title_ebullition

class Fermentation(models.Model):
    recette = models.ForeignKey('Recette', null=True, editable=False)
    ferm_tag = models.ForeignKey('Etape_fermentation', null=True)
    ferm_detail = models.CharField(max_length=150)


class Etape_fermentation(models.Model):
    title_fermentation = models.CharField(max_length=256)
    label_fermentation = models.CharField(max_length=100,default='Label')
    detail_fermentation = models.TextField()

    def __str__(self):
        return self.title_fermentation

class Methode(models.Model):
    title = models.CharField(max_length=256)
    label = models.CharField(max_length=100,default='Label')
    detail = models.TextField()

    def __str__(self):
        return self.title