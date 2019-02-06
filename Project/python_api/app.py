"""
Cloud Computing Implementation
Brian R Kabuye
02/05/2018
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse
import re

app = Flask(__name__)
api = Api(app)

messages = [
    {
        "name": "smith",
        "messages": {"amber": ["find", "friend"]},
    },
    {
        "name": "anna",
        "messages": {"smith": ["why", "racecar"]},
    },
    {
        "name": "amber",
        "messages": {"anna": ["Red rum, sir, is murder"]},
    },
    {
        "name": "joel",
        "messages": {"tom": ["abba", "racecar"]},
    },
]


class MessageList(Resource):
    @staticmethod
    def get():
        dic = {"messages": []}
        for message in messages:
            for key, value in message["messages"].items():
                print("{0} received {1} messages from {2}:\n {3}".format(message["name"], len(value), key,','.join(value)))
                dic["messages"].append({
                    "name": message["name"],
                    "messages": {key: [','.join(value)]},
                })
        if len(dic) < 1:
            return "{0} Bad connection or missing {1}".format(401, 404)
        else:
            return dic, 200

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('sender', required=True)
        parser.add_argument('receiver', required=True)
        parser.add_argument('message', required=True)
        args = parser.parse_args()
        name_status = [message["name"].lower() for message in messages if message["name"].lower() == args["receiver"].lower()]
        if args["receiver"].lower() in name_status:
            for x in range(0, len(messages)):
                if messages[x]["name"].lower() == name_status[0].lower():
                    messages[x]["messages"][args["sender"]] = [messages[x]["messages"].get(name_status[0], args["message"])]
        else:
            messages.append({
                "name": args["receiver"],
                "messages": {args["sender"]: [args["message"]]}
            })
        return messages, 201


class Message(Resource):

    def put(self, data):
        parser = reqparse.RequestParser()
        parser.add_argument('sender', required=True)
        parser.add_argument('old_message', required=True)
        parser.add_argument('new_message', required=True)
        args = parser.parse_args()
        count = 0
        name_status = [message['name'].lower() for message in messages if str(data).lower() == message['name'].lower()]
        if str(data).lower() in name_status:
            for x in range(0, len(messages)):
                if messages[x]['name'] == str(data).lower():
                    for key, value in messages[x]["messages"].items():
                        for i in range(0, len(value)):
                            if value[i].lower() == args["old_message"].lower() and key.lower() == args["sender"].lower():
                                value[i] = value[i].replace(value[i], args["new_message"].lower())
                                count += 1
            if count < 1:
                return "Not Found", 404
            else:
                return messages, 201
        else:
            return "Not Found", 404

    def get(self, data):
        count = 0
        dic = {"messages": []}
        for message in messages:
            for key, value in message["messages"].items():
                if str(data) in value:
                    count += 1
                    status = self.__palindrome(str(data))
                    if status is True:
                        dic["messages"].append({
                            "name": message["name"],
                            "messages": {key: [','.join(value)]},
                            "palindrome": status
                        })
                        count += 1
                    else:
                        dic["messages"].append({
                            "name": message["name"],
                            "messages": {key: [','.join(value)]},
                            "palindrome": status
                        })
                else:
                    pass
        if count < 1:
            return "Not found", 404
        else:
            return dic, 200

    @staticmethod
    def delete(data):
        global messages
        count = 0
        for message in messages:
            for key, value in message["messages"].items():
                if str(data) in value:
                    message["messages"][key] = [x for x in value if str(data).lower() != x]
                    count += 1
        if count < 1:
            return "Not Found", 404
        else:
            return messages, 201

    @staticmethod
    def __palindrome(data):
        hold = re.sub("[^a-zA-Z0-9]+", "", data).lower()
        if len(hold) < 1:
            return False
        count = int(len(hold) / 2)
        for i in range(0, count):
            if ''.join(sorted(hold[i].lower())) != ''.join(sorted(hold[len(hold) - (i + 1)].lower())):
                return False
        return True


api.add_resource(Message, "/message/<string:data>")
api.add_resource(MessageList, "/messageList/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
