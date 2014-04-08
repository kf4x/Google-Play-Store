class CreateAppsPermissionsJoin < ActiveRecord::Migration
  def up
    create_table 'apps_permissions', :id => false do |t|
      t.column 'app_id', :integer
      t.column 'permission_id', :integer
    end
  end

  def down
    drop_table 'apps_permissions'
  end
end
