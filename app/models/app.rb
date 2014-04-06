class App < ActiveRecord::Base
  attr_accessible :description, :name, :package, :rating, :searchterm
end
