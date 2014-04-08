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


app = App.create({searchterm: "facebook",
                  package: "com.facebook.katana",
                  name: "Facebook",
                  rating: 3.9,
                  description: 'Keeping up with friends is faster than ever.\nSee what friends are up to\nShare updates, photos and videos\net notified when friends like and comment on your posts\nText, chat and have group conversations\nPlay games and use your favorite apps\nNow you can get early access to the next version of Facebook for Android by becoming a beta tester. Learn how to sign up, givefeedback and leave the program in our Help Center: http://on.fb.me/133NwuP\nProblems downloading or installing the app? See http://bit.ly/GPDownload1\nStill need help? Please tell us more about the issue. http://bit.ly/invalidpackage\nFacebook is only available for users age 13 and over.\nTerms of Service: http://m.facebook.com/terms.php.'})

app.permissions << Permission.find(1)

comment = Comment.create({author:'rblutionkimmyb',
                          content: 'Where\'d the notification bar go?!? What the hell Facebook after the last update it tells me i have notifications but I open the app and there\'s no way to check them please fix not very convenient when I can\'t use my phone'})

app.comments << comment