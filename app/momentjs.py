# encoding: utf8

from jinja2 import Markup


class Momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, frmt):
        return Markup("""
        <script>
            document.write(moment(\"{}\").{});
        </script>
        """.format(self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), frmt))

    def format(self, fmt):
        return self.render('format(\"{}\")'.format(fmt))

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")