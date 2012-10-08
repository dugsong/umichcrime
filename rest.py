#!/usr/bin/env python

import json, logging

from google.appengine.ext import webapp

import base, dps

class RestHandler(base.BaseHandler):
    def get(self):
        month = self.request.get('month')
        day = self.request.get('day')
        year = self.request.get('year')

        try:
            d = dps.incident_log(month, day, year)
            self.response.out.write(json.dumps(d))
        except:
            logging.info('nyan')
            self.redirect('http://nyan.cat')

app = webapp.WSGIApplication([
        (r'/rest/.*', RestHandler),
    ], debug=True)
