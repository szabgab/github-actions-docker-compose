import app

def test_main():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.encode('utf-8') == 'main page'

