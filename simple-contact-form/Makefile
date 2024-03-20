# Migrations
make-migrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate

# Superuser
create-superuser:
	docker-compose run web python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@meant4.com', 'admin123')"

# Non-admin user
create-user:
	docker-compose run web python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('testuser', 'testuser@meant4.com', 'test1234')"

docker-up:
	docker-compose up -d --remove-orphans --build

docker-down:
	docker-compose down

load-fixtures:
	docker-compose run web python manage.py loaddata contacts.json --app contacts.Contact

docker-logs:
	docker-compose logs -f

test-contacts:
	docker-compose run web pytest

run-coverage:
	docker-compose run web coverage run -m pytest

coverage-html:
	docker-compose run web coverage html
