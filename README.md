# 🖼️ artscii
This tool uses AI to generate ascii art from a given prompt.             
![Screenshot 2024-03-13 at 5 06 36 PM](https://github.com/sweetkane/artscii/assets/71854758/451a3c17-ab7c-4421-8dd3-a52cb007abd0)
## Installation
### Homebrew
To install artscii with Homebrew, run:
```
brew install sweetkane/artscii/artscii
```
[tap repo](https://github.com/sweetkane/homebrew-artscii)

## Usage
Note: To use artscii, the `OPENAI_API_KEY` environment variable must be set.
The most basic usage is to simply invoke the tool and supply a prompt.
It will look like this:
```
artscii "a scene in the swiss alps"
```
### Options
You can specify many options to customize the way your image is converted to ascii. Add any number of these options after the prompt.
To output an image with color, you can run:
```
artscii "a scene in the swiss alps" --color
```
To use braille characters AND color, you can run:
```
artscii "a scene in the swiss alps" --braille --color
```
These options are actually passed directly to the `ascii-image-converter` program, a third party dependency of `artscii`. 
A full list of options can be found [here](https://github.com/TheZoraiz/ascii-image-converter?tab=readme-ov-file#flags)

### Caching
You can cache the OpenAI API response, which contains the raw image, using the `-c` option before the prompt.
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


## Packages Used
https://github.com/TheZoraiz/ascii-image-converter


