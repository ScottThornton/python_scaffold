#!/usr/bin/env python3

import boto3


def tagImage(bucket, file):
    client = boto3.client("rekognition")

    response = client.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": file,
            },
        },
    )
    return response


output = tagImage("boxoffrogs.mybucket", "Grumpy_Kitty.jpg")
print (output)
