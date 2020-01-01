#!/usr/bin/env bash
heroku container:login || exit 1
heroku container:push web --app http-quest-backend || exit 1
heroku container:release web --app http-quest-backend || exit 1
curl --fail https://http-quest-backend.herokuapp.com/health || exit 1
