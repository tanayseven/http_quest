#!/usr/bin/env bash
docker-compose run integration-tests poetry run pytest --cov http_quest --cov test/ || exit 1
aws s3 sync . s3://tanayseven-http-quest-backend-build/$TRAVIS_BUILD_NUMBER/coverage_files/ --exclude="*" --include ".coverage"
