import json
import tornado.ioloop
import tornado.web
import tornado.websocket
from handler import handler
from tts import speak

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("views/index.html")

class PlanHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("views/plan.html")

class QueryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("views/query.html")

class TTSHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("views/tts.html")

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Websocket opened!")

    def on_message(self, message):
        """
            Message type:
            0: Check Connection
            1: Explain Query Execution Plan; Input: Query
            2: Explain Query Execution Plan; Input: Plan
            3: Text to speech
        """
        payload = json.loads(message)
        result = handler(payload)
        self.write_message(result)
        speak(result)

    def on_close(self):
        print("Websocket Closed!")

def make_app():
    return tornado.web.Application([
            (r"/", MainHandler),
            (r"/plan", PlanHandler),
            (r"/query", QueryHandler),
            (r"/tts", TTSHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': "./static"}),
            (r"/websocket", EchoWebSocket),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

