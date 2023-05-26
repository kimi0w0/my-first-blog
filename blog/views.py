# views.pyはモデルとテンプレートの橋渡し
from django.shortcuts import render
from .models import Post # 同じディレクトリなら.で代用できる
from django.utils import timezone

# Create your views here.
def post_list(request):
    # クエリセットをつくり、blogの記事を取り出す
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # {}内に指定した情報を、テンプレートが表示
    return render(request,'blog/post_list.html',{'posts':posts})


