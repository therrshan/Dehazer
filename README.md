# DEHAZER
<img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/> <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>

This repository consists the code for the application developed for the final year project that used the custom model for depth prediction and predicts depth on image and video feed. The application also show cases the use of these depth maps as transmission maps in AODNET for fog removal and can remove the fog from any given input hazy image and display the clean image. The code for the depth map testing is explained in this [repo](https://github.com/therrshan/Monodepth-GIFTest) and the code for the fig removal is explained [here](https://github.com/therrshan/FogRemoval-AODNET)

## Summary

This app was developed using the Flask  web app framework of python language and was optimized for deployment on the heroku platform. The execution of the application is as given below.

## How to run
The code runs on Python 3.6+, Pytorch 0.4.1 and has a couple of other requirements which are specisified in the 'requirements.txt' which can be easily installed on a fresh virtual enviornment using the pip command.

```shell
pip install -r Requirements.txt
```

The project directory consists of the models and their files in the respective folders which are used by the app backend to predict and display the results. The main backend runs from the app.py in the root directory, thus to run the application on the local host just execute the following after sucessfull creation of the envioenment with the requirements.

```shell
python3 app.py or flask run
```


