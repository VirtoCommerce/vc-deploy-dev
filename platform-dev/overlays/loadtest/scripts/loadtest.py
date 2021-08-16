import requests
import json
import os
import subprocess
import shlex
import shutil
import datetime

tag = os.environ.get('RELEASE_TAG')
benchmark_test = os.environ.get('TEST')
benchmark_repo = os.environ.get('REPO')
api_token = os.environ.get('AUTH_TOKEN')
jmeter_bin = '/home/vcadmin/jmeter/apache-jmeter-5.4.1/bin/jmeter'
brach_location = '~/loadtest'
rusults_dir = './results'
result_file_name = 'loadtest-result-{}-{}'.format(tag, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))
result_file_name_jtl = result_file_name + '.jtl'
git = f'git clone {benchmark_repo}'
loadtest = f'sh {jmeter_bin} -n -t {benchmark_test} -l {rusults_dir }/{result_file_name_jtl}'
post_data = {
  'tag_name': f'{tag}',
  'target_commitish': 'loadtest',
  'name': f'Loadtest result {tag}'
}
owner = "VirtoCommerce"
repo = "vc-deploy-dev"
query_url = f"https://api.github.com/repos/{owner}/{repo}/releases"
post_headers = headers = {
    'Authorization': f'token {api_token}',
    'Accept': 'application/vnd.github.v3+json'
}

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, text=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc



def github_release(file_name):
    response = requests.post(query_url, json.dumps(post_data, indent = 2), headers=post_headers)
    print(response.json())
    release_id = (response.json()['id'])
    if response.status_code == 201:
        print(f'Release {release_id} created')
        asset = open(f'{file_name}', 'rb')
        upload_query_url = f"https://uploads.github.com/repos/{owner}/{repo}/releases/{release_id}/assets?name={file_name}"
        upload_response = requests.post(upload_query_url, files={"archive": ("index.zip", asset)}, headers=post_headers)
    if upload_response.status_code == 201:
        print(f'File {file_name} uploaded')
        print(f'https://github.com/{owner}/{repo}/releases/tag/{tag}')

def main():
    run_command('rm -rf vc-benchmark')
    run_command(git)
    run_command(loadtest)
    shutil.make_archive(result_file_name, 'zip', rusults_dir, result_file_name_jtl)
    output_filename = result_file_name + '.zip'
    github_release(output_filename)
    os.remove(output_filename)

if __name__ == '__main__':
    main()