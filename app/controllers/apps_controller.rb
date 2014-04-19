class AppsController < ApplicationController


  def show
    @app = App.find_by_package(params[:id])
    # puts(@app.description)

    @more_by_dev = App.more_apps_by_dev(@app)

  end

  def list
    @apps = App.all
  end

  def list_by_search
    @apps = App.search_for(params[:q])
    # puts(params[:q])
    render :template => 'apps/list'
  end

  def list_by_dev
    @apps = App.find_all_by_developer(params[:dev])

    render :template => 'apps/list'
  end

end
