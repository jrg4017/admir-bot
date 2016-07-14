[![Build Status](https://travis-ci.org/jrg4017/admir-bot.svg?branch=master)](https://travis-ci.org/jrg4017/admir-bot)

Build is pretty simple for now, but hopefully will be updated.


# Branches

Please make your pull requests against `Develop`. This branch pushes to dev for the final stages of testing.
You can request to join the HipChat and Slack channels for testing the integration in real time.

Once testing is passed, the feature will appear in Master which gets pushed to production. This integration can be
used by anyone.

# Documentation:

## Extending Admir Bot for other chat clients.

The nice thing about the Admir Bot is that the integrations are designed in such a way that you only really need to set `command` and `command_message` in order for the bot to perform the neccessary actions.

The individual files in the integration folder handle the parsing of request, formatting the response, and any chat client specific needs.

## Developing features
Since the necessary information is typically the `command` and the `command_message` we are able to develop features independent of chat client needs. Those specifics are handled in each file.
