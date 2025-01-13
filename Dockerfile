FROM jupyter/base-notebook
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# WORKDIR /project
EXPOSE 8888
COPY . .
# CMD ["python", "start-notebook.py"]