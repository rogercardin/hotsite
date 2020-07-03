from django.shortcuts import render,redirect
from combate.models import Post
from combate.forms import PostForm


def lista(request):
        lista = Post.objects.all().order_by('-id')
        return render(request,'combate/lista.html',{'lista_posts':lista})

def novo(request):
        form = PostForm(request.POST or None)
        if request.method == 'POST':
          if form.is_valid():
             form.save()
             return redirect(lista)

        return render(request,'combate/novo.html',{'form':form})

def atualiza(request,id):
        post=Post.objects.get(id=id)
        form=PostForm(request.POST or None, instance=post)

        if form.is_valid():
           form.save()
           return redirect(lista)
        return render(request,'combate/novo.html',{'form':form})

def deletar(request,id):
        post=Post.objects.get(id=id)
        post.delete()
        return redirect(lista)


