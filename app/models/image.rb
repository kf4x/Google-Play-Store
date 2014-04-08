class Image < ActiveRecord::Base
  attr_accessible :location

  belongs_to :app
end
