#!/usr/bin/env python3

import os
import requests
import json
import subprocess
import argparse

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def setup_arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""This tool uses AI to generate ascii art from a given prompt.""",
        epilog="""
        Copyright © 2024 Kane Sweet <kanesweet11@gmail.com>
        Distributed under the Apache License Version 2.0 (Apache-2.0)
        For further details, visit https://github.com/sweetkane/artscii"""
    )
    
    parser.add_argument(
        'prompt', 
        nargs=1, 
        help='description of the desired image'
    )
    parser.add_argument(
        *['-c', '--cache'],
        help="save the OpenAI response to a json file in the current directory",
        action='store_true'
    )
    parser.add_argument(
        #*['-f', '--flags'], 
        'flags',
        nargs=argparse.REMAINDER,
        help='flags to be passed to ascii-image-converter. run `ascii-image-converter -h` for more details'
    )
    return parser.parse_args()
    

def check_requirements():
    if subprocess.run(["ascii-image-converter", "-h"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
        print("ERR: Missing `ascii-image-converter` package.")
        print("ERR: See: https://github.com/TheZoraiz/ascii-image-converter?tab=readme-ov-file#installation")
        exit(1)
    if not OPENAI_API_KEY:
        print("ERR: OPENAI_API_KEY environment variable not set.")
        print("ERR: See: https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key")
        exit(1)


def main():
    check_requirements()
    args = setup_arg_parser()

    # generate image
    headers = {
        'Authorization': f"Bearer {OPENAI_API_KEY}",
    }
    json_data = {
        'model': 'dall-e-3',
        'prompt': args.prompt[0] + " (this image will be converted to ascii art)",
        'n': 1,
        'size': '1024x1024',
    }
    response = requests.post(
        url='https://api.openai.com/v1/images/generations', 
        headers=headers, 
        json=json_data
    ).json()

    # convert to ascii
    img_url = response["data"][0]["url"]
    subprocess.call(["ascii-image-converter", img_url] + args.flags)

    # handle cache
    if (args.cache):
        try:
            with open('artscii.cache.json', 'r') as fp:
                cachedic = json.loads(fp.read())
        except:
            cachedic = {"openai_responses": []}
        with open('artscii.cache.json', 'w') as fp:
            cachedic["openai_responses"].append(response)
            json.dump(cachedic, fp)

            
if __name__ == '__main__':
    main()
