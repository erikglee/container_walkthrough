#Python base image
FROM python:latest

# Prepare environment
RUN python3 -m pip install numpy==1.19.2
RUN python3 -m pip install nibabel==3.2.2
RUN python3 -m pip install matplotlib==3.5.1


#Input some test data that we can use
RUN mkdir /data
COPY tpl-MNI152NLin2009cAsym_res-01_T1w.nii.gz /data/t1.nii.gz
COPY tpl-MNI152NLin2009cAsym_res-01_T2w.nii.gz /data/t2.nii.gz


#load the python script and tell docker to run that script
#when someone tries to execute the container
RUN mkdir /code
COPY run.py /code/run.py
ENTRYPOINT ["python3", "/code/run.py"]

RUN chmod 555 -R /code /data
