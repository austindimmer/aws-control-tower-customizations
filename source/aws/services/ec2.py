##############################################################################
#  Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.   #
#                                                                            #
#  Licensed under the Apache License, Version 2.0 (the "License").           #
#  You may not use this file except in compliance                            #
#  with the License. A copy of the License is located at                     #
#                                                                            #
#      http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                            #
#  or in the "license" file accompanying this file. This file is             #
#  distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY  #
#  KIND, express or implied. See the License for the specific language       #
#  governing permissions  and limitations under the License.                 #
##############################################################################

# !/bin/python

from botocore.exceptions import ClientError
from aws.utils.boto3_session import Boto3Session


class EC2(Boto3Session):
    def __init__(self, logger, region, **kwargs):
        self.logger = logger
        __service_name = 'ec2'
        kwargs.update({'region': region})
        super().__init__(logger, __service_name, **kwargs)
        self.ec2_client = super().get_client()

    def describe_availability_zones(self, name='state', value='available'):
        try:
            response = self.ec2_client.describe_availability_zones(
                Filters=[
                    {
                        'Name': name,
                        'Values': [value]
                    }
                ]
            )
            return [resp['ZoneName'] for resp in response['AvailabilityZones']]
        except ClientError as e:
            self.logger.log_unhandled_exception(e)
            raise

    def create_key_pair(self, key_name):
        try:
            response = self.ec2_client.create_key_pair(
                KeyName=key_name
            )
            return response
        except ClientError as e:
            self.logger.log_unhandled_exception(e)
            raise
