rm -rf planship_openapi_gen
mkdir planship_openapi_gen
cp openapitools.json planship_openapi_gen/
cd planship_openapi_gen
npx @openapitools/openapi-generator-cli generate -g python -i http://localhost:8002/openapi.json --additional-properties=packageName=planship_openapi_gen
