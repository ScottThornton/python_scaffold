#!/usr/bin/env python3

import click
import boto3

@click.command(help="This tool does label detection")
@click.command('--bucket', prompt='Provide the name of the bucket')
@click.command('--file', prompt='Provide the name of the file')

def tagImage(bucketName, fileName):
    client = boto3.client('rekognition')

    response = client.detect_labels(
        Image={
          'S3Object': {
                'Bucket': bucketName,
                'Name': fileName,
            },
          },  
    )
    return response

if __name__ == '__main__':
    # pylint: disable=E1120
    tagImage()

output = tagImage('boxoffrogs.mybucket', 'Grumpy_Kitty.jpg')
print (output)