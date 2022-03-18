#!/usr/bin/env python3

import urllib.request, json, fileinput, re

repoList = [
    'VirtoCommerce/vc-module-core',
    'VirtoCommerce/vc-module-azure-search',
    'VirtoCommerce/vc-module-cart',
    'VirtoCommerce/vc-module-catalog',
    'VirtoCommerce/vc-module-content',
    'VirtoCommerce/vc-module-customer',
    'VirtoCommerce/vc-module-elastic-search',
    'VirtoCommerce/vc-module-export',
    'VirtoCommerce/vc-module-image-tools',
    'VirtoCommerce/vc-module-inventory',
    'VirtoCommerce/vc-module-lucene-search',
    'VirtoCommerce/vc-module-marketing',
    'VirtoCommerce/vc-module-notification',
    'VirtoCommerce/vc-module-order',
    'VirtoCommerce/vc-module-payment',
    'VirtoCommerce/vc-module-pricing',
    'VirtoCommerce/vc-module-search',
    'VirtoCommerce/vc-module-shipping',
    'VirtoCommerce/vc-module-sitemaps',
    'VirtoCommerce/vc-module-store',
    'VirtoCommerce/vc-module-subscription',
    'VirtoCommerce/vc-module-tax',
    'VirtoCommerce/vc-module-customer-review',
    'VirtoCommerce/vc-module-Authorize.Net',
    'VirtoCommerce/vc-module-avatax',
    'VirtoCommerce/vc-module-catalog-personalization',
    'VirtoCommerce/vc-module-catalog-publishing',
    'VirtoCommerce/vc-module-catalog-csv-import',
    'VirtoCommerce/vc-module-contentful',
    'VirtoCommerce/vc-module-bulk-actions',
    'VirtoCommerce/vc-module-quote',
    'VirtoCommerce/vc-module-dynamic-associations',
    'VirtoCommerce/vc-module-experience-api',
    ]    

for repo in repoList:
    with urllib.request.urlopen('https://api.github.com/repos/{}/releases'.format(repo)) as url:
        data = json.loads(url.read().decode())
        downloadUrl = data[0]['assets'][0]['browser_download_url']
        print('{}: {}'.format(repo, downloadUrl))

        for line in fileinput.input('deployment-cm.yaml', inplace=1):
            print(re.sub(r"(\"PackageUrl\":\ \")(...+{}/...+)(\")".format(repo), r'\1{}\3'.format(downloadUrl), line), end='')