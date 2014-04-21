class ChangeDescriptionAndContentFormat < ActiveRecord::Migration
  def up
    change_column :apps, :description, :text, :limit => nil
    change_column :comments, :content, :text, :limit => nil
  end

  def down
    change_column :apps, :description, :string
    change_column :comments, :content, :string
  end
end
