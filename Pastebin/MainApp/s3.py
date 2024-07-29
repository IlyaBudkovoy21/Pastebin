from contextlib import asynccontextmanager
from django.conf import settings

from aiobotocore.session import get_session


class ClientS3:
    def __init__(self, access_key: str, secret_key: str, endpoint_url: str, bucket_name: str):
        self.config = {'aws_access_key_id': access_key, 'aws_secret_access_key': secret_key,
                       'endpoint_url': endpoint_url}
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(
            self,
            file_path: str
    ):
        object_name = file_path.split('/')[-1]
        async with self.get_client() as client:
            with open(object_name, 'rb') as file:
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key=object_name,
                    Body=file
                )


client = ClientS3(
    access_key=settings.AWS_ACCESS_KEY_ID,
    secret_key=settings.AWS_SECRET_ACCESS_KEY,
    endpoint_url='https://s3.storage.selcloud.ru',
    bucket_name='my_container'
)
