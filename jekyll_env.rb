require 'dotenv'
require 'gibbon'

Dotenv.load

Gibbon::Request.api_key = ENV['MAILCHIMP_API_KEY']
Gibbon::Request.timeout = 15
Gibbon::Request.open_timeout = 15