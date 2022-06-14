#this is our "base" image
#FROM continuumio/miniconda3
FROM condaforge/mambaforge

#Input some test data that we can use
RUN mkdir /data
COPY tpl-MNI152NLin2009cAsym_res-01_T1w.nii.gz /data/t1.nii.gz
COPY tpl-MNI152NLin2009cAsym_res-01_T2w.nii.gz /data/t2.nii.gz


#create environment with packages specified in yml file
COPY environment.yml .
RUN conda env create -f environment.yml

#tell the dockerfile to use the conda shell instead of default shell
SHELL ["conda", "run", "-n", "example_container", "/bin/bash", "-c"]

#load the python script and tell docker to run that script
#when someone tries to execute the container
RUN mkdir /code
COPY run.py /code/run.py
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "example_container", "python", "/code/run.py"]

RUN chmod 555 -R /code /data
