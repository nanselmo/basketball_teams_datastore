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

import os
import webapp2
from google.appengine.ext import ndb

class MainHandler(webapp2.RequestHandler):
    def get(self):

        class Team(ndb.Model):
            city = ndb.StringProperty()
            name = ndb.StringProperty()

        class Player(ndb.Model):
            team = ndb.KeyProperty(kind='Team')
            last_name= ndb.StringProperty()
            position = ndb.StringProperty()

        da_bulls= Team(city='Chicago', name='Bulls')
        bulls_key = da_bulls.put()

        drose = Player(team=bulls_key,last_name='Rose', position='Point Guard')
        joakim = Player(team=bulls_key,last_name='Noah', position='Center')


        drose.put()
        joakim.put()

        lakers= Team(city='Los Angeles', name='Lakers')
        lakers_key = lakers.put()

        shaq = Player(team=lakers_key,last_name='O\'Neal', position='Center')
        kobe = Player(team=lakers_key,last_name='Bryant', position='Point Guard')

        shaq.put()
        kobe.put()

        

        player_query = Player.query(Player.team==bulls_key)
        player_data = player_query.fetch()
        for player in player_data:
            self.response.out.write('<p>'+player.last_name+'</p>')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
