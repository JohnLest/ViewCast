FROM python:3.9
WORKDIR /
COPY ./ViewCast/requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
copy ./ViewCast/ /
RUN ls -la /
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=40100"]
