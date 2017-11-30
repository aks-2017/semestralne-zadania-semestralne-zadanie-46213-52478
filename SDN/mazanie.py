#!/usr/bin/python

from subprocess import call

call(["curl","-X DELETE","-d {\"route_id\": \"1\"}","http://localhost:8080/router/0000000000000001"])

