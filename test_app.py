import app

def test_main():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == 'main page'

def test_mongodb():
    web = app.app.test_client()

    rv = web.post('/mongodb', data={ "text": "foo bar" })
    #assert rv.status == '200 OK'
    #assert rv.data.decode('utf-8') == 'done'

    rv = web.get('/mongodb')
    assert rv.status == '200 OK'
    print(rv.data)
    #assert rv.data.decode('utf-8') == 'done'

