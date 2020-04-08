from chalice import Chalice

app = Chalice(app_name='lambda-postgres')
# See .chalice/config.json for Subnet and SG settings

@app.route('/')
def index():
    from remote_postgres import RemotePostgres
    from chalicelib import mysecrets
    db = RemotePostgres(f'postgres://{mysecrets.pg_user}:{mysecrets.pg_password}@{mysecrets.pg_host}:{mysecrets.pg_port}/{mysecrets.pg_database}')
    counts = db.get_counts()
    del db
    return counts

@app.route('/select', methods=['POST'])
def select():
    from remote_postgres import RemotePostgres
    from chalicelib import mysecrets
    db = RemotePostgres(f'postgres://{mysecrets.pg_user}:{mysecrets.pg_password}@{mysecrets.pg_host}:{mysecrets.pg_port}/{mysecrets.pg_database}')
    if not (app.current_request.json_body and 'select_statement' in app.current_request.json_body):
        return {'Syntax': 'curl -X POST $(chalice url)select -d @select.json -H "Content-Type: application/json"'}
    else:
        records = db.select(app.current_request.json_body['select_statement'])
        del db
        return records


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
