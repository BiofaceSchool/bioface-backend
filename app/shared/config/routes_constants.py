from ...Auth.auth_constants import AUTH_TAG, AUTH_ENDPOINT
from ...University.config.university_constants import UNIVERSITY_TAG, UNIVERSITY_ENDPOINT
from ...Faculties.config.faculty_constants import FACULTY_TAG, FACULTY_ENDPOINT
from ...Campus.config.campus_constants import CAMPUS_TAG, CAMPUS_ENDPOINT
from ...Camera.config.face_encoding_constants import FACE_ENCODING_TAG, FACE_ENCODING_ENDPOINT
# routes
PREFIX = '/api/v1'

# AUTH ROUTES
AUTH_TAG = AUTH_TAG
AUTH_ROUTE = PREFIX + AUTH_ENDPOINT

# UNIVERSITY ROUTES
UNIVERSITY_TAG = UNIVERSITY_TAG
UNIVERSITY_ROUTE = PREFIX + UNIVERSITY_ENDPOINT

# FACULTY ROUTES
FACULTY_TAG = FACULTY_TAG
FACULTY_ROUTE = PREFIX + FACULTY_ENDPOINT

# Campus routes
CAMPUS_TAG = CAMPUS_TAG
CAMPUS_ROUTE = PREFIX + CAMPUS_ENDPOINT

# Face encoding routes
FACE_ENCODING_TAG = FACE_ENCODING_TAG
FACE_ENCODING_ROUTE = PREFIX + FACE_ENCODING_ENDPOINT

