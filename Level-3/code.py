import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass

        # defends against path traversal attacks
        if path.startswith('/') or path.startswith('..'):
            return None

        # builds path
        #print("TSTE: " + __file__)
        base_dir = os.path.dirname(os.path.abspath(__file__))

        #print("Base Dir: " + base_dir)
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))
        #print("prof_picture_path: " + prof_picture_path)

        #Mine
        #GOOD -- Verify with normalised version of path
        if not prof_picture_path.startswith(base_dir):
            return None

        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None

        if not path:
            raise Exception("Error: Tax form is required for all users")

        #My solution
        #print("PATH: " + path)
        #if path.startswith('/') or path.startswith('..'):
        #    raise Exception("Error: Path starts with / or ..")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        #print("BASE DIR: " + base_dir)

        base_dir_path = path[:len(base_dir)]
        #print("BASE DIR PATH: " + base_dir)

        if base_dir!=base_dir_path:
            return None


        file_after_basedir = path[len(base_dir):]
        #print("AFTRE BASE DIR: " + file_after_basedir)

        if file_after_basedir.startswith("."):
            #print("LLLLLLLLL")
            return None

        if file_after_basedir.endswith(".pdf") == False:
            return None

        #if not path.startswith(base_dir):
        #    return None
            #raise Exception("Error: Tax form is required for all users")
        #print("PATH: " + path)

        with open(path, 'rb') as form:
            tax_data = bytearray(form.read())

        # assume that tax data is returned on screen after this
        return path
