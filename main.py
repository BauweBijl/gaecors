from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os

class MainPage(webapp.RequestHandler):
  def get(self):
    self.redirect('/index.html')

class CORSEnabledHandler(webapp.RequestHandler):
	def get(self, path):
		path = os.path.join(os.path.dirname(__file__), 'static', path.split('/')[-1])
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
# any type
		self.response.headers['Content-Type'] = '*.*'
		self.response.out.write(open(path, 'rb').read())

application = webapp.WSGIApplication(

        [('/(.+)$', CORSEnabledHandler),
        ('/', MainPage)], 
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

