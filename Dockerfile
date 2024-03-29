FROM node:11.12.0-alpine as build-vue
WORKDIR /src
ENV PATH /src/node_modules/.bin:$PATH
COPY ./src/package*.json ./
RUN npm install
COPY ./src .
RUN npm run build

# production
FROM nginx:stable-alpine as production
WORKDIR /src
RUN apk update && apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY --from=build-vue /src/dist /usr/share/nginx/html
COPY /src/public/images /usr/share/nginx/html/images
COPY ./config/default.conf /etc/nginx/conf.d/default.conf
COPY ./src/api .
RUN pip3 install wheel
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
CMD gunicorn -b 0.0.0.0:5000 app:app --daemon && sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'
