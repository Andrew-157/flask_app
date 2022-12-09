from app import create_app

app = create_app('config.LocalConfig')
app.run(debug=True)
