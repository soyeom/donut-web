from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "57edd379bad5f3fa9facbef3c15d231e",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "german",    # 유저 아이디
            "item_name": "연어초밥",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "100",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/pay/approval/",
            "cancel_url": "https://naver.com",
            "fail_url": "https://naver.com",
        }

        res = requests.post(URL, headers=headers, params=params)
        request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)


    return render(request, 'payapp/index.html')


def approval(request):
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "57edd379bad5f3fa9facbef3c15d231e",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "1001",     # 주문번호
        "partner_user_id": "german",    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }
    return render(request, 'payapp/approval.html', context)