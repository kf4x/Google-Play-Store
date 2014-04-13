class ChangeInstallsTypeInApps < ActiveRecord::Migration
  def up
    change_column :apps, :installs, :string
  end

  def down
    change_column :apps, :installs, :integer
  end
end
