#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2
import csv

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	try:
    		template = JINJA_ENVIRONMENT.get_template('templates%s' % self.request.path)
    		logging.info("Determing which page to render")

    		if self.request.path == '/projects.html':
    			self.response.write(template.render())
    			logging.info("Projects template rendered")
    		if self.request.path =='/contact.html':
    			self.response.write(template.render())
    			logging.info("Contact template rendered)")
    		if self.request.path == '/journey.html':
    			self.response.write(template.render())
    			logging.info("Journey template rendered")
    		if self.request.path == '/home.html':
    			self.response.write(template.render())
    			logging.info("Home template rendered")
    	except:
    		template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        	self.response.write(template.render())
        	logging.info("No path requested, page rendered manually to Home template")

    def post(self):
        try:
            reason = self.request.get("reason")
            logging.info(reason)
            email = self.request.get("email")
            message = self.request.get("message")
            outfile = open("contactdata.csv" , "w")
            outfile.write( "%s, %s, %s\n" % (email, reason, message))
            outfile.close()
            template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        except:
            logging.info("csv file could not be created")
            template = JINJA_ENVIRONMENT.get_template('templates/home.html')
    
            	

    						
    			


app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/home.html', MainHandler),
	('/journey.html', MainHandler),
	('/contact.html', MainHandler),
	('/projects.html', MainHandler)
], debug=True)
