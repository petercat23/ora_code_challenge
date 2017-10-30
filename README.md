# ora_code_challenge

#### About:

I've actually never had to adhere to the [JSON API](http://jsonapi.org/format/) schema standard before or implement a JWT authentication system (I've usually just stuck with DRF's standard token authentication scheme or a slightly tweaked version of it).

As such I leaned heavily on two third party packages [django-rest-framework-jwt](https://github.com/davesque/django-rest-framework-simplejwt) and [django-rest-framework-json-api](https://github.com/django-json-api/django-rest-framework-json-api) (both of which seemed active enough).

For the JWT authentication I had to slightly deviate from the packages intended use to meet the code challenges specifications and as such I'm not entirely confident I implemented the `rotational token` functionality correctly, but given a little more time/research or elucidation on how the api is/was intended to function it wouldn't be a problem to implement.

In regards to the requested API schema, while response bodies do adhere to the [JSON API](http://jsonapi.org/format/) format I did not match the responses exactly to the specified API responses (such as including any `links` fields. You'll have to forgive me but I was running a little short on time this weekend and while attention to detail IS important I figured you were more interested in the "core demostration" of knowledge over "exactness" since IMO the later only requires more elbow grease :) )


Test coverage is also sparser than I would normally implement but this was solely due to time constraints. For production code I would, obviously, ensure more robust coverage (testing 400's and stress the authentication system much more rigoriously then I did).

Throughout the code base are some specific comments regarding any design choices, observations, concerns, etc.

Please let me know if you have any questions or have trouble getting the project to start, etc.

Thanks so much!!!

#### Running the project

After building the project:

	$ docker-compose build

simply run:

	$ docker-compose up


#### Running Unit tests

After building the project:

	$ docker-compose build

simply run:

	$ docker-compose run web python manage.py test
