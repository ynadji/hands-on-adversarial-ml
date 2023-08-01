FROM jupyter/tensorflow-notebook:87210526f381

#Set the working directory
WORKDIR /home/jovyan/

# cleverhans -> tensorflow-probability doesn't specify a version for dm-tree
# and newer versions depend on cmake 3.12 but the rest of the docker image is
# old enough this cascades into another series of problems. just install a
# version around the same time frame so the dependency is handled.
RUN pip install dm-tree==0.1.2

# Modules
COPY requirements.txt /home/jovyan/requirements.txt
RUN pip install -r /home/jovyan/requirements.txt

# Add files
COPY notebooks /home/jovyan/notebooks
COPY data /home/jovyan/data
COPY solutions /home/jovyan/solutions
COPY util /home/jovyan/util

# Allow user to write to directory
USER root
RUN chown -R $NB_USER /home/jovyan \
    && chmod -R 774 /home/jovyan
USER $NB_USER

# Expose the notebook port
EXPOSE 8888

# Start the notebook server
CMD jupyter notebook --no-browser --port 8888 --ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.disable_check_xsrf=True --NotebookApp.iopub_data_rate_limit=1.0e10
