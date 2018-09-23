 chmod 777 bash.sh 
 docker build -t 360api:latest .
 docker run -d -p 5000:5000 360api