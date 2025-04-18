from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("process_request")

        # ログイン画面の場合、Continue実行
        if request.path == "/userlogin/":
            return None

        # 戻り値なし or Noneを返す場合、次のミドルウェアを実行する
        
        # 他の画面の場合、セッション情報認証を実施する
        info_dict = request.session.get('info')
        if info_dict:
            return None
        else:
            return redirect("/userlogin/")
    def process_response(self, request, response):
        print("process_response")
        return response