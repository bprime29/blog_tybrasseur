from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Recette, Methode, Ingredient, Etape, Empatage, Ebullition, Fermentation, Photo
from .forms import PostForm, RecetteForm, EtapeFormset, IngredientFormset, ImageFormset
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


# Recettes
TYPE_CHOICES = ['1','2','3','4'];
def allrecettes(request):

    recettes = Recette.objects.all().order_by('-id');
    typeObjet=None
    if request.method == 'GET':
        if request.GET.get('type'):
            if request.GET['type'] in TYPE_CHOICES:
                type = request.GET['type']
                typeObjet = Methode.objects.get(id=type)
                recettes = Recette.objects.filter(type=type);
    paginator = Paginator(recettes, 10)
    page = request.GET.get('page')
    try:
        recettes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        recettes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        recettes = paginator.page(paginator.num_pages)
    contexte = {
        'typeObjet': typeObjet,
        'recettes': recettes,
    }
    return render(request, 'blog/allrecettes.html', contexte)

def recette(request, id):

    recette = Recette.objects.get(id=id)
    etapes = Etape.objects.filter(recette=id)
    ingredients = Ingredient.objects.filter(recette=id)
    etapes_empatage = Empatage.objects.filter(recette=id)
    etapes_ebullition = Ebullition.objects.filter(recette=id)
    etapes_fermentation = Fermentation.objects.filter(recette=id)
    photos = Photo.objects.filter(recette=id)
    contexte = {
        'recette'    : recette,
        'etapes'     : etapes,
        'ingredients': ingredients,
        'etapes_empatage': etapes_empatage,
        'etapes_ebullition': etapes_ebullition,
        'etapes_fermentation': etapes_fermentation,
        'photos'     : photos,
    }
    return render(request, 'blog/affiche-recette.html', contexte)

def nouvelleRecette(request):

    form = RecetteForm()
    IngredientForm = IngredientFormset()
    EtapeForm = EtapeFormset()
    ImageForm = ImageFormset()

    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            recette = form.save()
            recette.user = request.user
            recette.save()
            IngredientForm = IngredientFormset(request.POST,instance=recette)
            if IngredientForm.is_valid():
                IngredientForm.save()
                EtapeForm = EtapeFormset(request.POST,instance=recette)
                if EtapeForm.is_valid():
                    EtapeForm.save()
                    ImageForm = ImageFormset(request.POST,request.FILES,instance=recette)
                    if ImageForm.is_valid():
                        ImageForm.save()
                        return render(request, "blog/nouvelle-recette.html", {
                            'form': form,
                            'IngredientForm': IngredientForm,
                            'EtapeForm': EtapeForm,
                            'ImageForm': ImageForm,
                            'success_message':'success'
                        })

    return render(request, "blog/nouvelle-recette.html", {
        'form': form,
        'IngredientForm': IngredientForm,
        'EtapeForm': EtapeForm,
        'ImageForm':ImageForm,
    })