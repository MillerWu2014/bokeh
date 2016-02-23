import boto
import os

from boto.s3.key import Key as S3Key
from boto.exception import NoAuthHandlerFound
from os.path import join

from .constants import job_id
from .utils import ok, fail


def upload_file_to_s3_by_job_id(file_path, content_type="text/html"):
    """
    Uploads a file to bokeh-travis s3 bucket under a job_id folder
    """
    s3_filename = join(job_id, file_path)
    return upload_file_to_s3(file_path, s3_filename)


def upload_file_to_s3(file_path, s3_filename, content_type="text/html"):
    """
    Uploads a file to bokeh-travis s3 bucket.
    """

    s3_bucket = "bokeh-travis"
    s3 = "https://s3.amazonaws.com/%s" % s3_bucket

    try:
        conn = boto.connect_s3()
        bucket = conn.get_bucket(s3_bucket)
        with open(file_path, "r") as f:
            contents = f.read()
        key = S3Key(bucket, s3_filename)
        key.set_metadata("Content-Type", content_type)
        key.set_contents_from_string(contents, policy="public-read")
        ok("Access upload at: %s" % (join(s3, s3_filename)))

    except NoAuthHandlerFound:
        fail("Upload was requested but could not connect to S3.")

    except OSError:
        fail("Upload was requested but file %s was not available." % file_path)