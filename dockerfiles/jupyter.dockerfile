FROM jupyter/base-notebook
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888
COPY . . 