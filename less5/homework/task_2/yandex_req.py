import requests
from Token import TOKEN


class YaUploader:
    token = TOKEN

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disc_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers(self=YaUploader)
        params = {'path': disc_file_path, 'overwrite': 'true'}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disc(self, disc_file_path, file_name):
        href = self.get_upload_link(self=YaUploader, disc_file_path=disc_file_path).get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

    def create_folder(self, dir_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
        headers = self.get_headers()
        params = {"path": dir_name, "overwrite": "true"}
        response = requests.put(upload_url, headers=headers, params=params)
        if response.status_code != 201:
            return "Error"
        return response.status_code

    def get_info_dir(self, dir_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": dir_name}
        response = requests.get(upload_url, headers=headers, params=params, timeout=10)
        if response.status_code != 200:
            return "Error"
        dirname = response.json()["name"]
        type_dir = response.json()["type"]
        return dirname, type_dir, response.status_code


if __name__ == '__main__':
    uploader = YaUploader(token=TOKEN)
    new_dir_name = "test_folder"
    resp_create_folder = uploader.create_folder(new_dir_name)
    resp_get_info = uploader.get_info_dir(new_dir_name)