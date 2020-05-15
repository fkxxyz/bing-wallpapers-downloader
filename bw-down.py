#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import requests
import urllib
import os
import argparse


default_name_format = '{d}_{n}_{r}.jpg'
default_resolution = 'UHD'


def getImagesInfo(idx, n):
    url = 'https://www.bing.com/HPImageArchive.aspx'
    params = {
        'format': 'js',
        'idx': idx,
        'n': n,
    }
    
    return requests.get(url, params = params).json()['images']


def formatInfo(info):
    def getName(urlbase):
        ns = urllib.parse.parse_qsl(urlbase)[0][1]
        return ns[ns.find('.')+1:ns.find('_')]
    
    return {
        'date': info['enddate'],
        'name': getName(info['urlbase']),
        'urlbase': info['urlbase'],
    }


SupportedResolutionsList = [
    'UHD',
    '1920x1200',
    '1920x1080',
    '1366x768',
    '1280x768',
    '1024x768',
    '800x600',
    '800x480',
    '768x1280',
    '720x1280',
    '640x480',
    '480x800',
    '400x240',
    '320x240',
    '240x320',
]
SupportedResolutions = set(SupportedResolutionsList)
def getImageUrl(urlbase, resolution):
    if resolution not in SupportedResolutions:
        return None
    return 'https://www.bing.com' + urlbase + '_' + resolution + '.jpg'


def saveImage(path, formatted_info, resolution, name_format):
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.isdir(path):
        return
    
    save_path = name_format.replace('{d}', formatted_info['date'])
    save_path = save_path.replace('{n}', formatted_info['name'])
    save_path = save_path.replace('{r}', resolution)
    save_path = path + os.sep + save_path
    if os.path.exists(save_path):
        return
        
    url = getImageUrl(formatted_info['urlbase'], resolution)
    if url is None:
        return
        
    print('Save to ' + save_path + ' from ' + url)
    
    response = requests.get(url)
    if response.status_code // 100 != 2:
        return
    
    open(save_path, 'wb').write(response.content)


def main(args):
    infos = getImagesInfo(0, args.count)
    formatted_infos = list(map(formatInfo, infos))
    for formatted_info in formatted_infos:
        saveImage(args.output, formatted_info,
            args.resolution, args.name_format)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Download daily' + \
        ' wallpapers from Bing website.')
    parser.add_argument('output', help = 'Destination path')
    parser.add_argument('--name-format', '-n',
        help = 'File name format. ' + \
        'Use the following parameters to name: ' + \
        '{d} is date, {n} is image name, {r} is resolution. ' + \
        'The default is ' + default_name_format,
        default = default_name_format)
    parser.add_argument('--resolution', '-r', help = 'Resolution. ' + \
        'The default is ' + default_resolution + '.',
        default = default_resolution,
        choices = SupportedResolutions)
    parser.add_argument('--count', '-c',
        help = 'How many days past pictures to download. ' + \
        'Maximum value is 8. The default is 8. Minimum value is 1.',
        default = 8,
        choices = set(range(1,1,8))
        )
    args = parser.parse_args()

    exit(main(args))

