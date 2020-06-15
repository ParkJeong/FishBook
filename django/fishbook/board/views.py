import datetime

from django.db.models import F, Max
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Board
from users.models import User
import json
import pdb

PAGESIZE=10
# Create your views here.

def list(request, page=1):
    kwd = request.GET.get('kwd')
    if kwd == None or kwd is '' or kwd == 'null':
        start = (page - 1) * PAGESIZE
        board_count = Board.objects.count()
        boardlist = Board.objects.all().order_by('-groupno', 'orderno')[start:start+PAGESIZE]
    else:
        start = (page - 1) * PAGESIZE
        board_count = Board.objects.filter(title__contains=kwd).count()
        boardlist = Board.objects.filter(title__contains=kwd).order_by('-groupno', 'orderno')[start:start+PAGESIZE]

    data = {
        'boardlist': boardlist,
        'board_count': board_count,
        'current_page': page,
        'page': page,
    }

    kwd = request.GET.get('kwd')
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd

    return render(request, 'board/list.html', data)

# 게시글 작성

def writeform(request, no=-1, page=1):
    # 인증
    authuser = request.session.get('authUser')
    if authuser is None:
        return HttpResponseRedirect('board/list')

    if no == -1:
        return render(request, 'board/write.html', {"page":page})
    else:
        data = {"no":no, "page":page}
        kwd = request.GET.get('kwd')
        if kwd is None:
            data['kwd'] = json.dumps(kwd)
        else:
            data['kwd'] = kwd
        return render(request, 'board/write.html', data)

def write(request, page=1):
    # 인증
    authuser = request.session.get('authUser')
    if authuser is None:
        return HttpResponseRedirect('board/list')

    board = Board()
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.user = User.objects.get(email=request.session['authUser']['email'])

    # 새글 작성하기
    if request.POST.get('no') == '-1':
        value = Board.objects.aggregate(max_groupno=Max('groupno'))
        if value.get('max_groupno') is None:
            value['max_groupno'] = 0
        board.groupno = value.get('max_groupno') + 1
        board.save()
    else:
        board2 = Board.objects.get(email=request.POST.get('no'))
        Board.objects.filter(orderno__gte=board2.orderno+1).update(orderno=F('orderno')+1)
        board.groupno = board2.groupno
        board.orderno = board2.orderno + 1
        board.depth = board2.depth + 1
        board.save()
    data = {
        'page': 1
    }
    kwd = request.GET.get('kwd')
    print(kwd, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd
    # if kwd is '':
    #     return HttpResponseRedirect(f'/board/list/{page}')
    return HttpResponseRedirect(f'/board/list/{page}?kwd={kwd}')
# 상세보기
def view(request, no=0, page=1):
    if no == 0:
        return HttpResponseRedirect('list')

    board = Board.objects.filter(id=no)

    data = {
        'board':board[0],
        'page': page,
    }

    kwd = request.GET.get('kwd')
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd

    response = render(request, 'board/view.html', data)

    if request.session.get('authUser') is None:
        cookie_name = 'hit'
    else:
        cookie_name = f'hit:{request.session["authUser"]["email"]}'
        cookie_name = cookie_name[:cookie_name.find('@')]

    tomorrow = datetime.datetime.replace(datetime.datetime.now(), hour=23, minute=59, second=0)
    expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")

    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(no) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{no}', expires=expires)
            board.update(hit=F('hit')+1)
            return response
    else:
        response.set_cookie(cookie_name, no, expires=expires)
        board.update(hit=F('hit')+1)
        return response

    return render(request, 'board/view.html', data)

# 수정 및 삭제
def modifyform(request, no=0, page=1):
    board = Board.objects.filter(id=no)[0]
    authuser = request.session.get('authUser')
    if authuser is None or board.user.email != authuser['email']:
        return HttpResponseRedirect('board/list')

    data = {
        'board': board,
        'page': page,
    }

    kwd = request.GET.get('kwd')
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd

    return render(request, 'board/modify.html', data)

def modify(request, page=1):
    board_id = request.POST['id']
    board = Board.objects.get(id=board_id)
    authuser = request.session.get('authUser')
    if authuser is None or board.user.email != authuser['email']:
        return HttpResponseRedirect('board/list')

    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    data = {
        'board': board,
        'page': page,
    }

    kwd = request.GET.get('kwd')
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd

    return HttpResponseRedirect(f'/board/{board_id}/{page}', data)

def delete(request, no=0, page=1):
    board = Board.objects.get(id=no)

    authuser = request.session.get('authUser')
    if authuser is None or board.user.email != authuser['email']:
        return HttpResponseRedirect('board/list')

    board.title = "삭제된 글입니다."
    board.save()
    return HttpResponseRedirect(f'/board/list/{page}')
