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
# Para funcionar precisa atribuir um id (sequencial) a cada linha do csv/objeto do json




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
class Friends(Resource):
    def get(self, friends_id):
        abort_if_data_doesnt_exist(friends_id)
        return FRIENDS[friends_id]

    def delete(self, friends_id):
        abort_if_data_doesnt_exist(friends_id)
        del FRIENDS[friends_id]
        return '', 204

    def put(self, friends_id):
        args = parser.parse_args()
        content = {'Year_of_prod': args['Year_of_prod'], 
                    'Season': args['Season'], 
                    'Episode_Title': args['Episode_Title'],
                    'Duration': args['Duration'],
                    'Summary': args['Summary'],
                    'Director': args['Director'],
                    'Stars': args['Stars'],
                    'Votes': args['Votes']}
        FRIENDS[friends_id] = content
        return content, 201


class FriendsList(Resource):
    def get(self):
        return FRIENDS

    def post(self):
        args = parser.parse_args()
        friends_id = max(FRIENDS.keys()) + 1
        FRIENDS[friends_id] = {'Year_of_prod': args['Year_of_prod'], 
                                'Season': args['Season'], 
                                'Episode_Title': args['Episode_Title'],
                                'Duration': args['Duration'],
                                'Summary': args['Summary'],
                                'Director': args['Director'],
                                'Stars': args['Stars'],
                                'Votes': args['Votes']}
        return FRIENDS[friends_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(FriendsList, '/friends')
api.add_resource(Friends, '/friends/<int:friends_id>')


if __name__ == '__main__':
    app.run(debug=True)