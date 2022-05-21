import os, random
from jennie.ubuntu.nginxfiles import *
from jennie.ubuntu.uwsgifiles import *

def deploy_folder_nginx(port, domain):
    folder_to_serve = os.getcwd()
    os.system("apt-get install nginx -y")
    os.system("service nginx start")

    if port == "http":
        frontend_nginx_file = NGINX_HTTP_CONF
    elif port == "https":
        frontend_nginx_file = NGINX_HTTPS_CONF
    else:
        frontend_nginx_file = NGINX_PORT_CONF.replace("PORT", port)
    domain_name = domain.replace(".", "-")
    frontend_nginx_file = frontend_nginx_file.replace("DOMAIN", domain).replace("ROOT", folder_to_serve)
    open("/etc/nginx/conf.d/{}.conf".format(domain_name).format(), "w").write(frontend_nginx_file)
    os.system("sudo systemctl reload nginx")
    print ("\n\nFrontend Deployed on port {} on  domain {}n\n\nKindly Restart Nginx to make the effect work.\n".format(port, domain))



