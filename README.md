# wasuaje.com Site


This is a personal docker stack made to set up a small pipeline on my personal website, this
stack uses a docker-compose,  with nginx, django and mysql images exposed sharing volumes, this 
allows nginx to serve statics while uwsgi serve dynamic content.



**Notice**

Don't forget to connect to mysql container to make django test work


```
docker exec %(docker ps | grep mysql ) mysql -uroot -p
GRANT ALL PRIVILEGES ON mydb.* TO 'myser'@'%' IDENTIFIED BY 'your_password' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```