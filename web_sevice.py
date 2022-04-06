# %%
from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import pandas as pd
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
# %%
friends_csv = pd.read_csv("Data\friends_episodes_v2.csv")
friends_csv.to_json("Data\friends.json")
FRIENDS = pd.read_json("Data\friends.json")
# create serial id for friends data




def abort_if_data_doesnt_exist(friends_id):
    if friends_id not in FRIENDS':
        abort(404, message=f'Friends id {friends_id} doesn\'t exist')

parser = reqparse.RequestParser()
parser.add_argument('Year_of_prod', type=int)
parser.add_argument('Season', type=int)
parser.add_argument('Episode_Title')
parser.add_argument('Duration', type=int)
parser.add_argument('Summary')
parser.add_argument('Director')
parser.add_argument('Stars')
parser.add_argument('Votes', type=float)


# Todo
# shows a single todo item and lets you delete a todo item
class Country(Resource):
    def get(self, country_id):
        abort_if_country_doesnt_exist(country_id)
        return COUNTRIES[country_id]

    def delete(self, country_id):
        abort_if_country_doesnt_exist(country_id)
        del COUNTRIES[country_id]
        return '', 204

    def put(self, country_id):
        args = parser.parse_args()
        content = {'name': args['name'], 'population': args['population']}
        COUNTRIES[country_id] = content
        return content, 201


class CountryList(Resource):
    def get(self):
        return COUNTRIES

    def post(self):
        args = parser.parse_args()
        country_id = max(COUNTRIES.keys()) + 1
        COUNTRIES[country_id] = {'name': args['name'], 'population': args['population']}
        return COUNTRIES[country_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(CountryList, '/country')
api.add_resource(Country, '/country/<int:country_id>')


if __name__ == '__main__':
    app.run(debug=True)