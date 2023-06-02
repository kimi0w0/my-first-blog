# views.pyはモデルとテンプレートの橋渡し
from django.shortcuts import render,get_object_or_404 # get_list_or_404もあるので間違えないこと
from .models import Post # 同じディレクトリなら.で代用できる
from django.utils import timezone

# Create your views here.
def post_list(request):
    # クエリセットをつくり、blogの記事を取り出す
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # {}内に指定した情報を、テンプレートが表示
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})


