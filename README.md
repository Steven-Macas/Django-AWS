<div align="center">

# Django + AWS Image Gallery

**Image uploads with Django, storage on Amazon S3 and label detection with Rekognition**

<img src="https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python: 3" /> <img src="https://img.shields.io/badge/Django-web-092E20?style=flat-square&logo=django&logoColor=white" alt="Django: web" /> <img src="https://img.shields.io/badge/AWS-S3%20%C2%B7%20Rekognition-232F3E?style=flat-square" alt="AWS: S3 · Rekognition" />

</div>

## Overview

A Django web application to upload and display images, together with a notebook that connects to
**Amazon Web Services** with `boto3`: it uploads images to an **S3** bucket and analyses them with
**Amazon Rekognition** (`detect_labels`).

## Repository structure

| Path | Description |
| --- | --- |
| `server/` | Django project settings and URLs |
| `members/` | App with the image model, upload form, views and templates |
| `members/static/faceApp/` | CSS, JavaScript and images |
| `gallery_images/` | Uploaded images |
| `aws_boto3.ipynb` | S3 upload and Rekognition label detection with `boto3` |
| `db.sqlite3` | Development database |

## How to run

```bash
pip install django pillow boto3 python-dotenv
python manage.py migrate
python manage.py runserver      # http://127.0.0.1:8000
```

For the AWS notebook, load your credentials from environment variables or a `.env` file
(`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_DEFAULT_REGION`)
instead of writing them in the code.

---

<sub>Made by <b>Steven Macas</b> — Data Engineer &amp; Data Analyst · <a href="https://gointy.com">gointy.com</a> · <a href="https://www.linkedin.com/in/steven-macas">LinkedIn</a> · <a href="https://github.com/Steven-Macas">GitHub</a></sub>
