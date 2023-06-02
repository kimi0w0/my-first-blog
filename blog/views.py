# views.pyはモデルとテンプレートの橋渡し
from django.shortcuts import render,get_object_or_404,redirect # get_list_or_404もあるので間違えないこと
from .models import Post # 同じディレクトリなら.で代用できる
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    # クエリセットをつくり、blogの記事を取り出す
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # {}内に指定した情報を、テンプレートが表示
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,pk): # urlsからpkを受け取る
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})


