#!/bin/bash
# call this file with . set-env-vars.sh
export DIST_OUTPUT_BUCKET=custom-control-tower-configuration-291460973700-eu-west-1 # Name for the S3 bucket where customized code will reside
export TEMPLATE_OUTPUT_BUCKET=custom-control-tower-configuration-291460973700-eu-west-1 # Name for the S3 bucket where the template will be located
export SOLUTION_NAME=customizations-for-aws-control-tower # name of the solution
export VERSION=1.1.1 # version number for the customized code