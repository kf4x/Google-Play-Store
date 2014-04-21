# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended to check this file into your version control system.

ActiveRecord::Schema.define(:version => 20140421042033) do

  create_table "apps", :force => true do |t|
    t.string   "name"
    t.string   "package"
    t.string   "searchterm"
    t.string   "image"
    t.text     "description",   :limit => 255
    t.float    "rating"
    t.datetime "created_at",                   :null => false
    t.datetime "updated_at",                   :null => false
    t.string   "developer"
    t.string   "lastupdate"
    t.string   "installs"
    t.string   "website"
    t.string   "email"
    t.string   "privacypolicy"
    t.integer  "ratings"
    t.string   "price"
    t.integer  "fivestars"
    t.integer  "fourstars"
    t.integer  "threestars"
    t.integer  "twostars"
    t.integer  "onestar"
  end

  create_table "apps_permissions", :id => false, :force => true do |t|
    t.integer "app_id"
    t.integer "permission_id"
  end

  create_table "comments", :force => true do |t|
    t.string   "author"
    t.text     "content",    :limit => 255
    t.integer  "app_id"
    t.datetime "created_at",                :null => false
    t.datetime "updated_at",                :null => false
  end

  create_table "images", :force => true do |t|
    t.string   "location"
    t.integer  "app_id"
    t.datetime "created_at", :null => false
    t.datetime "updated_at", :null => false
  end

  create_table "permissions", :force => true do |t|
    t.string   "name"
    t.string   "description"
    t.datetime "created_at",  :null => false
    t.datetime "updated_at",  :null => false
  end

end
