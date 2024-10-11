from mitmproxy import ctx, http
import json

class XiaoYuanKouSuan:
    def request(self, flow):
        if (flow.request.url.find("https://xyks.yuanfudao.com/leo-game-pk/%7Bclient%7D/math/pk/match") != -1):
            flow.request.url = flow.request.url.replace("%7Bclient%7D", "android")
            print("Fix request url to", flow.request.url)
    
    def response(self, flow):
        if (flow.request.url.find("https://xyks.yuanfudao.com/leo-math/android/exams") != -1 or flow.request.url.find("https://xyks.yuanfudao.com/leo-game-pk/android/math/pk/match") != -1):
            response = json.loads(flow.response.get_text())
            response["questionCnt"] = 1
            response["questions"] = [
                {
                    "id": 1,
                    "content": "9+\\square=12",
                    "answer": "1",
                    "userAnswer": None,
                    "answers": [ "1" ],
                    "script": None,
                    "wrongScript": None,
                    "status": 0,
                    "errorState": 0,
                    "costTime": 0
                }
            ]
            flow.response.set_text(json.dumps(response))
            print("Modified!");
            
addons = [
    XiaoYuanKouSuan()
]