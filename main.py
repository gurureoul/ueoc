from ueocdata import create_app

app = create_app()

if __name__ == '__main__':
    # 'app' gets imported by the wsgi, so having this in main
    # shouldn't run on the production server
    app.run(debug=True)
