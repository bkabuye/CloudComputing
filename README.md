# Messaging Api Service
## Description
All responses will be in this format.
```json
 {
   "name": "String type holding the name of the receiver from the response",
   "messages": "HashMap hold string type key from the sender and value string array holding the message list"
 }
```
Subsequent response definitions will only detail the expected value of the 'message fields'
### List received messages
**Definition**

` GET /messageList/`

**Response**
- '200 OK' on success
```json
{
  "messages": [
    {
      "name": "smith",
      "messages": {"amber": ["find,friend,when is amber coming back?"] }
    },
    {
      "name": "anna",
      "messages": {"smith": ["why,legal"]}
    }
  ]
}
```
**Definition**

` GET /message/data`

**Arguments**
- `"data":string` a specific message on demand to determine if it is a palindrome.

**Response**
- '200 OK' on success
```json
{
  "messages": [
    {
      "name": "joel",
      "messages": {
      "tom": ["tell, racecar"]
      },
      "palindrome": true
    }
  ]
}
```
### Post messages
**Definition**

` POST /messageList/`

**Arguments**

- `"receiver":string` a globally unique identifier for the receivers account.
- `"sender":string` a senders account.
- `"message":string` message sent by the sender.

**Response**

- `201 Created` on success

- `404 Not Found` if the old message does not exist

```json
{
  "messages": [
    {
      "name": "Brian",
      "messages": {
        "Arthur": [
          "When is amber coming back?"
        ]
      },
      "Status": "Success"
    }
  ]
}
```
**Definition**

` PUT /message/data`

**Arguments**
- `data` a globally unique identifier for the receivers account to updated.
- `old_message:string` string parameter for message to be replaced.
- `new_message:string` string parameter for value to replace.

**Response**

- `201 OK` on update.
```json
[{
    "name": "arthur",
    "messages": {"brian": ["Tell me where is maryland?"]}
  }]
```
######
### Delete messages
**Definition**

` DELETE /message/data`

**Arguments**
- `"data":string` string message to be deleted.

**Response**

- `204 No Content` on success

- `404 Not Found` if the the old message does not exist

```json
{
  "messages": [
    {
      "name": "Brian",
      "messages": {
        "Arthur": [
          "When is amber coming back?"
        ]
      },
      "Status": "Success"
    }
  ]
}
```
####Build, Deploy, Test & Access

**Tools**

- `Docker` a program used to perform operating system-level containerization.
- `Insomnia Rest` . is a free and open source cross-platform REST Client.
- `Python 3**` is an interpreted, high-level, general-purpose programming language.

**Imported Libraries**

- `flask` is a micro-framework written in python.
- `flask_restful` . an extension of flask that adds support when quickly building REST APIs.
- `re` this is a third-party regex module with an API used to string manipulation.

**Build**
- Run and Install Docker.
- Start running Docker.
- Using Terminal for mac or linux or command prompt for windows, navigate to the "Project" folder.
- Type 'Docker-compose build' and enter. Wait until installation is successfully complete and the panel displays following image.(This command builds the source and libraries to be used in docker)
![Alt text]

**Run**

- Type 'Docker-compose Up' and hit enter. Wait until installation is successfully complete and this panel displays following image.(This command excutes and runs python code)
![Alt text]
- Either use a regular browser or Insomnia or Postman.

**Test**

*Using browser/Insomnia/Postman*

- Navigate to GET http://localhost:5000/messageList/
- This will list all the messages sent to each receiver and the sender.

*Using Insomnia/Postman*

- Navigate to POST http://localhost:5001/messageList/
- This will post json data or messages sent to the receiver from the sender.

*Using Insomnia/Postman*
- Navigate to PUT http://localhost:5001/message/receiver
- This will update messages sent to the receiver by the sender.

*Using Insomnia/Postman*
- Navigate to GET http://localhost:5001/message/text
- This will return a specified existing text and determine if it is palindrome.

*Using Insomnia/Postman*
- Navigate to DELETE http://localhost:5001/message/text
- This will remove a specified text sent to any receiver by the sender.








