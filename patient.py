from bottle import get, post, request,route, run, template,put,delete
pat_dict = {}
disp_list=[]

@route('/')
@route('/patient')
def patient():
    return '<b>Its working... create, update, delete</b>!'

@post('/patient')
def create():
    pid = request.POST['id']
    pname = request.POST['name']
    pgender = request.POST['gender']
    page = request.POST['age']
    paddress = request.POST['address']
    pphone = request.POST['phone']
    disp_list = ' '.join([pname,pgender,page,paddress,pphone])
    pat_dict.update({pid:disp_list})
    return pat_dict

@get('/patient/<id>')
def read(id):
    return pat_dict[id]

@put('/patient/<id>')
def update(id):
    pname = request.POST['name']
    pgender = request.POST['gender']
    page = request.POST['age']
    paddress = request.POST['address']
    pphone = request.POST['phone']
    update_patient=[pname,pgender,page,paddress,pphone]
    pat_dict[id]=update_patient
    return pat_dict

@delete('/patient/<id>')
def delete(id):
    del(pat_dict[id])
    return "Deleted Sucessfully"

run(host='localhost', port=8080)

