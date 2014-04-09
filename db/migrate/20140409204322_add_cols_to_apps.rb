class AddColsToApps < ActiveRecord::Migration
  def change
    add_column :apps, :developer, :string
    add_column :apps, :lastupdate, :string
    add_column :apps, :installs, :integer
    add_column :apps, :website, :string
    add_column :apps, :email, :string
    add_column :apps, :privacypolicy, :string
    add_column :apps, :ratings, :integer
  end
end
