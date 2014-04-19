class App < ActiveRecord::Base
  # attr_accessible :description, :name, :package, :rating, :searchterm, :developer, :lastupdate, :installs, :website, :email, :privacypolicy, :ratings, :price
  has_and_belongs_to_many :permissions
  has_many :images
  has_many :comments

  scoped_search :on => [:name, :description]

  def self.more_apps_by_dev(app)
    where("developer = ? AND name != ?", app.developer, app.name).take(3)
  end
end
