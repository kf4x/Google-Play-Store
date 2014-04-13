# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
[
    "find accounts on the device",
    "approximate location (network-based)",
    "precise location (GPS and network-based)",
    "full network access"
].each do |perm|
  Permission.find_or_create_by_name(perm)
end


app2 = App.create({searchterm: "facebook",
                  package: "com.facebook.katana",
                  name: "Facebook",
                  rating: 3.9,
                  price: "FREE",
                  developer: 'Facebook',
                  lastupdate: 'March 21, 2014',
                  installs: "500,000,000 - 1,000,000,000",
                  website: 'https://www.facebook.com/FacebookMobile',
                  email: 'android-support@fb.com',
                  privacypolicy: 'https://www.facebook.com/about/privacy/',
                  ratings: 14902908,
                  description: 'Keeping up with friends is faster than ever.\nSee what friends are up to\nShare updates, photos and videos\net notified when friends like and comment on your posts\nText, chat and have group conversations\nPlay games and use your favorite apps\nNow you can get early access to the next version of Facebook for Android by becoming a beta tester. Learn how to sign up, givefeedback and leave the program in our Help Center: http://on.fb.me/133NwuP\nProblems downloading or installing the app? See http://bit.ly/GPDownload1\nStill need help? Please tell us more about the issue. http://bit.ly/invalidpackage\nFacebook is only available for users age 13 and over.\nTerms of Service: http://m.facebook.com/terms.php.'})

app3 = App.create({searchterm: "facebook",
                  package: "com.facebook.orca",
                  name: "Facebook Messenger",
                  rating: 4.2,
                  price: "FREE",
                  developer: 'Facebook',
                  lastupdate: 'April 9, 2014',
                  installs: "100,000,000 - 500,000,000",
                  website: 'https://www.facebook.com/FacebookMobile',
                  email: 'android-support@fb.com',
                  privacypolicy: 'https://www.facebook.com/about/privacy/',
                  ratings: 4003474,
                  description: 'Keeping up with friends is faster than ever.\nSee what friends are up to\nShare updates, photos and videos\net notified when friends like and comment on your posts\nText, chat and have group conversations\nPlay games and use your favorite apps\nNow you can get early access to the next version of Facebook for Android by becoming a beta tester. Learn how to sign up, givefeedback and leave the program in our Help Center: http://on.fb.me/133NwuP\nProblems downloading or installing the app? See http://bit.ly/GPDownload1\nStill need help? Please tell us more about the issue. http://bit.ly/invalidpackage\nFacebook is only available for users age 13 and over.\nTerms of Service: http://m.facebook.com/terms.php.'})

app1 = App.create({searchterm: "twitter",
                  package: "com.handmark.tweetcaster",
                  name: "TweetCaster for Twitter",
                  rating: 4.4,
                  price: "FREE",
                  developer: 'OneLouder Apps',
                  lastupdate: 'April 2, 2014',
                  installs: "10,000,000 - 50,000,000",
                  website: 'http://www.onelouder.com',
                  email: 'support@onelouder.com',
                  privacypolicy: 'https://tweetcaster.com/privacy',
                  ratings: 475805,
                  description: 'Keeping up with friends is faster than ever.\nSee what friends are up to\nShare updates, photos and videos\net notified when friends like and comment on your posts\nText, chat and have group conversations\nPlay games and use your favorite apps\nNow you can get early access to the next version of Facebook for Android by becoming a beta tester. Learn how to sign up, givefeedback and leave the program in our Help Center: http://on.fb.me/133NwuP\nProblems downloading or installing the app? See http://bit.ly/GPDownload1\nStill need help? Please tell us more about the issue. http://bit.ly/invalidpackage\nFacebook is only available for users age 13 and over.\nTerms of Service: http://m.facebook.com/terms.php.'})


app1.permissions << Permission.find(1)
app2.permissions << Permission.find(2)
app3.permissions << Permission.find(1)

comment2 = Comment.create({author:'rblutionkimmyb',
                          content: 'Where\'d the notification bar go?!? What the hell Facebook after the last update it tells me i have notifications but I open the app and there\'s no way to check them please fix not very convenient when I can\'t use my phone'})

comment3 = Comment.create({author:'Keltin Hamilton',
                          content: 'Great app! It\s a nice, reliable app and I personally have no issues or complaints at all other than not being able to share videos.'})

comment1 = Comment.create({author:'Kevin Queiroz',
                          content: 'Not too bad More options than the official app, don\'t like how it doesn\'t show who favorited or sometimes even retweeted your tweets though.'})

app2.comments << comment2
app3.comments << comment3
app1.comments << comment1