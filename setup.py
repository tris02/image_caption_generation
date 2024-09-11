from setuptools import setup, find_packages

setup(
    name='image_caption_generation',
    version='0.1.0',
    description='A Python package for generating captions from webpage images and local images using Gradio and Salesforce BLIP model.',
    author='tristan',
    author_email='tris02@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests==2.31.0',
        'beautifulsoup4==4.12.3',
        'Pillow==10.4.0',
        'torch==2.2.1',
        'transformers==4.38.2',
        'huggingface-hub==0.24.6',
        'tokenizers==0.15.2',
        'gradio==4.44.0',
        'pytest==8.3.3',
        'pydantic==2.9.1',
        'langchain==0.1.11'
    ],
    entry_points={
        'console_scripts': [
            'caption_images_url=automate_url_captioner:main',  # For URL image captioning
            'caption_images_local=image_captioning_app:main'  # For Gradio-based local image captioning
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
