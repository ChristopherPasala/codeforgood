# Makefile
## 🌶 flask and hot-reload
flask:
	docker-compose up -d

flask-debug:
	docker-compose -f docker-compose.yml -f docker-compose.debug.yml up
