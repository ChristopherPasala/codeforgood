from flask_restful import Resource

# Login
class Login(Resource):
    def post(self):
        print("Login")
        args = parser.parse_args()
        print(args)
        username = args['username']
        password = args['password']
        print(username, password)

        if username is None or password is None:
            abort (400)