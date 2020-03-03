### Install Python Dependencies
AWS Lambda runs on Amazon Linux distributions. Some Python packages
that have C dependencies need to be installed as if we were using an
Amazon Linux distribution. For this reason, we install inside a Docker
container running an Amazon Linux distribution. The current volume is 
mounted so we can zip these files later outside the container.

```bash
$ docker build -f Dockerfile -t serverless:latest .
$ docker run -it -v "$PWD":/serverless serverless:latest bash
```
Then inside the container:

```bash
$ pip install -t . -r requirements.txt
```

Then back outside the container:

```bash
$ zip -r handler.zip .
```