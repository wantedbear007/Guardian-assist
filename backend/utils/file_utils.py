

ALLOWED_FILE_TYPES = {'pdf'}

def allowed_file_types(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_TYPES
    