class App < ActiveRecord::Base
  attr_accessible :description, :name, :package, :rating, :searchterm, :developer, :lastupdate, :installs, :website, :email, :privacypolicy, :ratings, :price
  has_and_belongs_to_many :permissions
  has_many :images
  has_many :comments

  scoped_search :on => [:name, :description]

  def self.more_apps_by_dev(app)
    #TODO add where statement where app.devname == name && app.name != app

    # get all the apps by the developer
    tmp = find_all_by_developer(app.developer)
    # only get 3 that are not the same as current app
    tmp.select{|apps| apps.name!= app.name}.take(3)

  end
end
