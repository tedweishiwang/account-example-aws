Package code and save binary to S3:
```
cd lambda
zip -r ../create_account.zip .
cd ..
aws s3 cp create_account.zip s3://my-account-lambda-code-bucket/create_account.zip
```

Deploy all resources in Cloudformation
```
aws cloudformation deploy \
  --template-file cloudformation.yaml \
  --stack-name CreateAccountStack \
  --capabilities CAPABILITY_NAMED_IAM
```

Test
```
{
  "name": "Alice",
  "password": "123456"
}
```