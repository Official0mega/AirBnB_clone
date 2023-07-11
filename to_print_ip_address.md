To set up..please run

### ./0-setup_web_static.sh
* This script will handle the installation and configuration of the web server (e.g., Nginx) to serve the web application.


### ./3-deploy_web_static.py
* execute this script to deploy the web application
* This script will handle the deployment of your web application, including copying the static files to the appropriate location and configuring the web server to serve the application.


### sudo service nginx status
* To verify if Nginx is running, you can execute the following command:


### sudo service nginx start
* If Nginx is running, you should see a message indicating its status. If it's not running, you can start it using the following command:

### To find the IP address of your server, you can use the following command:
* ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'


### ip addr show eth0 | grep inet
* Verify IP address: Double-check the IP address of your server by running the command




