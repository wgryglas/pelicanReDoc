FROM gcr.io/cloud-builders/gcloud


RUN pip install --no-cache-dir --upgrade setuptools
RUN pip install --no-cache-dir --upgrade docutils
RUN pip install --no-cache-dir --upgrade pelican
RUN pip install --no-cache-dir --upgrade loremipsum 
RUN pip install --no-cache-dir --upgrade invoke
RUN pip install --no-cache-dir --upgrade xhtml2pdf
RUN pip install --no-cache-dir --upgrade rst2pdf


ENTRYPOINT ["invoke"]
