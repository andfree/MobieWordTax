import decorator
from django.contrib import messages
from django.urls import resolve
from django.http.response import HttpResponseRedirect
from accounting.util import redirect_with_qs


@decorator.decorator
def trader_required(f, request, *args, **kwargs):
    if not request.user.current_trader:
        messages.add_message(request, messages.ERROR, '<strong>상호를 등록</strong>하면 모든 기능을 이용하실 수 있습니다.')
        return redirect_with_qs('/accounts', request)

    return f(request, *args, **kwargs)


@decorator.decorator
def client_required(f, request, *args, **kwargs):
    from accounting.models import Trader
    trader_id = kwargs.get('resource_id')
    if not trader_id:
        trader_id = args[0] if args else None

    trader = None
    if trader_id:
        trader = Trader.objects.filter(id=trader_id).first()

    if not trader:
        messages.add_message(request, messages.WARNING,
            '사업자[{}]가 존재하지 않습니다. 삭제된 사업자인지 확인해 주세요.'.format(trader_id))
        if 'trader' in request.session:
            del request.session['trader']
        return HttpResponseRedirect('/manager/')

    return f(request, *args, **kwargs)


def resolve_referer(request):
    return resolve(request.META['HTTP_REFERER'].replace(request.build_absolute_uri('/'), '/'))
