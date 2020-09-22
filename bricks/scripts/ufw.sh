#!/bin/bash

echo $(ufw allow in "Apache Full")
echo 

echo $(ufw allow in "OpenSSH")
echo 

echo $(yes | ufw enable)
echo 
