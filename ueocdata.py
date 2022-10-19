from ueocdata import create_app

ueoc_data = create_app()

if __name__ == '__main__':
    ueoc_data.run(debug=True)
