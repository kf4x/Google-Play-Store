class ChangeDescriptionAndContentFormat < ActiveRecord::Migration
  def up
    change_column :apps, :description, :text
    change_column :comments, :content, :text
  end

  def down
    change_column :apps, :description, :string
    change_column :comments, :content, :string
  end
end
