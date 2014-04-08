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


app = App.create({searchterm: "facebook", package: "com.facebook.katana", name: "Facebook", rating: 4.3, description: 'fb'})

app.permissions << Permission.find(1)

comment = Comment.create({author:'rblutionkimmyb', content: 'Where\'d the notification bar go?!? What the hell Facebook after the last update it tells me i have notifications but I open the app and there\'s no way to check them please fix not very convenient when I can\'t use my phone'})

app.comments << comment