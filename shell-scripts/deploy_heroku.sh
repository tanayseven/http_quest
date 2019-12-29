#!/usr/bin/env bash
heroku container:push web --app http-quest-backend || exit 1
heroku container:release web --app http-quest-backend || exit 1
