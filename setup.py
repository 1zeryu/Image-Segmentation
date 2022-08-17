import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name= "SegbyKmeans", 
    version = "1.0", 
    author="YuKun Zhou", 
    author_email="Yu-Kun-Zhou@outlook.com", 
    description="This is my first packages", 
    long_description=long_description, 
    long_description_content_type="text/markdown", 
    packages=setuptools.find_packages(), 
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    install_requires=[
        'opencv-python',
    ],
    python_requires=">=3",
    # url="https://github.com/1zeryu/Image-Segmentation", # github地址
)