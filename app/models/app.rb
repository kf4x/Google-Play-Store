class App < ActiveRecord::Base
  attr_accessible :description, :name, :package, :rating, :searchterm, :developer, :lastupdate, :installs, :website, :email, :privacypolicy, :ratings
  has_and_belongs_to_many :permissions
  has_many :images
  has_many :comments
end
