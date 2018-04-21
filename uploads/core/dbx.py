import os
import uuid
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

def db_upload(file_path, file_name=None):
    try:
        db_token = "_hWpEzHNy44AAAAAAAALXETklYeEysRczN2DcwbovSLWRtMyJ0RkYsdMJKKZz1cs"
        dbx = dropbox.Dropbox(db_token)
        target_path = '/dilumarriage'
        filename, file_extension = os.path.splitext(file_path)
        filename = os.sep.join([target_path, str(uuid.uuid4())])
        import pdb; pdb.set_trace()
        target_filename = ''.join([filename, file_extension ])
        with open(file_path, 'rb') as f:
                dbx.files_upload(f.read(), target_filename, mute=False)
        print "Dropbox upload complete"
        # dbx.files_upload(, target_path, mode=WriteMode('add'), autorename=True)
    except ApiError as err:
        print "Error uploading file to Dropbox"