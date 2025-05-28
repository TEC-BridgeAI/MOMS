FROM public.ecr.aws/lambda/python:3.9

# Copy requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install dependencies
RUN pip install -r requirements.txt

# Copy function code
COPY backend/ ${LAMBDA_TASK_ROOT}/backend/
COPY handlers/ ${LAMBDA_TASK_ROOT}/handlers/
COPY wsgi_handler.py ${LAMBDA_TASK_ROOT}

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=moms_project.settings.serverless
ENV PYTHONPATH=${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD [ "wsgi_handler.handler" ]