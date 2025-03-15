require 'sinatra'
require 'gibbon'

post '/subscribe' do
  content_type :json
  request.body.rewind
  data = JSON.parse(request.body.read)
  email = data['email']

  gibbon = Gibbon::Request.new
  list_id = ENV['MAILCHIMP_LIST_ID']

  begin
    gibbon.lists(list_id).members.create(
      body: {
        email_address: email,
        status: 'subscribed'
      }
    )
    { message: 'Subscription successful!' }.to_json
  rescue Gibbon::MailChimpError => e
    status 500
    { error: e.message }.to_json
  end
end
