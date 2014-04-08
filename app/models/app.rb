class App < ActiveRecord::Base
  attr_accessible :description, :name, :package, :rating, :searchterm
  has_and_belongs_to_many :permissions
end
