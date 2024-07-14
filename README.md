# 🖼️ artscii
This command line tool uses AI to generate ascii art from a text prompt.             
![Screenshot 2024-03-13 at 5 06 36 PM](https://github.com/sweetkane/artscii/assets/71854758/451a3c17-ab7c-4421-8dd3-a52cb007abd0)

## Overview

Artscii is a simple command line tool that:
1. Makes a call to [OpenAI's image generation API](https://platform.openai.com/docs/api-reference/images)
2. Converts the image to ascii using [ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter)
3. Outputs the ascii art to the command line

## Installation
### Homebrew
To install artscii with Homebrew, run:
```
brew install sweetkane/tap/artscii
```
[tap repo](https://github.com/sweetkane/homebrew-tap)

## Usage
**Note: To use artscii, the `OPENAI_API_KEY` environment variable must be set.**

The most basic usage is to simply invoke the tool and supply a prompt.
It will look like this:
```
artscii "a scene in the swiss alps"
```
### Options
You can specify many options to customize the way your image is converted to ascii. Add any number of these options after the prompt.
These options are actually passed directly to the `ascii-image-converter` program, a third party dependency of `artscii` with many options for customizing the output.

To output an image with color, you can run:
```
artscii "a scene in the swiss alps" --color
```
To use braille characters AND color, you can run:
```
artscii "a scene in the swiss alps" --braille --color
```

A full list of options can be found [here](https://github.com/TheZoraiz/ascii-image-converter?tab=readme-ov-file#flags)

### Caching
You can cache the OpenAI API response json, which contains a link to the raw image, by adding the `-c` flag before the prompt.
It will look like this:
```
artscii -c "a scene in the swiss alps"
```
The cache will be created as `artscii.cache.json` in your working directory. The program will append to the cache if one already exists.

## Gallery
<img width="544" alt="Screenshot 2024-03-18 at 12 49 35 PM" src="https://github.com/sweetkane/artscii/assets/71854758/000318b6-bbbb-4665-9c86-9f379f98873b">
<img width="689" alt="Screenshot 2024-03-18 at 12 15 48 PM" src="https://github.com/sweetkane/artscii/assets/71854758/46465c1e-0a76-4bde-b11f-870416849f92">
<img width="711" alt="Screenshot 2024-03-18 at 12 22 39 PM" src="https://github.com/sweetkane/artscii/assets/71854758/674ce661-aa3d-4a5c-bfe1-46f22ec6f6ac">
<img width="667" alt="Screenshot 2024-03-18 at 12 23 53 PM" src="https://github.com/sweetkane/artscii/assets/71854758/9ca1e59c-8eeb-4e62-b431-f9feb2760e40">
<img width="976" alt="Screenshot 2024-03-26 at 4 19 49 PM" src="https://github.com/sweetkane/artscii/assets/71854758/47619704-de82-4448-a503-34748582d32c">


## Packages Used
https://github.com/TheZoraiz/ascii-image-converter

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


