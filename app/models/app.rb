class App < ActiveRecord::Base
  attr_accessible :description, :name, :package, :rating, :searchterm, :developer, :lastupdate, :installs, :website, :email, :privacypolicy, :ratings
  has_and_belongs_to_many :permissions
  has_many :images
  has_many :comments

  def self.more_apps_by_dev(app)
    # would like to see this as a where statement
    # get 3 the apps by the developer
    tmp = find_all_by_developer(app.developer)
    # only get 3 that are not the same as current app
    tmp.select{|apps| apps.name!= app.name}.take(3)

  end
end
