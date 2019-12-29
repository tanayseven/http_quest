#!/usr/bin/env bash
aws s3 sync s3://tanayseven-http-quest-backend-build/$TRAVIS_BUILD_NUMBER/coverage_files/ .
docker-compose run integration-tests poetry run coveralls
