class CreateApps < ActiveRecord::Migration
  def change
    create_table :apps do |t|
      t.string :name
      t.string :package
      t.string :searchterm
      t.string :description
      t.float :rating

      t.timestamps
    end
  end
end
