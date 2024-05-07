from minio import Minio
from dotenv import load_dotenv
# import osload_dotenv()
# LOCAL_FILE_PATH = os.environ.get('LOCAL_FILE_PATH')
# ACCESS_KEY = os.environ.get('ACCESS_KEY')
# SECRET_KEY = os.environ.get('SECRET_KEY')
LOCAL_FILE_PATH = "test.csv"
ACCESS_KEY = "admin"
SECRET_KEY = "password"
MINIO_API_HOST = "http://localhost:9000"
MINIO_CLIENT = Minio("localhost:9000", access_key=ACCESS_KEY,
                     secret_key=SECRET_KEY, secure=False)


def main():
    found = MINIO_CLIENT.bucket_exists("huditest")
    if not found:
        MINIO_CLIENT.make_bucket("huditest")
    else:
        print("Bucket already exists")


MINIO_CLIENT.fput_object("huditest", "test.csv", LOCAL_FILE_PATH,)
print("It is successfully uploaded to bucket")
