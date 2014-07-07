import webapp2
import os
from google.appengine.ext.webapp import template



class BaseHandler(webapp2.RequestHandler):
    def render_template(self, view_filename, params=None):
		if not params:
			params = {}
		path = os.path.join(os.path.dirname(__file__), 'templates', view_filename)
		self.response.out.write(template.render(path, params))




class MainPage(BaseHandler):
    def get_value(self):
        value=  self.request.get("text")
        value = list(value)

        return value

    def convert_value(self, list_value):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",	"i", "j", "k", "l", "m", "n", "o", "p",	"q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
        cAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        converted_value=""
        for element in list_value:

            if element.islower():
                indeks = alphabet.index(element)
                if indeks >= 13 and indeks <= 25:
                    indeks = indeks - 13
                else:
                    indeks = indeks + 13
                converted_value = converted_value + alphabet[indeks]

            if element.isupper():
                indeks = cAlphabet.index(element)
                if indeks >= 13 and indeks <= 25:
                    indeks = indeks - 13
                else:
                    indeks = indeks + 13
                converted_value = converted_value + cAlphabet[indeks]


            
        return converted_value


    def get(self):
        self.render_template("index.html")

    def post(self):
        listed_value = self.get_value()
        stavek = self.convert_value(listed_value)

        params = {"value":stavek}
        self.render_template("index.html", params)



application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)