FROM us.gcr.io/jupyterhub-170614/<series_id>:<single user version>

USER root

# notebook and ipykernel should already be installed. now just need jupyterhub
RUN pip install --upgrade --no-cache-dir jupyterhub==0.8.1

# Specify tornado==4.5.3
RUN pip install --upgrade --no-cache-dir tornado==4.5.3

USER jovyan

WORKDIR /home/jovyan

# css stuff
RUN for i in `find / -wholename /opt/conda/*/custom.css 2>/dev/null` ; \
  do echo "@import url(\"https://cdn.oreillystatic.com/jupyterhub/jupyterhub-theme/custom/custom.css\")" \
  | tee ${i}; done

CMD jupyterhub-singleuser \
  --port=8888 \
  --ip=0.0.0.0 \
  --user="$JPY_USER" \
  --cookie-name=$JPY_COOKIE_NAME \
  --base-url=$JPY_BASE_URL \
  --hub-prefix=$JPY_HUB_PREFIX \
  --hub-api-url=$JPY_HUB_API_URL \

