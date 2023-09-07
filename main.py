from flask import Flask ,request ,jsonify


app =Flask(__name__)
@app.route('/users' ,methods=['GET'])
def get_users():
     return jsonify({'users':users})
@app.route('/user/<int:id>',methods =['GET'])

def get_user(id):
   for user in users:
    if user['id'] == id:
      return jsonify(user)
   return jsonify({'error':'user not found '})
users = [{
   'id' : 1,
   'name':'chaimae',
   'age':26 ,
   'job':'dev'},
   {
   'id': 2,
   'name':'mery',
   'age':26 ,
   'job':'opti'}]
@app.route('/users',methods=['POST'])

def add_user():
  request_body = request.get_json()
  data = {
    'id'  : request_body['id'],
    'name': request_body['name'],
    'name': request_body['name'],
    'age':request_body['age'],
    'job':request_body['job']}
  users.append(data)
  return jsonify(data)

@app.route('/users/<int:id>',methods = ['PUT'])
def update_user(id):
  for user in users:
   if user['id'] == id: 
    request_body =request.get_json() 
    user['name']= request_body['name']
    user['age']= request_body['age']
    user['job']= request_body['job']      
    return jsonify(user['name'])
  return jsonify({'error':'user not found '})

@app.route('/users/<string:name>',methods =['DELETE'])
def delete_user(name):
   for index ,user in enumerate(users):
    if user[name] == name:
       del users[index]
       returnjsonify({'message':'User Deleted'})
   return jsonify({'error':'user not found'}) 
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0',debug=True)

