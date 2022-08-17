# **Image Segmentation**

**Background**: Image segmentation has a wide range of applications. It can assist in complex tasks in medicine, industry. Most of the open source use complicated algorithm to make it. I implement the classical machine learning algorithm to achieve it. The project has convient interface  

### Usage: 

```bash
git clone https://github.com/1zeryu/Image-Segmentation.git
```

The main code is in SegByKmeans directory. 

Before usage, you must make a example directory through

```bash
cd SegByKmeans
mkdir example
```

The main parameters are as follows:

```bash
usage: Seg.py [-h] [-k K] [--MaxIter MAXITER] [--seed SEED]
              [--resultPath RESULTPATH]
              ImageName

hyper parameters for kmeans

positional arguments:
  ImageName             select the image file name, must in the example
                        directory

optional arguments:
  -h, --help            show this help message and exit
  -k K                  number of center
  --MaxIter MAXITER     max iterations of kmeans algorithm
  --seed SEED           seed for random center
  --resultPath RESULTPATH
                        Specify the path to the generated file, the default is
                        the current folder
```

