## Motivational Quote Video Generator

Python-based application that allows you to create inspiring and motivational quote videos. With the help of the MoviePy library, this tool enables you to combine beautiful background images, captivating animations, and motivating quotes to produce engaging videos that inspire and uplift.

Example: 
https://www.youtube.com/shorts/Z83-qnzxwD8


## Installation Guide

This guide will walk you through the installation process for the "Motivational Quote Video Generator" using Python and MoviePy. The installation will be done using a requirements file, which will ensure that all the necessary dependencies are installed correctly.

### Install Dependencies

```
pip install -r requirements.txt
```


## Configure the Generator
Before running the generator, you need to obtain a Pexels API key and configure it in the `config.ini` file. Here's how:

1. Visit the Pexels API website: [https://www.pexels.com/api/](https://www.pexels.com/api/)
    
2. Sign up for an account and obtain an API key. The API key is required to fetch background images for the motivational quote video.
    
3. Open the `config.ini` file in a text editor.
    
4. Look for the `[DEFAULT]` section in the `config.ini` file.
    
5. Replace the placeholder value `<Api-key>` with your actual Pexels API key. The section should look like this:
```
[DEFAULT]
PexelsApiKey=<Api-key>
```

### Generate the Motivational Quote Video
To generate the motivational quote video, run the following command:
```
python generate_video.py
```

