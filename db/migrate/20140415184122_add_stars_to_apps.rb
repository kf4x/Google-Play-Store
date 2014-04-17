class AddStarsToApps < ActiveRecord::Migration
  def change
    add_column :apps, :fivestars, :integer
    add_column :apps, :fourstars, :integer
    add_column :apps, :threestars, :integer
    add_column :apps, :twostars, :integer
    add_column :apps, :onestar, :integer
  end
end
