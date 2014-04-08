class CreateComments < ActiveRecord::Migration
  def change
    create_table :comments do |t|
      t.string :author
      t.string :content
      t.integer :app_id

      t.timestamps
    end
  end
end
