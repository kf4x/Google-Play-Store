class AddPriceToApps < ActiveRecord::Migration
  def change
    add_column :apps, :price, :string
  end
end
